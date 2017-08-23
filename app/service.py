#! usr/bin/python
# coding=utf-8

from os.path import getsize
import datetime

from .forms import LoginForm, UploadForm, TagCreateForm
from .models import Resource, User, Tag, insert, delete, update
from .utils import save_file_storage, get_config
from .view_object import ValidateResult, UploadResult, TableCell, Table, ResourceHeader


def validate_user(form: LoginForm, user: User):
    if form.username.data != get_config().username:
        return ValidateResult(False, "用户名错误")
    if not user.verify_password(form.password.data):
        return ValidateResult(False, "密码错误")
    return ValidateResult(True, "ok")


def validate_upload(form: UploadForm):
    return ValidateResult(True, "ok")


def insert_resource(form: UploadForm):
    resource = Resource()
    resource.name = form.name.data
    tags = get_tags(form.tag.data)
    resource.tags = tags
    file_storage = form.binary.data
    resource.origin_name = file_storage.filename
    resource.path = save_file_storage(file_storage)
    resource.size = getsize(resource.path)
    insert(resource, now=False)
    return UploadResult(True, "[{}]上传成功".format(resource.name))


def insert_tag(form: TagCreateForm):
    tag = Tag()
    tag.name = form.name.data
    insert(tag, now=False)


def get_tags(tags: list):
    return Tag.get_by_ids(set([int(item) for item in tags]))


def delete_resource(resource: Resource):
    delete(resource)


def update_resource(resource: Resource):
    resource.update_time = datetime.datetime.now()
    update(resource)


def scan_resource():
    scan_res = Resource.query.limit(get_config().item_num_per_page)
    return build_resource_table(scan_res)


def build_resource_table(resource: list, in_resource=False):
    row_list = []
    for row in resource:
        col_list = [TableCell(row.name), TableCell(row.origin_name),
                    # TableCell(row.path),
                    TableCell(wrap_file_size(row.size)), TableCell(row.create_time), TableCell(row.update_time),
                    TableCell(build_option_html(row.id, in_resource))]
        row_list.append(col_list)
    return Table(ResourceHeader, row_list)


def scan_tag():
    return Tag.query.all()


def wrap_file_size(size: int):
    if size is None:
        return "-"
    if size > 1024 * 1024 * 1024:
        return "%.2f GB" % (size / (1024 * 1024 * 1024))
    elif size > 1024 * 1024:
        return "%.2f MB" % (size / (1024 * 1024))
    elif size > 1024:
        return "%.2f KB" % (size / 1024)
    else:
        return "%.2f B" % size


option_html_template = """
<a href=\"resource/download/{}\"><span class=\"glyphicon glyphicon-save\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"resource/delete/{}\"<span class=\"glyphicon glyphicon-remove\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"resource/edit/{}\"<span class=\"glyphicon glyphicon-edit\" aria-hidden=\"true\"></span></a>
"""

resource_option_html_template = """
<a href=\"download/{}\"><span class=\"glyphicon glyphicon-save\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"delete/{}\"<span class=\"glyphicon glyphicon-remove\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"edit/{}\"<span class=\"glyphicon glyphicon-edit\" aria-hidden=\"true\"></span></a>
"""


def build_option_html(resource_id, in_resource):
    if in_resource:
        return resource_option_html_template.format(resource_id, resource_id, resource_id)
    else:
        return option_html_template.format(resource_id, resource_id, resource_id)


def get_resource(resource_id: int):
    return Resource.query.filter_by(id=resource_id).first()


def get_tag(tag_id: int):
    return Tag.query.filter_by(id=tag_id).first()
