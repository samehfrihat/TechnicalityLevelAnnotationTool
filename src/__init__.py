from datetime import timedelta

from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder="static/templates", static_folder="static")
CORS(app)

app.config['SECRET_KEY'] = 'ThisIsTopSecretKey'
app.permanent_session_lifetime = timedelta(days=5)  # session stays for 5 days

from src import views