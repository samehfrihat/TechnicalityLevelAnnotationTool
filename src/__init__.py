from datetime import timedelta

from flask import Flask, request
from flask_babel import Babel, gettext
from flask_cors import CORS
from flask_fontawesome import FontAwesome

app = Flask(__name__, template_folder="static/templates", static_folder="static")

babel = Babel(app)
fa = FontAwesome(app)
CORS(app)

app.config['SECRET_KEY'] = 'ThisIsTopSecretKey'
app.permanent_session_lifetime = timedelta(days=5)  # session stays for 5 days


@babel.localeselector
def get_locale():
    translations = [str(translation) for translation in babel.list_translations()]
    return request.accept_languages.best_match(translations)


from src import views
