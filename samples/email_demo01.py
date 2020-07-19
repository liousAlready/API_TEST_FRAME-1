#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: email_demo01.py
# @time: 2020/7/19 3:03 下午

import smtplib
from email.mime.text import MIMEText

body_str = '''
<h3 align="center">自动化测试报告</h3>
<table border="2" align="center" width="50%",height="400">
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
</table>
'''
# msg = MIMEText('hello,P1P2','plain','utf-8')
msg = MIMEText(body_str,'html','utf-8')
msg['from'] = "329999897@qq.com"
msg['to'] = "329999897@qq.com"
msg['Cc'] = '1053300691@qq.com'
msg['subject'] = 'P1P2自动化测试框架学习'

smtp = smtplib.SMTP()
smtp.connect( "smtp.qq.com" )
smtp.login( user="329999897@qq.com" ,password='wvcsgattkyqqbhah' )
smtp.sendmail( "329999897@qq.com",["329999897@qq.com",'1053300691@qq.com'],msg.as_string() )

