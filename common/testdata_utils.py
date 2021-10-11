#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: testdata_utils.py
# @time: 2020/7/5 11:01 上午

import os
from common.excel_utils import ExcelUtils
from common import config
from common.localconfig_utils import local_config
from common.sql_utils import SqlUtils

current_path = os.path.dirname(__file__)
test_data_path = os.path.join( current_path,'..', local_config.CASE_DATA_PATH )

class TestdataUtils():
    def __init__(self,test_data_path = test_data_path):
        self.test_data_path = test_data_path
        self.test_data_sheet = ExcelUtils(test_data_path,"Sheet1")
        self.test_data = self.test_data_sheet.get_sheet_data_by_dict()
        self.test_data_by_mysql = SqlUtils().get_mysql_test_case_info()

    def __get_testcase_data_dict(self):
        testcase_dict = {}
        for row_data in self.test_data:
            if row_data['用例执行'] == '是':
                testcase_dict.setdefault( row_data['测试用例编号'],[] ).append( row_data )
        return testcase_dict

    def def_testcase_data_list(self):
        testcase_list = []
        for k,v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict["case_info"] = v
            testcase_list.append( one_case_dict )
        return tuple(testcase_list)

    def __get_testcase_data_dict_by_mysql(self):
        testcase_dict = {}
        for row_data in self.test_data_by_mysql:
            testcase_dict.setdefault( row_data['测试用例编号'],[] ).append( row_data )
        return testcase_dict

    def def_testcase_data_list_by_mysql(self):
        testcase_list = []
        for k,v in self.__get_testcase_data_dict_by_mysql().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict["case_info"] = v
            testcase_list.append( one_case_dict )
        return tuple(testcase_list)

    def get_row_num(self,case_id,case_step_name):
        for j in range(len(self.test_data)):
            if self.test_data[j]['测试用例编号'] == case_id and self.test_data[j]['测试用例步骤'] == case_step_name:
                break
        return j+1

    def get_result_id(self):
        for col_id in range(len(self.test_data_sheet.sheet.row(0))):
            if self.test_data_sheet.sheet.row(0)[col_id].value == '测试结果':
                break
        return col_id

    def write_result_to_excel(self,case_id,case_step_name,content="通过"):
        row_id = self.get_row_num(case_id,case_step_name)
        col_id = self.get_result_id
        self.test_data_sheet.update_excel_data(row_id,col_id,content)

    def clear_result_from_excel(self):
        # 方法思路是对的，但是xlutils不支持
        # row_count = self.test_data_sheet.get_row_count()
        # # self.test_data_sheet.update_excel_data(2, 14, "")
        # for row_id in range(1,row_count):  # 1--5
        #     self.test_data_sheet.update_excel_data( row_id,14,"")
        row_count = self.test_data_sheet.get_row_count()
        col_id = self.get_result_id
        self.test_data_sheet.clear_excel_column(1,row_count,col_id)







if __name__=="__main__":
    testdataUtils = TestdataUtils()
    testdataUtils.write_result_to_excel('case02','step_02')
    # for i in testdataUtils.def_testcase_data_list():
    #     print( i )
    # row = testdataUtils.get_row_num('case02','step_02')
    # print(row)
    # testdataUtils.write_result_to_excel('case03','step_02',"失败")


