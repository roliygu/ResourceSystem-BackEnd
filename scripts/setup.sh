#!/usr/bin/env bash
# 初始化开发和运行环境
sudo pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install flask==0.12.2
pip3 install flask-wtf==0.14.2
pip3 install flask-script==2.0.5
pip3 install flask-bootstrap==3.3.7.1
pip3 install flask-sqlalchemy==1.1.13