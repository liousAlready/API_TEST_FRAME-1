#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: mysql_demo.py
# @time: 2020/7/19 5:20 下午

import pymysql

connect = pymysql.connect(host='127.0.0.1',
                          port=3306,
                          user='root',
                          password='123456',
                          database='api_test',
                          charset='utf8')
cur = connect.cursor( cursor=pymysql.cursors.DictCursor )
sql_str = '''
select case_info.case_id as '测试用例编号',case_info.case_name as '测试用例名称',case_step_info.case_step_name,api_info.api_name,api_info.api_request_type,api_info.api_request_url,api_info.api_url_params,api_post_data,case_step_info.get_value_type,case_step_info.variable_name,case_step_info.get_value_code,case_step_info.excepted_result_type,case_step_info.excepted_result
from case_step_info 
LEFT JOIN case_info on case_step_info.case_id = case_info.case_id
LEFT JOIN api_info on case_step_info.api_id = api_info.api_id 
where case_info.is_run = 1
order by case_info.case_id,case_step_info.case_step_name;
'''
cur.execute( sql_str )
for test_step in cur.fetchall():
    print(test_step)
# print( cur.fetchone() )