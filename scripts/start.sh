#!/usr/bin/env bash

source venv/bin/activate

nohup python3 manage.py runserver -p 50000 -h 0.0.0.0 &