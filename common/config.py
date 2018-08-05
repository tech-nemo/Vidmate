#coding=utf-8

import  os




PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# the config of app
platformName = 'Android'
platformVersion= '5.1'
deviceName = 'CYSBBDE750530130'
app = PATH('./app/yymobile_client-7.5.2-SNAPSHOT-58674-official.apk')
appPackage = 'com.nemo.vidmate'
appActivity= 'com.nemo.vidmate.MainActivity'
