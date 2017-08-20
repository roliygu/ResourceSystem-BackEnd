#! usr/bin/python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ValidateResult:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = StringField('密码', validators=[DataRequired()])
    submit = SubmitField('确定')


def main():
    pass


if __name__ == '__main__':
    main()
