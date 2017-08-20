#! usr/bin/python
# coding=utf-8

from flask import Blueprint

main = Blueprint('main', __name__)

# 避免循环引入，特地放到最后import
from . import views, errors
