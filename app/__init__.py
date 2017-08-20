#! usr/bin/python
# coding=utf-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from app.utils.utils import generate_random_integer, get_mysql_url

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(generate_random_integer())
    app.config['SQLALCHEMY_DATABASE_URI'] = get_mysql_url()
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    #
    bootstrap.init_app(app)
    #
    db.init_app(app)
    #
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
