#-*- coding:utf-8 -*-
import ConfigParser
import threading
import sys
import os
from time import ctime,sleep
import urllib2
import json
import re


appId=""
appSecret=""
accessToken=""
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

def checkMsgContent(msg):
    global accessToken
    data = {'content': msg}
    jdata = json.dumps(data,ensure_ascii=False)
    requrl = "https://api.weixin.qq.com/wxa/msg_sec_check?access_token="+accessToken
    req = urllib2.Request(requrl, jdata)
    res_data = urllib2.urlopen(req)
    res = json.loads(res_data.read())
    if (res["errcode"] != 0):
        if(res["errcode"] == 87014):
            print msg.decode("utf-8").encode("gbk")
        else:
            print res["errcode"]


def findAllWords(filePath):
    global typeList
    fileName, fileType = os.path.splitext(filePath)
    kind = fileType.replace('.','')
    if not typeList.has_key(kind):
        return
    
    f = open(filePath, "r")
    lines = f.readlines()
    f.close()
    length = len(lines)

    if length == 0:
        return
    global wordsList
    zhPattern = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5]+')
    for line in lines:
            line = unicode(line, 'utf-8')
            results = re.findall(zhPattern, line)
            for str in results:
                if not wordsDict.has_key(str):
                    wordsDict.setdefault(str,str)
                    wordsList.append(str.encode('utf-8'))


def findDirAllWords(path):
    global wordsList
    for file in os.listdir(path):
        filepath = path + "//" + file
        if os.path.isdir(filepath):
            findDirAllWords(filepath)
        elif os.path.isfile(filepath):
            findAllWords(filepath)


def checkWords():
    global appId
    global appSecret
    global wordsList
    global typeList
    reload(sys)
    sys.setdefaultencoding('utf8')
    conf = ConfigParser.ConfigParser()
    conf.read("config.ini")
    appId = conf.get("appConfig","appId")
    appSecret = conf.get("appConfig", "appSecret")
    #files need check
    if (conf.has_section('checkType')):
        checkTypes = conf.items("checkType")
        for pairs in checkTypes:
            if not typeList.has_key(pairs[1]):
                typeList.setdefault(pairs[1],pairs[1])

    #get all words
    packFolders=[]
    if (conf.has_section('checkDir')):
        checkDirs = conf.items("checkDir")
        for pairs in checkDirs:
            findDirAllWords(pairs[1])

    

    print("totalwords:"+ str(len(wordsList)))
    print("load words success!")
    getAccessToken()

    items=wordsList
    threads = []
    if (len(items)>0):
            for item in items:
                t =threading.Thread(target=checkMsgContent,args=(item,))
                threads.append(t)
    if len(threads) > 0 :
        for t in threads:
            t.start()
        t.join()


checkWords()
sleep(0.1)
os.system("pause")
