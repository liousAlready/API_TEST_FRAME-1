#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: xlutils_demo.py
# @time: 2020/7/22 8:58 下午

import os
import xlrd
from xlutils.copy import copy

excel_path = os.path.join( os.path.dirname(__file__) , 'data/test_data.xls' )
wb = xlrd.open_workbook( excel_path,formatting_info=True)  # 创建工作薄对象 xlrd模块2007 2003

# sheet = wb.sheet_by_name('Sheet1')
# sheet = wb.sheet_by_index(0)
# print( sheet.cell_value(0,0) )

new_workbook = copy(wb)  #  new_workbook 已经变成可写的对象 xlwt 对象
sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))     #sheet_by_name('Sheet1')
sheet.write(2,3,60)
new_workbook.save(excel_path)