#coding=utf-8
import os,sys
import time
import io
import json


def  checkAnimation(folder):
  for root, dirs, files in os.walk(folder):
        for dirName in dirs:
            if dirName.find(".json") <> -1:  
                checkAnimation(dirName)
        for fileName in files:
            filePath = os.path.join(root, fileName)
            if filePath.find(".json") <> -1:
              f = open(filePath,'r')
              subJson = json.loads(f.read())
              f.close()

              if(type(subJson) == type({}) and subJson.has_key('mc')):
                  animation = subJson['mc']
                  aniKey = fileName.replace('.json','')
                  if(not animation.has_key(aniKey)):
                      print  filePath + "------ " + fileName

if __name__ == "__main__":
        checkAnimation(".")
        print("--------check finish---------")
        os.system("pause")
