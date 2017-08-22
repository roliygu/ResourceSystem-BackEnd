#! usr/bin/python
# coding=utf-8


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('确定')


class UploadForm(FlaskForm):
    name = StringField('资源名', validators=[DataRequired()])
    binary = FileField('文件', validators=[DataRequired()])
    submit = SubmitField('确定')


class ResourceEditForm(FlaskForm):
    name = StringField('资源名', validators=[DataRequired()])
    submit = SubmitField('确定')
