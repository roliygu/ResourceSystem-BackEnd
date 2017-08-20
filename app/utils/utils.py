#! usr/bin/python
# coding=utf-8

import random

from flask import make_response

from app.vo.view_object import ValidateResult


def generate_random_integer():
    return random.randint(0, 65535)


def warp_response(res: ValidateResult):
    response = make_response(res.message)
    if not res.success:
        response.status_code = 401
    return response


def main():
    pass


if __name__ == '__main__':
    main()
