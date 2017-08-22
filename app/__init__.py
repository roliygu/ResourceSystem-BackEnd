#! usr/bin/python
# coding=utf-8

import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, DEFAULTS, configure_uploads, patch_request_class
from flask_login import LoginManager

from app.utils import generate_random_integer, get_mysql_url
from config import Config

config = Config()

bootstrap = Bootstrap()
db = SQLAlchemy()

all_files = UploadSet('allfiles', DEFAULTS + ('pdf',))
max_file_size = int(config.max_file_size) * 1024 * 1024

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登录'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(generate_random_integer())
    app.config['SQLALCHEMY_DATABASE_URI'] = get_mysql_url()
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # bootstrap
    bootstrap.init_app(app)
    # db
    db.init_app(app)
    # upload
    app.config['UPLOADED_ALLFILES_DEST'] = os.getcwd()
    configure_uploads(app, all_files)
    patch_request_class(app, size=max_file_size)
    # login
    login_manager.init_app(app)
    # blueprint main
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # blueprint auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
