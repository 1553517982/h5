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

        findFileName=""
        files = os.listdir("./")
        for f in files:
            if f.endswith('.game'):
                findFileName=f
                break
        appid=""
        if findFileName=="com.CCshacheng.game":
            appid="q500116"
            key="1c56cbf7c037fc3940d30bebe2155ca2"
        elif findFileName=="com.BNchuanqi.game":
            appid="q500112"
        elif findFileName=="com.CCzhanshen.game":
            key="422caae1cb795514a01e7ae7432ef7bf"
            appid="q500117"
        print appid
        with open(findFileName) as file_obj:
            content = file_obj.read()
            jobj=json.loads(content)
            userdata = jobj["content"]
            decrypted = decrypt(key, userdata)

            ##modify skill
            userObj=json.loads(decrypted)
            uid=userObj["userAllData"][0]["data"]["userData"]["userInfo"]["userName"]
            for k in userObj["userAllData"]:
                skilldata = k["data"]["sklliData"]
                #modify skill
                for i in  range(0,len(skilldata)):
                    skilldata[i]["isLearn"]=1
                    skilldata[i]["lv"]=9
                #modify money exp
                userinfo=k["data"]["userData"]["userInfo"]
                userinfo["lv"]=79
                userinfo["upLvExp"]=1000000000000
                userinfo["jinBi"]=1000000000
                userinfo["yuanBao"]=10000
                userinfo["cream"]=1000000000
                userinfo["duty"]="爸爸"
                
                #modify bag
                userbag=k["data"]["userData"]["userBag"]
                userbag["bagLen"]=500
                baglist=userbag["bagData"]
                
                #modify equip
                userequip=k["data"]["userData"]["userBag"]["equipData"]
                mainatk="atk"
                if userinfo["dutyName"]=="daoShi":
                    mainatk="spt"
                elif userinfo["dutyName"]=="faShi":
                    mainatk="mag"
                elif userinfo["dutyName"]=="zhanShi":
                    mainatk="atk"
                    
                random = [mainatk,"lucky","magic_find1","HpDrain","MpDrain","DamageReduction","BonusDamage","hp","mp","speed","def"]
                
                for equip in userequip:
                    if len(equip)>0:
                        equip["d_suiji"]=[]
                        equip["randomEffectInfo"]=[]
                        for attr in random:
                            subattr={"max":300,"name":attr,"value":300}
                            equip["d_suiji"].append(subattr)
                            equip["randomEffectInfo"].append(subattr)
                            equip["quality"]=4
                            equip["class"]=4
                            equip["d_pinzhi"]= 4
                            equip["color"]="#ff0c00",
                
                #modify yueka
                starttime=1590589360
                endTime=7952342400000
                
                k["data"]["initialCharge"]["profit"]["isTong"]=1
                k["data"]["initialCharge"]["profit"]["startTime"]=starttime
                k["data"]["initialCharge"]["profit"]["endTime"]=endTime

                k["data"]["initialCharge"]["recovery"]["isTong"]=1
                k["data"]["initialCharge"]["recovery"]["startTime"]=starttime
                k["data"]["initialCharge"]["recovery"]["endTime"]=endTime

                k["data"]["initialCharge"]["godOfWar"]["isTong"]=1
                k["data"]["initialCharge"]["godOfWar"]["startTime"]=starttime
                k["data"]["initialCharge"]["godOfWar"]["endTime"]=endTime
                
                
                    
            userinfo=  json.dumps(userObj)  
            ##send userdata
            
            passed = encrypt(key,userinfo).decode('hex')
            passed = base64.b64encode(str(passed))
            jobj["content"]=passed
            after=json.dumps(jobj)
            
            t=time.time();
            s = "app_id^"+appid+"data^"+after+"time^"+str(t)+"uid^"+uid+key
            m= hashlib.md5(s.encode()).hexdigest()

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
