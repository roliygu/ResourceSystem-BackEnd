#! usr/bin/python
# coding=utf-8

import os

from flask import render_template, flash, send_file, abort, redirect, url_for
from flask_login import login_required

from . import main
from ..service import ResourceService, TagService
from ..forms import UploadForm, ResourceEditForm, TagCreateForm, SearchForm

template_map = {
    "index": "main/index.html",
    "upload": "main/upload.html",
    "edit": "main/edit.html",
    "search": "main/search.html",
    "create_tag": "main/create_tag.html"
}


def redirect_index():
    return redirect(url_for('main.index'))


@main.route('/')
def index():
    resources = ResourceService.scan_resources()
    table = ResourceService.build_resource_table(resources)
    return render_template(template_map["index"], table=table)


@main.route('/resource/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    form.tag = TagService.map_scan_tag()
    if form.validate_on_submit():
        validate_res = ResourceService.validate_upload(form)
        if validate_res.success:
            upload_res = ResourceService.upload_resource(form)
            flash(upload_res.message)
            return redirect_index()
        else:
            flash(validate_res.message)
    return render_template(template_map["upload"], form=form)


@main.route('/resource/delete/<int:resource_id>', methods=['GET'])
@login_required
def delete(resource_id: int):
    resource = ResourceService.get_resource(resource_id)
    if resource:
        if os.path.exists(resource.path):
            os.remove(resource.path)
        ResourceService.delete_resource(resource)
    flash("删除成功")
    return redirect_index()


@main.route('/resource/edit/<int:resource_id>', methods=['GET', 'POST'])
@login_required
def edit(resource_id: int):
    form = ResourceEditForm()
    form.tag = TagService.map_scan_tag()
    if form.validate_on_submit():
        resource = ResourceService.get_resource(resource_id)
        if not resource:
            flash("找不到该资源")
            return redirect_index()
        ResourceService.update_resource(resource, form)
        flash("更新成功")
        return redirect_index()
    return render_template(template_map["edit"], form=form)


@main.route('/resource/download/<int:resource_id>', methods=['GET'])
@login_required
def download(resource_id: int):
    resource = ResourceService.get_resource(resource_id)
    path = resource.path
    if os.path.isfile(path):
        return send_file(path, attachment_filename=resource.origin_name)
    abort(404)


@main.route('/resource/search', methods=['GET', 'POST'])
@login_required
def search_resource():
    form = SearchForm()
    form.name = TagService.map_scan_tag()
    if form.validate_on_submit():
        tag = TagService.get_tag(int(form.name.data))
        resources = tag.resource.all()
        table = ResourceService.build_resource_table(resources, in_resource=True)
        return render_template(template_map["search"], table=table, form=form)
    return render_template(template_map["search"], form=form, table=ResourceService.build_resource_table([], in_resource=True))


@main.route('/tag/create', methods=['GET', 'POST'])
@login_required
def create_tag():
    form = TagCreateForm()
    if form.validate_on_submit():
        tag = TagService.get_tag(form.name.data)
        if tag:
            flash("标签已存在")
            return redirect_index()
        TagService.add_tag(form)
        flash("添加标签成功")
        return redirect_index()
    tag_names = [item.name for item in TagService.scan_tag()]
    return render_template(template_map["create_tag"], form=form, tag_names=tag_names)
