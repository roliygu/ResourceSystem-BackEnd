#! usr/bin/python
# coding=utf-8

from flask_script import Manager

from app import create_app, db

app = create_app()

manager = Manager(app)


@manager.command
def init_db():
    db.create_all()


@manager.command
def reset_db():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()
