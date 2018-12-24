#-*- coding:utf-8 -*-
import ConfigParser
import sys
import os
import urllib2
import json


appId=""
appSecret=""
accessToken=""
codeSize=430
wordsDict={}
wordsList=[]
typeList={}

def getAccessToken():
    global appId
    global appSecret
    global accessToken

    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+appId+"&secret="+ appSecret
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = json.loads(res_data.read())
    accessToken = res['access_token']

def queryQRCode(chanel,param):
    global accessToken
    global codeSize
	
    data = {'scene': param,'width':codeSize}
    jdata = json.dumps(data,ensure_ascii=False)
    requrl = "https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token="+accessToken
    req = urllib2.Request(requrl, jdata)
    res_data = urllib2.urlopen(req)
    content = res_data.read()
    if (type(content) =='dict'):
        print(chanel + " make fail")
    else:
         f = open(chanel+".png",'wb')
         f.write(content)
         f.close()

def mkQRCode():
    global appId
    global appSecret
    global wordsList
    global typeList
    global codeSize
    print "=========WECHAT QRCode Maker======"
    print "qq: 1553517982"
    print "=================================="
    conf = ConfigParser.ConfigParser()
    conf.read("config.ini")
    appId = conf.get("appConfig","appId")
    appSecret = conf.get("appConfig", "appSecret")
    codeSize = conf.get("appConfig", "size")

    getAccessToken()
    
    if (conf.has_section('launchParam')):
        checkDirs = conf.items("launchParam")
        for pairs in checkDirs:
            queryQRCode(pairs[0],pairs[1])

mkQRCode()
os.system("pause")
