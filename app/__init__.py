#! usr/bin/python
# coding=utf-8

import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, DEFAULTS, configure_uploads, patch_request_class

from app.utils.utils import generate_random_integer, get_mysql_url

bootstrap = Bootstrap()
db = SQLAlchemy()
all_files = UploadSet('allfiles', DEFAULTS + ('pdf',))
mb256 = 256 * 1024 * 1024


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
    patch_request_class(app, size=mb256)
    # blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
