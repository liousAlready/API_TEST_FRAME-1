#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: data_demo.py
# @time: 2020/7/26 10:57 上午

from faker import Faker

f=Faker(locale='zh_CN') # 为生成数据的文化选项，默认为en_US，只有使用了相关文化，才能生成相对应的随机信息

for i in range(10):
    print( f.name() + " : " + f.ssn() )  # 随机生成中文姓名和地址