# -*- coding:utf-8 -*-
import re
from appium import webdriver
import os
import time

class Open():
    try:
        def Phone(self ,appPackage,appActivity,deviceid,port):
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 设备系统
            desired_caps['automationName'] = 'UiAutomator2'
            desired_caps['platformVersion'] = '8.0.0'  # 设备系统版本
            #desired_caps['platformVersion'] = os.popen('adb -s %s shell getprop ro.build.version.release' % deviceid).readlines()  # 设备系统版本
            desired_caps['deviceName'] = deviceid # 设备名称
            desired_caps['appPackage'] = appPackage
            desired_caps['appActivity'] = appActivity
            desired_caps['udid'] = deviceid
            desired_caps['unicodeKeyboard'] = "True"
            desired_caps['resetKeyboard'] = "True"
            driver = webdriver.Remote('http://localhost:'+port+'/wd/hub',desired_caps)
            return driver
    except :
        pass

if __name__ == '__main__':
    decice = '53476787'
    old_list = []
    #os.system('adb shell am start -n com.dobe.sandbox/.home.Main2Activity')
    driver = Open().Phone('com.dobe.sandbox','.home.Main2Activity', decice, '4713')
    driver.implicitly_wait(50)
    driver.find_element_by_id('com.dobe.sandbox:id/download_device').click()
    driver.find_element_by_name('修改设备').click()
    driver.find_element_by_name('修改机型').click()
    time.sleep(2)
    if driver.find_elements_by_class_name('android.widget.TextView') != []:
        list = driver.find_elements_by_class_name('android.widget.TextView')
        IMEI = re.findall('IMEI: (.*)',list[2].get_attribute(("text")))[0]
        MAC = re.findall('MAC: (.*)',list[5].get_attribute(("text")))[0]
        Brand = re.findall('BRAND: (.*)',list[6].get_attribute(("text")))[0]








