#! usr/bin/python
# coding=utf-8

from flask import Blueprint

main = Blueprint('main', __name__)

# 避免循环引入，特地放到最后import; model和view都需要引入，分别用来绑定数据库和路由
from .views import *
from ..models import *
