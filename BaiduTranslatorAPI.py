# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:15:48 2020

@author: a8275
"""

import requests
import json
import urllib.request
import ssl
import random
import hashlib


def getStrAsMD5(parmStr):
    if isinstance(parmStr,str):
        # 如果是unicode先转utf-8
        parmStr=parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()

def BaiduTranslator(a):
    url='https://fanyi-api.baidu.com/api/trans/vip/translate'
    salt=str(random.randint(0,10))
    appid='20201101000605342'
    password='O4tx_UwAEG0J0BrChe_X'
    sign=getStrAsMD5(appid+a+salt+password)
    parmas={'q':a,'from':'en','to':'zh','appid':appid,'salt':salt,'sign':sign}
    r=requests.get(url,parmas)
    r.json()
    try:
        return r.json()['trans_result'][0]['dst']
    except KeyError:
        return -1


    
    
    
    