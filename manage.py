#! usr/bin/python
# coding=utf-8

from flask_script import Manager

from app.application import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
