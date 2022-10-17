from flask import request, render_template, redirect, url_for, session, make_response
from flask_babel import gettext

from src import app
from src.config import DEBUG
from src.controllers.user_db import UsersDB
from src.controllers.german_abstracts_db import GermanAbstractsDB

user_db = UsersDB()
abstract_db = GermanAbstractsDB()


@app.route('/home', methods=['GET', 'POST'])
def index():
    if "username" not in session:
        return redirect(url_for('signup'))
    return render_template('index.html', username=session["username"], annotations=session["annotations"],
                           level=session["level"])


@app.route('/reward', methods=['GET', 'POST'])
def reward():
    if "username" not in session:
        return redirect(url_for('signup'))
    return render_template('reward.html', username=session["username"], annotations=session["annotations"],
                           level=session["level"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        param = request.form.to_dict()
        user = {'username': param['username']}
        print(user)
        result = user_db.login(user)
        print("result", result)
        if result["status"]:
            session.permanent = True  # this session will be exist for 5 days.
            session["username"] = user["username"]  # create a session for user.
            return redirect(url_for('index'))  # welcome page after login
        else:
            message = result["error"]
            return render_template('signup.html', title='login', message=message)
    if "username" in session:  # if user already logged in
        if DEBUG:
            print("[STEP] Already logged in user!")
        return redirect(url_for('index'))

    return render_template('signup.html', title='login')


@app.route('/', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        param = request.form.to_dict()
        print(param)
        result = user_db.new_user(param)
        print("result", result)
        if result["status"]:
            session.permanent = True  # this session will be exist for 5 days.
            session["username"] = param["username"]  # create a session for user.
            session["annotations"] = param["annotations"]
            session["level"] = param["level"]
            # create a session for user.
            return redirect(url_for('index'))  # welcome page after login
        else:
            message = result["error"]
            return render_template('signup.html', title='sign up', message=message)
    if "username" in session:  # if user already logged in
        if DEBUG:
            print("[STEP] Already logged in user!")
        return redirect(url_for('index'))
    return render_template('signup.html', title='sign up')


@app.route('/change_pass', methods=['GET', 'POST'])
def change_pass():
    if "username" not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        result = user_db.change_password(session["username"], request.form.to_dict())
        print(result)
    return render_template('change_pass.html', title='change password', username=session["username"])


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if "username" in session:
        session.pop("username", None)
    return redirect(url_for('login'))


def get_current_level(param):
    if param < 2:
        return gettext("annotation newbee")
    elif 2 <= param < 4:
        return gettext("research supporter")
    elif 4 <= param < 6:
        return gettext("ambitious annotator")
    elif 6 <= param < 8:
        return gettext("annotation star")
    elif 8 <= param < 10:
        return gettext("annotation master")
    elif param >= 10:
        return gettext("legendary annotator")


@app.route('/technicality', methods=['GET', 'POST'])
def technicality():
    if "username" not in session:
        return redirect(url_for('signup'))
    _doc = abstract_db.get_document(session['username'])
    if request.method == 'POST':
        abstract_db.add_document_annotation(username=session['username'], _id=session["_docID"],
                                            param=request.form.to_dict())
        _doc["annotations"] = session["annotations"] + 1
        session["annotations"] = _doc["annotations"]
        _doc["level"] = get_current_level(session["annotations"]);
        session["level"] = _doc["level"]
        _doc["username"] = session["username"]
        user_db.update_user(_doc);
        return redirect(url_for('reward'))
    if not _doc["status"]:
        print("This is an error needs to be handled later!")
    session["_docID"] = _doc["value"]['_id'].__str__()
    return render_template('technicality.html', title='Annotate Technicality', doc=_doc["value"])
