#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: xlutils_demo.py
# @time: 2020/7/22 8:58 下午

import os
import xlrd
from xlutils.copy import copy
from common.localconfig_utils import local_config

excel_path = os.path.join( os.path.dirname(__file__) , '..',local_config.CASE_DATA_PATH )
wb = xlrd.open_workbook( excel_path,formatting_info=True)  # 创建工作薄对象 xlrd模块2007 2003

# 思路一：
# for i in range(1,6):
#     new_workbook = copy(wb)  #  new_workbook 已经变成可写的对象 xlwt 对象
#     sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))     #sheet_by_name('Sheet1')
#     sheet.write(i,14,"")
#     new_workbook.save(excel_path)

# 思路二：
new_workbook = copy(wb)  #  new_workbook 已经变成可写的对象 xlwt 对象
sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))
for i in range(1,6):
    sheet.write(i, 14, "")
new_workbook.save(excel_path)
