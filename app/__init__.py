# app/_init_.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
#from passlib.hash import sha256_crypt

# from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.login_user'
login_manager.session_protection = 'strong'
#sha256_crypt_1 = sha256_crypt()


def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    # login_manager.login_view=app
    # bcrypt_1.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
