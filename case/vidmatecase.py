#coding=utf-8

import time
import unittest
import sys  
sys.path.append('/Users/Shared/Jenkins/Home/workspace/Test_vidmate/default/android/Vidmate/common')

from appium import webdriver
import config
import AppiumApi


def testcase_one(self):

    self.driver.find_element_by_id('com.nemo.vidmate:id/btnOK').click()
    el=self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Video")')
    el.click()
