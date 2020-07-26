#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: log_demo_nb.py
# @time: 2020/7/26 11:18 上午

import os
from nb_log import LogManager

# l_path = os.path.join( os.path.dirname(__file__),'pythonlogs')
# print( l_path )

logger = LogManager('newdream').get_logger_and_add_handlers(log_filename='ApiTest.log')
print('hello')
logger.info('你好！')
logger.warning('警告！！')
logger.error('这是错误日志')

