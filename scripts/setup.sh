#!/usr/bin/env bash
# 初始化开发和运行环境
sudo pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r resources/requirements.txt