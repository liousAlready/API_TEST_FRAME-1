#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: config_utils.py
# @time: 2020/7/5 11:49 上午

import configparser


class ConfigUtils():
    def __init__(self, config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path,encoding="utf-8")

    def read_value(self, section, key):
        value = self.cfg.get(section, key)
        return value
