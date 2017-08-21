#! usr/bin/python
# coding=utf-8

import datetime

from config import Config
from app.vo.view_object import ValidateResult, UploadResult, TableCell, Table, ResourceHeader
from app.main.forms import LoginForm, UploadForm
from app.models import Resource
from app.utils.utils import save_file_storage


def validate_user(form: LoginForm):
    config = Config()
    if form.username.data != config.username:
        return ValidateResult(False, "用户名错误")
    if form.password.data != config.password:
        return ValidateResult(False, "密码错误")
    return ValidateResult(True, "ok")


def validate_upload(form: UploadForm):
    return ValidateResult(True, "ok")


def insert_resource(form: UploadForm):
    resource = Resource()
    resource.name = form.name.data
    file_storage = form.binary.data
    resource.origin_name = file_storage.filename
    resource.path = save_file_storage(file_storage)
    resource.create_time = datetime.datetime.now()
    resource.update_time = datetime.datetime.now()
    resource.insert()
    return UploadResult(True, "[{}]上传成功".format(resource.name))


def scan_resource():
    scan_res = Resource.query.limit(20)
    row_list = []
    for row in scan_res:
        col_list = [TableCell(row.name), TableCell(row.origin_name), TableCell(row.path),
                    TableCell(row.create_time), TableCell(row.update_time)]
        row_list.append(col_list)
    return Table(ResourceHeader, row_list)
