#! usr/bin/python
# coding=utf-8

from . import db

DEFAULT_STRING_LENGTH = 256
DEFAULT_STRING_COL = db.String(DEFAULT_STRING_LENGTH)


class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    origin_name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    path = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)
    create_time = db.Column(db.TIMESTAMP)
    update_time = db.Column(db.TIMESTAMP)

    def insert(self):
        db.session.add(self)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(DEFAULT_STRING_COL, index=True, nullable=False)

    def insert(self):
        db.session.add(self)


class ResourceTagRe(db.Model):
    __tablename__ = 'resource_tag_re'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    resource_id = db.Column(db.BigInteger, index=True)
    tag_id = db.Column(db.BigInteger, index=True)

    def insert(self):
        db.session.add(self)
