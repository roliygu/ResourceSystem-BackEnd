#! usr/bin/python
# coding=utf-8

from . import db


class Resource(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String, index=True, nullable=False)
    binary = db.Column(db.LargeBinary)
    create_time = db.Column(db.Time)
    update_time = db.Column(db.Time)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String, index=True, nullable=False)


class ResourceTagRe(db.Model):
    __tablename__ = 'resource_tag_re'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    resource_id = db.Column(db.BigInteger, index=True)
    tag_id = db.Column(db.BigInteger, index=True)
