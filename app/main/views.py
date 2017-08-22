#! usr/bin/python
# coding=utf-8

import os

from flask import render_template, flash, send_file, abort, redirect, url_for
from flask_login import login_required

from app.service import validate_upload, insert_resource, scan_resource, get_resource
from . import main
from ..forms import UploadForm


@main.route('/')
@login_required
def index():
    table = scan_resource()
    return render_template('main/index.html', table=table)


@main.route('/resource/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        validate_res = validate_upload(form)
        if validate_res.success:
            upload_res = insert_resource(form)
            flash(upload_res.message)
            return redirect(url_for('main.index'))
        else:
            flash(validate_res.message)
    return render_template('main/upload.html', form=form)


@main.route('/resource/download/<int:resource_id>', methods=['GET'])
@login_required
def download(resource_id: int):
    resource = get_resource(resource_id)
    path = resource.path
    if os.path.isfile(path):
        return send_file(path, attachment_filename=resource.origin_name)
    abort(404)


@main.route('/resource/edit/<int:resource_id>', methods=['GET'])
@login_required
def edit(resource_id: int):
    abort(404)


@main.route('/resource/delete/<int:resource_id>', methods=['GET'])
@login_required
def delete(resource_id: int):
    abort(404)
