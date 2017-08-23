#! usr/bin/python
# coding=utf-8

import datetime

from werkzeug.security import check_password_hash
from flask_login import UserMixin

from . import db, login_manager
from .utils import get_config

DEFAULT_STRING_LENGTH = 128
DEFAULT_STRING_COL = db.String(DEFAULT_STRING_LENGTH)


def insert(item: db.Model, now=False):
    db.session.add(item)
    if now:
        db.session.commit()


def delete(item: db.Model, now=False):
    db.session.delete(item)
    if now:
        db.session.commit()


def update(item: db.Model, now=False):
    db.session.add(item)
    if now:
        db.session.commit()


resource_tag_re = db.Table('resource_tag_re',
                           db.Column('resource_id', db.BigInteger, db.ForeignKey('resource.id')),
                           db.Column('tag_id', db.BigInteger, db.ForeignKey('tag.id'))
                           )


class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    origin_name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    path = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    size = db.Column(db.BigInteger)
    create_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now())
    update_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now())
    tags = db.relationship('Tag', secondary=resource_tag_re, backref=db.backref('resource', lazy='dynamic'),
                           lazy='dynamic')

    def get_by_id(self):
        Resource.query.filter_by(id=self.id).first()


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False, unique=True)
    create_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now())
    update_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now())


class User(UserMixin):
    def __init__(self, name, password_hash):
        self.id = 1
        self.name = name
        self.password_hash = password_hash

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(id: int):
    return User(get_config().username, get_config().password_hash)
