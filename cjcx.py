#coding=utf-8
import urllib2
from PIL import Image
from io import BytesIO
import base64
import os
import sys
import urllib
import urllib2

def getUrlWithRetry(url):  
    user_agent ='"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'  
    headers = { 'User-Agent' : user_agent }  
    maxTryNum=10  
    for tries in range(maxTryNum):  
        try:  
            req = urllib2.Request(url, headers = headers)   
            html=urllib2.urlopen(req).read()  
            break  
        except:  
            if tries <(maxTryNum-1):  
                continue  
            else:  
                logging.error("Has tried %d times to access url %s, all failed!",maxTryNum,url)  
                break  
              
                  
    return html 


queryUrl='https://www.hneeb.cn/cmsInter/eduInterface/edu/v1/gkcj/image/{0}/{1}'
queryUrl2='https://www.hneeb.cn/pzInter/edu?PARAMS={0}&FLAG=GKCJ&YZM={1}'

ksh = raw_input("Student Num(last 10 number): ");
sfz = raw_input("IdentityId (last 6 number): ");
#queryCode
param= base64.b64encode(str(ksh)+"_"+str(sfz))
image = Image.open(BytesIO(getUrlWithRetry(queryUrl.format(param,"1"))))
image.save('code.jpg')

code= raw_input("code: ");
codeVal=base64.b64encode(str(code))
print getUrlWithRetry(queryUrl2.format(param,codeVal)).decode('utf-8')


