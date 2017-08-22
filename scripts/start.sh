#!/usr/bin/env bash

source venv/bin/activate

nohup python3 manage.py runserver -p 5000 &