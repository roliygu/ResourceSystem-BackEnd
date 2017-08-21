#! usr/bin/python
# coding=utf-8

import configparser

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("%s/resources/config.cfg" % dir_path)
        self.username = config["user"]["username"]
        self.password = config["user"]["password"]
        self.mysql_address = config["mysql"]["url"]
        self.upload_base_dir = config["storage"]["base_dir"]


if __name__ == '__main__':
    conf = Config()
    print(conf.password)
