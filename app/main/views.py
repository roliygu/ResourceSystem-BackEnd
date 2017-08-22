#! usr/bin/python
# coding=utf-8

import os

from flask import render_template, flash, send_file, abort, redirect, url_for
from flask_login import login_required

from app.service import validate_upload, insert_resource, scan_resource, get_resource, delete_resource, update_resource
from . import main
from ..forms import UploadForm, ResourceEditForm


def redirect_index():
    return redirect(url_for('main.index'))


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
            return redirect_index()
        else:
            flash(validate_res.message)
    return render_template('main/upload.html', form=form)


@main.route('/resource/edit/<int:resource_id>', methods=['GET', 'POST'])
@login_required
def edit(resource_id: int):
    form = ResourceEditForm()
    if form.validate_on_submit():
        resource = get_resource(resource_id)
        if resource:
            resource.name = form.name.data
            update_resource(resource)
            flash("更新成功")
            return redirect_index()
        flash("找不到资源")
        return redirect_index()
    return render_template('main/edit.html', form=form)


@main.route('/resource/download/<int:resource_id>', methods=['GET'])
@login_required
def download(resource_id: int):
    resource = get_resource(resource_id)
    path = resource.path
    if os.path.isfile(path):
        return send_file(path, attachment_filename=resource.origin_name)
    abort(404)


@main.route('/resource/delete/<int:resource_id>', methods=['GET'])
@login_required
def delete(resource_id: int):
    msg = "删除成功"
    resource = get_resource(resource_id)
    if resource:
        if os.path.exists(resource.path):
            os.remove(resource.path)
        delete_resource(resource)
    flash(msg)
    return redirect_index()
