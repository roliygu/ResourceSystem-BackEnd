#! usr/bin/python
# coding=utf-8

from flask import Flask, session, redirect, url_for, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from app.utils.utils import generate_random_integer, get_mysql_url
from app.service.user_service import validate_user
from app.vo.view_object import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = str(generate_random_integer())
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = get_mysql_url()
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


@app.route('/')
def index():
    if "token" not in session:
        return redirect(url_for('login'))
    else:
        return "hello"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        validate_res = validate_user(form)
        if validate_res.success:
            session["token"] = generate_random_integer()
            return redirect(url_for('index'))
        else:
            flash(validate_res.message)
    return render_template('login.html', form=form)


class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String, index=True, nullable=False)
    binary = db.Column(db.LargeBinary)
    create_time = db.Column(db.Time)
    update_time = db.Column(db.Time)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String, index=True, nullable=False)


class ResourceTagRe(db.Model):
    __tablename__ = 'resource_tag_re'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    resource_id = db.Column(db.BigInteger, index=True)
    tag_id = db.Column(db.BigInteger, index=True)
