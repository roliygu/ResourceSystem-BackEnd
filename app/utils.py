#! usr/bin/python
# coding=utf-8

import random
import uuid

from flask import make_response
from werkzeug.datastructures import FileStorage

from .view_object import ValidateResult
from config import Config

config = Config.new_instance()


def get_config():
    return config


def generate_random_integer():
    return random.randint(0, 65535)


def warp_response(res: ValidateResult):
    response = make_response(res.message)
    if not res.success:
        response.status_code = 401
    return response


def get_mysql_url():
    return config.mysql_address


def save_file_storage(file_storage: FileStorage):
    path = "{}/{}_{}".format(config.upload_base_dir, uuid.uuid1(), file_storage.filename)
    file_storage.save(path)
    return path


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
