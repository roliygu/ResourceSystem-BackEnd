#! usr/bin/python
# coding=utf-8

from flask import redirect, url_for, render_template, flash, request
from flask_login import login_user, logout_user

from . import auth
from ..forms import LoginForm
from ..service import validate_user
from ..models import load_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = load_user(1)
        validate_res = validate_user(form, user)
        if validate_res.success:
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash(validate_res.message)
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash("退出登录成功")
    return redirect(url_for('main.index'))
