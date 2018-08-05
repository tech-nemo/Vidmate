# -*- coding: utf-8 -*

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import datetime
import time, os, sys,json,requests

# 第三方 SMTP 服务

def Send_Mail(Message, path, Status):
    mail_host="smtp.126.com"  #设置服务器
    mail_user="tech_nemo@126.com"   #用户名
    mail_pass="nemo123"   #密码
    sender = 'tech_nemo@126.com'
    receivers = 'chenhq@nemo-inc.com'  # 接收邮件
    message = MIMEMultipart()
    message['From'] = 'tech_nemo@126.com'
    message['To'] = 'chenhq@nemo-inc.com'
    subject = 'Vidmate自动化测试结果'+Status
    message['Subject'] = Header(subject, 'utf-8')
    TODAY = datetime.date.today()
    CURRENTDAY = TODAY.strftime('%Y-%m-%d')
    att = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')  # 设置附件的目录
    att['content-type'] = 'application/octet-stream'
    att['content-disposition'] = 'attachment;filename="%s result.html"'%CURRENTDAY  # 设置附件的名称
    content = str(Message)
    message.attach(att)
    body = MIMEText(content, 'html', 'utf-8')  # 设置字符编码
    message.attach(body)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功！")
    except Exception as e:
        print ("邮件发送失败！")
        print (e)

