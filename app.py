from flask import Flask
from dotenv import load_dotenv
from general.general import general
from auth.auth import auth
import os

from extentions import db, login_manager, bcrypt

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = 'dumb'
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    login_manager.login_view = "auth.login"
    app.register_blueprint(general)
    app.register_blueprint(auth)
    return app

