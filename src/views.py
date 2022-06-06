from flask import request, render_template, redirect, url_for, session

from src import app
from src.config import DEBUG
from src.controllers.user_db import UsersDB
from src.controllers.german_abstracts_db import GermanAbstractsDB

user_db = UsersDB()
abstract_db = GermanAbstractsDB()


@app.route('/home', methods=['GET', 'POST'])
def index():
    if "username" not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session["username"])


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        param = request.form.to_dict()
        user = {'username': param['username'], 'password': param['password']}
        print(user)
        result = user_db.login(user)
        print("result", result)
        if result["status"]:
            session.permanent = True  # this session will be exist for 5 days.
            session["username"] = user["username"]  # create a session for user.
            return redirect(url_for('index'))  # welcome page after login
        else:
            message = result["error"]
            return render_template('login.html', title='login', message=message)
    if "username" in session:  # if user already logged in
        if DEBUG:
            print("[STEP] Already logged in user!")
        return redirect(url_for('index'))
    return render_template('login.html', title='login')


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


@app.route('/technicality', methods=['GET', 'POST'])
def technicality():
    if "username" not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        abstract_db.add_document_annotation(username=session['username'], _id=session["_docID"], param=request.form.to_dict())
    _doc = abstract_db.get_document(session['username'])
    session["_docID"] = _doc["value"]['_id'].__str__()
    return render_template('technicality.html', title='Annotate Technicality', doc=_doc["value"])
