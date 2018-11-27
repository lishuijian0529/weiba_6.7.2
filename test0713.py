# -*- coding:utf-8 -*-
import threading
import os
from time import ctime,sleep
import requests
def run():
    while True:
        try:
            print requests.get('http://47.106.253.197:9600/wxapi/cust/replySM?cpid=dzbdwer&telephone=13764541234&replyInfo=YZ&replyPort=1065982340923').text
        except:pass
for i in range(0,100):
    threading.Thread(target=run, args=()).start()

