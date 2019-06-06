#-*- coding:utf-8 -*-
import os
import sys
import ConfigParser
import json
import re
import xlrd
from collections import OrderedDict
import json
import codecs

import qrcode


paramNameRow=0
dataStartRow=0
gameUrl=""
ignoreParams={}
outputPath=""
outPutNameColumName=""



def makeQRCode(data,name):
    global outputPath
    qr = qrcode.QRCode(     
        version=1,     
        error_correction=qrcode.constants.ERROR_CORRECT_L,     
        box_size=10,     
        border=4, 
    ) 
    qr.add_data(data) 
    qr.make(fit=True)  
    img = qr.make_image()
    img.save(outputPath+"\\"+name+".png")

def checkExcelFile(filePath):
        global paramNameRow
        global dataStartRow
        global gameUrl
        global outputPath
        global outPutNameColumName

	wb = xlrd.open_workbook(filePath)
	shName = wb.sheet_names()[0]
	sh = wb.sheet_by_index(0)
        title = sh.row_values(paramNameRow)
        idx = 0
        for name in title:
            if(outPutNameColumName == name):
                break
            idx+=1
            
        convert_list = []
        print shName
        for rownum in range(dataStartRow, sh.nrows):
                rowvalue = sh.row_values(rownum)
                paramStr=""
                paramPreStr=""
                for colnum in range(0, len(rowvalue)):
                    if not ignoreParams.has_key(str(title[colnum])):
                        paramValue = rowvalue[colnum]
                        if type(rowvalue[idx])== float:
                            paramValue=int(rowvalue[colnum])
                        paramPreStr = paramStr + str(title[colnum])+"="+str(paramValue)
                        paramStr = paramPreStr+"&"
                if paramPreStr != "":
                    print gameUrl+"?"+paramPreStr + " "+ str(rownum)+""
                    outName = rowvalue[idx]
                    if type(rowvalue[idx])== float:
                        outName = int(rowvalue[idx])
                    makeQRCode(gameUrl+"?"+paramPreStr,str(outName))

class MyConfig(ConfigParser.ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.ConfigParser.__init__(self, defaults=defaults)

    # 这里重写了optionxform方法，直接返回选项名
    def optionxform(self, optionstr):
        return optionstr

def batchParser():
    global paramNameRow
    global dataStartRow
    global gameUrl
    global outputPath
    global ignoreParams
    global outPutNameColumName
    iniPath = "config.ini"
    cf = MyConfig()
    cf.read(iniPath)
    gameUrl = cf.get("gameConfig","gameUrl")
    outputPath = cf.get("gameConfig","outPut")
    outPutNameColumName=cf.get("gameConfig","outPutNameColumName")
    outputPath = outputPath.decode('utf-8')
    print "game url:"+ gameUrl
    excelPath = cf.get("paramConfig","fileDir")
    excelPath = excelPath.decode('utf-8')
    print "excel path:"+ excelPath
    paramNameRow= int(cf.get("paramConfig","paramNameRow"))
    dataStartRow= int(cf.get("paramConfig","dataStartRow"))
    ignoreStr= cf.get("paramConfig","igoreParams")
    
    ignoreList=ignoreStr.split(',')
    for key in ignoreList:
        ignoreParams.setdefault(key,True)
    
    if(not os.path.exists(outputPath)):
        os.mkdir(outputPath)
    checkExcelFile(excelPath)
    os.system("pause")

batchParser()
