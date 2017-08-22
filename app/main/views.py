#! usr/bin/python
# coding=utf-8

import os

from flask import render_template, flash, send_file, abort, redirect, url_for
from flask_login import login_required

from app.service import validate_upload, insert_resource, scan_resource, scan_tag, get_resource, delete_resource, update_resource, get_tag, insert_tag
from . import main
from ..forms import UploadForm, ResourceEditForm, TagCreateForm


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


@main.route('/resource/edit/<int:resource_id>', methods=['GET', 'POST'])
@login_required
def edit(resource_id: int):
    form = ResourceEditForm()
    if form.validate_on_submit():
        resource = get_resource(resource_id)
        if not resource:
            flash("找不到该资源")
            return redirect_index()
        resource.name = form.name.data
        update_resource(resource)
        flash("更新成功")
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


@main.route('/tag/create', methods=['GET', 'POST'])
@login_required
def create_tag():
    form = TagCreateForm()
    if form.validate_on_submit():
        tag = get_tag(form.name.data)
        if tag:
            flash("标签已存在")
            return redirect_index()
        insert_tag(form)
        flash("添加标签成功")
        return redirect_index()
    tag_names = scan_tag()
    return render_template('main/create_tag.html', form=form, tag_names=tag_names)
