#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ssl
import http.client
import requests
import urllib2,urllib,httplib
import sys,os,hashlib,time,base64,codecs,json

MOD = 256

def KSA(key):
    key_length = len(key)
    # create the array "S"
    S = range(MOD)  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + ord(key[i % key_length])) % MOD
        S[i], S[j] = S[j], S[i]  # swap values

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        yield K


def get_keystream(key):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSA(key)
    return PRGA(S)


def encrypt(key, plaintext):
    keystream = get_keystream(key)

    res = []
    for c in plaintext:
        val = ("%02X" % (ord(c) ^ next(keystream)))  # XOR and taking hex
        res.append(val)
    return ''.join(res)


def decrypt(key, ciphertext):
    ''' :key -> encryption key used for encrypting, as hex string
        :ciphertext -> hex encoded ciphered text using RC4
    '''
    ciphertext = base64.b64decode(ciphertext)
    #print 'ciphertext to func:', ciphertext  # optional, to see
    res = encrypt(key, ciphertext)
    return res.decode('hex')


def main():
        key = "5fdd79763095baae440e87f7e1789d18"
        jobj=json.loads("{\"bnsycVERSION\":2,\"content\":\"\"}")
        with codecs.open('out.txt',"r") as f:
            userinfo=f.read()
            userObj=json.loads(userinfo)
            uid=userObj["userAllData"][0]["data"]["userData"]["userInfo"]["userName"]
            appid="q500112"
            passed = encrypt(key,userinfo).decode('hex')
            passed = base64.b64encode(str(passed))
            jobj["content"]=passed
            after=json.dumps(jobj)
            t=time.time();
            s = "app_id^"+appid+"data^"+after+"time^"+str(t)+"uid^"+uid+key
            m= hashlib.md5(s.encode()).hexdigest()
            print m

            datas = {"app_id": appid, "data": after,"time":t,"uid":uid,"sign":m}
            url = "https://qd.hnchangchuan.cn/light-game-api/date-persistence"
            
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "qd.hnchangchuan.cn",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                'Referer':"qd.hnchangchuan.cn",
                "User-Agent": "okhttp/3.11.0"
            }
            
            r = requests.post(url,headers=headers, data=datas, verify=False)
            print("success")
            os.system("pause")

if __name__ == '__main__':
    main()
