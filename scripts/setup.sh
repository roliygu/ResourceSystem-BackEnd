#!/usr/bin/env bash
# 初始化开发和运行环境
sudo pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install flask==0.12.2