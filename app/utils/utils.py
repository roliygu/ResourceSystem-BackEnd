#! usr/bin/python
# coding=utf-8

import random
import uuid

from flask import make_response
from werkzeug.datastructures import FileStorage

from app.vo.view_object import ValidateResult
from config import Config

config = Config()


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
