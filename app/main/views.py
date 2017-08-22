#! usr/bin/python
# coding=utf-8

import os

from flask import session, redirect, url_for, render_template, flash, send_file, abort

from . import main
from .forms import LoginForm, UploadForm
from app.service.service import validate_user, validate_upload, insert_resource, scan_resource, get_resource
from app.utils.utils import generate_random_integer


def render_index():
    table = scan_resource()
    return render_template('index.html', table=table)


@main.route('/')
def index():
    if "token" not in session:
        return redirect(url_for('main.login'))
    else:
        return render_index()


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


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        validate_res = validate_upload(form)
        if validate_res.success:
            upload_res = insert_resource(form)
            flash(upload_res.message)
            return render_index()
        else:
            flash(validate_res.message)
    return render_template('upload.html', form=form)


@main.route('/download/<int:resource_id>', methods=['GET'])
def download(resource_id: int):
    resource = get_resource(resource_id)
    path = resource.path
    if os.path.isfile(path):
        return send_file(path, attachment_filename=resource.origin_name)
    abort(404)
