#! usr/bin/python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = StringField('密码', validators=[DataRequired()])
    submit = SubmitField('确定')
