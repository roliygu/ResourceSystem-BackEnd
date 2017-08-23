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
def drop_db():
    db.drop_all()


@manager.command
def run():
    app.run(host='0.0.0.0', port=50000)


@manager.command
def generate_password_hash():
    from werkzeug.security import generate_password_hash
    print(generate_password_hash("aa"))


@manager.command
def profile(length=25, profile_dir='./'):
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length], profile_dir=profile_dir)
    app.run(host='0.0.0.0', port=50000)


@manager.command
def debug():
    app.run(host='0.0.0.0', port=50000, debug=True)


if __name__ == '__main__':
    manager.run()
