#coding=utf-8

from appium import webdriver
import sys  
sys.path.append('/Users/Shared/Jenkins/Home/workspace/Test_vidmate/default/android/Vidmate/common')
sys.path.append('/Users/Shared/Jenkins/Home/workspace/Test_vidmate/default/android/Vidmate/case')


import AppiumApi
import emailto
from MakeCase import TestVidmate
import unittest
import os
import time
import HTMLTestRunnerCN
import datetime
import argparse





if __name__ == '__main__':

    TODAY = datetime.date.today()
    CURRENTDAY = TODAY.strftime('%Y-%m-%d')
    # os.system('StartAppium.bat') #启动appium服务
    time.sleep(3)
    
    suite = unittest.TestSuite()
    suite.addTest(TestVidmate('testcase'))
    filename = '/Users/Shared/Jenkins/Home/workspace/Test_vidmate/default/android/vidmate/Appium_android/result/%s vidmate.html'%CURRENTDAY 
    fb = open(filename, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fb, title='Report', description='此邮件自动发送，请勿回复！')
    result=runner.run(suite)
    fb.close()

    # 发送邮件

    if result.failure_count>0 & result.error_count>0:
        Status='- Failed'
    else:
        Status='- Passed'
        
    reuslt_file = open(filename)
    result_data = reuslt_file.read()
    emailto.Send_Mail(result_data, filename, Status)
    

    # os.system('CloseAppium.bat') #关闭appium服务
