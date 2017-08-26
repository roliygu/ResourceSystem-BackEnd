#! usr/bin/python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('确定')


class UploadForm(FlaskForm):
    name = StringField('资源名', validators=[DataRequired()])
    tag = SelectMultipleField('标签', validators=[DataRequired()])
    binary = FileField('文件', validators=[DataRequired()])
    submit = SubmitField('确定')


class ResourceEditForm(FlaskForm):
    name = StringField('资源名', validators=[DataRequired()])
    tag = SelectMultipleField('标签', validators=[DataRequired()])
    submit = SubmitField('确定')


class TagCreateForm(FlaskForm):
    name = StringField('标签名称', validators=[DataRequired()])
    submit = SubmitField('确定')


class SearchForm(FlaskForm):
    method = SelectField('查询方式', validators=[DataRequired()])
    name = StringField('输入', validators=[DataRequired()])
    submit = SubmitField('确定')

