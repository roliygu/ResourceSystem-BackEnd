#! usr/bin/python
# coding=utf-8

from config import Config
from app.vo.view_object import ValidateResult
from app.main.forms import LoginForm


def validate_user(form: LoginForm):
    config = Config()
    if form.username.data != config.username:
        return ValidateResult(False, "用户名错误")
    if form.password.data != config.password:
        return ValidateResult(False, "密码错误")
    return ValidateResult(True, "ok")


def main():
    pass


if __name__ == '__main__':
    main()
