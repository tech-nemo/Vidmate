#coding=utf-8

import time
import unittest
import sys  
sys.path.append('/Users/Shared/Jenkins/Home/workspace/Test_vidmate/default/android/Vidmate/common')
sys.path.append('/Users/Shared/Jenkins/Home/workspace/Test_vidmate/default/android/Vidmate/case')

from appium import webdriver
import vidmatecase
import config
import AppiumApi

class TestVidmate(unittest.TestCase):
    def setUp(self):

       
        time.sleep(6)
        desired_caps = {}
        desired_caps['platformName'] = config.platformName
        desired_caps['platformVersion'] = config.platformVersion
        desired_caps['deviceName'] = config.deviceName
        # desired_caps['app'] = app
        # 如果设置的是app包的路径，则不需要配appPackage和appActivity
        desired_caps['appPackage'] = config.appPackage
        desired_caps['appActivity'] = config.appActivity
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)

        # AppiumApi.install_app(self.driver, config.app)

    
    def testcase(self):
        vidmatecase.testcase_one(self)

        
    def tearDown(self):

        print("执行脚本完毕！")
        self.driver.quit()
