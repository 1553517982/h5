# -*- coding: utf-8 -*-
from pydub import AudioSegment
from pydub.silence import detect_silence
import re
import os
import ConfigParser

inputDir=""
outDir=""
outformat="mp3"

def loadConf():
    global inputDir
    global outDir
    
    cf=ConfigParser.ConfigParser()
    cf.read("config.ini")
    inputDir = cf.get("path","inputpath")
    outDir = cf.get("path","outputpath")
    outformat = cf.get("path","outputformat")

def initEnv():
    runPath = os.path.abspath('.')
    os.environ["PATH"] = os.environ["PATH"]+";"+ runPath

def splitFile(filename,fileFormat):
    global inputDir
    global outformat
    sound = AudioSegment.from_file(filename, format=fileFormat)
    start_end = detect_silence(sound,300,-35,1)
    index=0
    maxLen = len(start_end)
    for i in range(0,len(start_end)):
        subpart = start_end[i]
        outputname = filename[len(inputDir):-(len(fileFormat))-1]
        targetfile = outDir+"/"+outputname+"_part"+str(index)+"."+outformat
        start=int(subpart[1])
        if i< maxLen-1:
            nextpart = start_end[i+1]
            soundoutput = sound[start:int(nextpart[0])]
            soundoutput.export(targetfile, format=outformat)        
        else:
            if start< (len(sound)-1):
                soundoutput = sound[start:len(sound)-1]
                soundoutput.export(targetfile, format=outformat)
        index+=1

def PaserSounds():
    global inputDir
    loadConf()
    initEnv()
    for parent, dirnames, filenames in os.walk(inputDir):
        for filename in filenames:
          pathfile = os.path.join(parent, filename)
          fileformat = os.path.splitext(pathfile)[1]
          splitFile(pathfile,fileformat[1:])
    os.system("pause")

PaserSounds()
