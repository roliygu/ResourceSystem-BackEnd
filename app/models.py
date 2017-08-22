#! usr/bin/python
# coding=utf-8

import datetime

from . import db

DEFAULT_STRING_LENGTH = 256
DEFAULT_STRING_COL = db.String(DEFAULT_STRING_LENGTH)


def insert(item: db.Model, now=False):
    db.session.add(item)
    if now:
        db.session.commit()


class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    origin_name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    path = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    create_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now())
    update_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now())
    # todo 增加文件大小

    def get_by_id(self):
        Resource.query.filter_by(id=self.id).first()


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)


class ResourceTagRe(db.Model):
    __tablename__ = 'resource_tag_re'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    resource_id = db.Column(db.BigInteger, index=True)
    tag_id = db.Column(db.BigInteger, index=True)
