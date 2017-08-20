#! usr/bin/python
# coding=utf-8

from flask import session, redirect, url_for, render_template, flash

from . import main
from .forms import LoginForm
from app.service.user_service import validate_user
from app.utils.utils import generate_random_integer


@main.route('/')
def index():
    if "token" not in session:
        return redirect(url_for('main.login'))
    else:
        return "hello"


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        validate_res = validate_user(form)
        if validate_res.success:
            session["token"] = generate_random_integer()
            return redirect(url_for('main.index'))
        else:
            flash(validate_res.message)
    return render_template('login.html', form=form)
