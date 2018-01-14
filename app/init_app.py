from flask_sqlalchemy import SQLAlchemy
from flask import Flask


def init_app():
    app = Flask(__name__)
    return app
