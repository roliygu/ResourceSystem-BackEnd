#!/usr/bin/env bash
rm resources/requirements.txt
source venv/bin/activate
pip3 freeze > resources/requirements.txt