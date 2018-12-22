#-*- coding:utf-8 -*-
import ConfigParser
import sys
import os
import urllib2
import json

appId=""
appSecret=""
accessToken=""

def getAccessToken():
    global appId
    global appSecret
    global accessToken

    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+appId+"&secret="+ appSecret
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = json.loads(res_data.read())
    accessToken = res['access_token']

def checkMsgContent(msg):
    global accessToken
    data = {'content': msg}
    jdata = json.dumps(data,ensure_ascii=False)
    requrl = "https://api.weixin.qq.com/wxa/msg_sec_check?access_token="+accessToken
    req = urllib2.Request(requrl, jdata)
    res_data = urllib2.urlopen(req)
    res = json.loads(res_data.read())
    if(res["errcode"] != 0):
        print msg.decode("utf-8").encode("gbk")

def checkWords():
    global appId
    global appSecret
    reload(sys)
    sys.setdefaultencoding('utf8')
    conf = ConfigParser.ConfigParser()
    conf.read("config.ini")
    appId = conf.get("appConfig","appId")
    appSecret = conf.get("appConfig", "appSecret")

    getAccessToken()

    items = conf.items("words")
    if (len(items)>0):
            for item in items:
                checkMsgContent(item[1])
    os.system("pause")

checkWords()
