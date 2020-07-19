#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: importdata_demo.py
# @time: 2020/7/19 9:23 上午

# 使用excel中的数据去驱动 requests_utils

from common.testdata_utils import TestdataUtils
from common.requests_utils import RequestsUtils

all_case_info = TestdataUtils().def_testcase_data_list()
# case_info = all_case_info[2].get('case_info')

for case_info in all_case_info:
    RequestsUtils().request_by_step( case_info.get('case_info') )


