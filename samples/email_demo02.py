#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: email_demo01.py
# @time: 2020/7/19 3:03 下午
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg.attach( MIMEText('<h3 align="center">自动化测试报告</h3>','html','utf-8') )
msg['from'] = "329999897@qq.com"
msg['to'] = "329999897@qq.com"
msg['Cc'] = '1053300691@qq.com'
msg['subject'] = 'P1P2自动化测试框架学习'

html_path = os.path.dirname(__file__)+'/../test_reports/P1P2接口自动化测试报告V1.4/P1P2接口自动化测试报告V1.4.html'
print( os.path.basename(html_path) )

attach_file = MIMEText( open(html_path,'rb').read() ,'base64','utf-8' )
attach_file['Content-Type'] = 'application/octet-stream'
attach_file.add_header('Content-Disposition', 'attachment', filename=('gbk', '', 'P1P2接口自动化测试报告V1.4.html'))
# attach_file['Content-Disposition'] = 'attachment; filename="report.html"'
msg.attach( attach_file )

smtp = smtplib.SMTP()
smtp.connect( "smtp.qq.com" )
smtp.login( user="329999897@qq.com" ,password='wvcsgattkyqqbhah' )
smtp.sendmail( "329999897@qq.com",["329999897@qq.com",'1053300691@qq.com'],msg.as_string() )

