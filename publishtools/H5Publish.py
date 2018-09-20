#coding=utf-8
import os,sys
import sys  
import threading
import time
import io
import hashlib
import os,sys
import ConfigParser
import shutil
import datetime
import struct
import binascii
import zipfile
import json
import chardet
import codecs

inputDir = ""
outputDir = ""
pre_md5conf = {}
compressFolders = {}
ecodingFolders={}
zipFolders={}
changedCount = 0
publishVersion = ""
projectPath = ""
publishPath = ""
runPath = ""
jpgQualityValue=str(30)
pngQualityValue=str(30)
totalBytes = 0

#打包目录为zip文件（未压缩）
def make_zip(source_dir, output_filename):
  zipf = zipfile.ZipFile(output_filename, 'w',zipfile.ZIP_DEFLATED)
  pre_len = len(os.path.dirname(source_dir))

  for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
      pathfile = os.path.join(parent, filename)
      arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
      zipf.write(pathfile, arcname)
  zipf.close()

def run_coding(file_dir):
    #需要把文件改成编码的格式
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for i in files:
            files_name = os.path.join(root, i)
            if(files_name.find('.json') <> -1 or files_name.find('.fnt') <> -1 ):
                f = open(files_name,'r')
                content = f.read()
                f.close()
                coding=chardet.detect(content)
                print files_name
                fileCoding  = coding.get('encoding')
                print fileCoding
                if not (fileCoding =='utf-8'):
                  content=codecs.decode(content,'gbk')
                  content = codecs.encode(content,'utf-8')
                  fw=open(files_name,'w')
                  fw.write(content)
                  fw.close()

def make_jsons_to_one(src):
      global inputDir
      global outputDir
      global zipFolders
      for root, dirs, files in os.walk(src):
        for dirName in dirs:
            bignore = False
            if dirName.find(".svn") <> -1:
                bignore = True
            if not bignore:    
                needZipFolder = False
                
                for pair in zipFolders:
                    filePath = os.path.join(root, dirName)
                    if filePath.find(pair[1]) <> -1:
                        needZipFolder = True
                #如果是需要压缩的文件夹 直接zip打包
                if needZipFolder:
                    outFileName = root.replace(inputDir,outputDir)
                    outName = outFileName+"\\" +dirName+ ".json"
                    make_json(root+"\\"+dirName,outName)


def make_json(source_dir, output_filename):
  pre_len = len(os.path.dirname(source_dir))
  jsonContent = "{"
  preContent = ""
  for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
      if filename.find('.json')<>-1:
        pathfile = os.path.join(parent, filename)
        arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
        print(filename)
        f = open(pathfile,'r')
        nameKey = filename.replace('.json','_json')
        subJsonStr = json.dumps(f.read())
        
        f.close()
        subJsonStr=subJsonStr.replace('\\n\\t\\t',' ')
        subJsonStr=subJsonStr.replace('\\n\\t',' ')
        subJsonStr=subJsonStr.replace('  ',' ')
        subJsonStr=subJsonStr.replace('\",\\n','\",')
        subJsonStr=subJsonStr.replace('\": ','\":')
        subContent = "\""+nameKey +"\":"+ subJsonStr
        preContent = jsonContent + " " + subContent
        jsonContent = jsonContent + " " + subContent + ","
  jsonContent = preContent
  jsonContent = jsonContent + "}"
  of = open(output_filename,'wb+')
  of.write(jsonContent)
  of.close()



def packData(data):
    typeDic = 1
    typeList = 2
    typeStr = 3
    typeNum = 4
    typeFloat = 5
    typeLong = 6
    ret = ""
    global totalBytes
    if(type(data) == dict):
      ret = ret + struct.pack('B',typeDic)
      totalBytes = totalBytes + 1
      ret = ret + struct.pack('!i',len(data))
      totalBytes = totalBytes + 4
      ret = ret + packDic(data)
    elif (type(data) == list):
      ret = ret + struct.pack('B',typeList)
      totalBytes = totalBytes + 1
      ret = ret + struct.pack('!i',len(data))
      totalBytes = totalBytes + 4
      for value in data:
        ret = ret + packData(value)
    elif (type(data) == int):
      ret = ret + struct.pack('B',typeNum)
      totalBytes = totalBytes + 1
      ret = ret + struct.pack('!l',data)
      totalBytes = totalBytes + 4
    elif (type(data) == str):
      ret = ret + struct.pack('B',typeStr)
      totalBytes = totalBytes + 1
      ret = ret + struct.pack('!i',len(data))
      totalBytes = totalBytes + 4
      ret = ret + struct.pack(str(len(data))+'s',data)
      totalBytes = totalBytes + len(data)
    elif (type(data) == unicode):
      packStr = data.encode('utf-8')
      ret = ret + struct.pack('B',typeStr)
      totalBytes = totalBytes + 1
      ret = ret + struct.pack('!i',len(packStr))
      totalBytes = totalBytes + 4
      ret = ret + struct.pack(str(len(packStr))+'s',packStr)
      totalBytes = totalBytes + len(packStr)
    elif (type(data) == float):
      ret = ret + struct.pack('B',typeFloat)
      totalBytes = totalBytes + 1
      ret = ret + struct.pack('!d',data)
      totalBytes = totalBytes + 8
    elif (type(data) == long):
      ret = ret + struct.pack('B',typeLong)
      totalBytes = totalBytes + 1
      ret = ret + struct.pack('!d',data)
      totalBytes = totalBytes + 8
    else:
      print(type(data))
      
    return ret
  
def packDic(dic):
    ret=""
    for key in dic:
      ret = ret + packData(key)
      ret = ret + packData(dic[key])
    return ret 

def make_jsons_to_buffer(src):
      global inputDir
      global outputDir
      global zipFolders
      for root, dirs, files in os.walk(src):
        for dirName in dirs:
            bignore = False
            if dirName.find(".svn") <> -1:
                bignore = True
            if not bignore:    
                needZipFolder = False
                
                for pair in zipFolders:
                    filePath = os.path.join(root, dirName)
                    if filePath.find(pair[1]) <> -1:
                        needZipFolder = True
                #如果是需要压缩的文件夹 直接zip打包
                if needZipFolder:
                    outFileName = root.replace(inputDir,outputDir)
                    outName = root+"\\" +dirName+ ".json"
                    outZipName = outFileName+"\\" +dirName+ ".json"
                    make_Buffer(root+"\\"+dirName,outName)
                    zipf = zipfile.ZipFile(outZipName, 'w',zipfile.ZIP_DEFLATED)
                    zipf.write(outName, dirName+ ".json")
                    zipf.close()
                    os.remove(outName)
      

def make_Buffer(source_dir, output_filename):
  pre_len = len(os.path.dirname(source_dir))
  global totalBytes
  typeDic = 1
  typeList = 2
  typeStr = 3
  typeNum = 4
  typeJsonKey = 80
    
  content = ""
  fileCount = 0
  for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
      if filename.find('.json')<>-1:
        pathfile = os.path.join(parent, filename)
        arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
        f = open(pathfile,'r')
        nameKey = filename.replace('.json','_json')
        subJson = json.loads(f.read())
        f.close()

        ret = struct.pack('!i',len(nameKey))
        param = str(len(nameKey))+'s'
        ret = ret + struct.pack(param,nameKey)
        totalBytes=0
        subContent = packData(subJson)
        
        ret = ret + struct.pack('!i',totalBytes)
        subFileContent = ret + subContent
        content = content + subFileContent
        fileCount = fileCount + 1
  countRet = struct.pack('!i',fileCount)
  of = open(output_filename,'wb+')
  of.write(countRet+content)
  of.close()
          
#caculate file md5
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename,'rb')
    b = f.read()
    myhash.update(b)
    f.close()
    return myhash.hexdigest()

def walkFolder(folder, rlist):
    global inputDir
    global outputDir
    for root, dirs, files in os.walk(folder):
        for dirName in dirs:
            walkFolder(dirName, rlist)
        for fileName in files:
            a = fileName.find(".png")
            b = fileName.find(".jpg")
            if a <> -1 or b <> -1:
                filePath = os.path.join(root, fileName)
                if os.path.abspath(filePath) == filePath:
                    fileMd5 = GetFileMd5(filePath)
                    relativePath = filePath.replace(inputDir,"")
                    if pre_md5conf.has_key(relativePath):
                        if not (fileMd5 == pre_md5conf[relativePath]):
                            rlist[relativePath] = filePath
                        pre_md5conf[relativePath] = fileMd5
                    else:
                        rlist[relativePath] = filePath
                        pre_md5conf.setdefault(relativePath,fileMd5)


#load file md5 list
def loadMd5():
    global runPath
    path = runPath + "\\fileMd5"
    if not os.path.exists(path):
        return 
    md5file = open(path,"r")
    
    for text in md5file.readlines():
        part = text.split('\t\t\t',1)
        if len(part) > 1:
            filePath = part[0].strip()
            md5 = str(part[1]).strip()
            pre_md5conf.setdefault(filePath,md5) 
    md5file.close()
    print("load md5 sucess")
    
#save file md5 list    
def saveMd5():
    global runPath
    path = runPath + "\\fileMd5"  
    md5file = open(path, 'w+')
    filecontent = ""
    for filePath in pre_md5conf :
        filecontent = filecontent + filePath + '\t\t\t' + pre_md5conf[filePath] + '\n'
    
    md5file.write(filecontent)   
    md5file.close()

def action(filePath):
    a = filePath.find(".png")
    b = filePath.find(".jpg")
    global inputDir
    global outputDir
    global changedCount
    global pngQualityValue
    global jpgQualityValue
    
    if a <> -1:
        outFileName = filePath.replace(inputDir,outputDir)
        dirName = os.path.dirname(outFileName)
        if not os.path.exists(dirName):
            os.makedirs(dirName)

        cmd = "pngquant.exe --force --output "+ outFileName + " --quality "+pngQualityValue+"-"+pngQualityValue+" %s"%(filePath)
        os.popen(cmd)
	changedCount = changedCount + 1
	print(filePath + "\n")
    elif b <> -1:
        outFileName = filePath.replace(inputDir,outputDir)
        dirName = os.path.dirname(outFileName)
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        
        cmd = "TexturePacker " + filePath + " --jpg-quality "+ jpgQualityValue +" --allow-free-size --disable-rotation --padding 0  --sheet " + outFileName
        os.popen(cmd)
	changedCount = changedCount + 1

def loadConf():
    global inputDir
    global outputDir
    global compressFolders
    global ecodingFolders
    global projectPath
    global publishPath
    global pub
    global runPath
    global zipFolders
    global jpgQualityValue
    global pngQualityValue
    
    iniPath = runPath + "\\config.ini" 
    cf=ConfigParser.ConfigParser()
    cf.read(iniPath)
    ConfigParser.ConfigParser.has_section
    
    inputDir = cf.get("path","inputpath")
    outputDir = cf.get("path","outputpath")
    compressFolders=cf.items("compressfolders")
    zipFolders=cf.items("zipfolders")
    projectPath = inputDir + "\\..\\"
    publishPath = projectPath + "\\bin-release\\web\\" + publishVersion
    if(cf.has_section('compressQuality')):
        jpgQualityValue = cf.get("compressQuality","jpg")
        pngQualityValue = cf.get("compressQuality","png")
    if(cf.has_section('changeForlderCoding')):
        ecodingFolders = cf.items('changeForlderCoding')
    
def compressPathPng(path):
    file_path = {}
    global inputDir
    compresspath = os.path.join(inputDir,path)
    walkFolder(compresspath,file_path)
    file_name_list = file_path
    for filePath in file_name_list:
        t =threading.Thread(target=action,args=(file_name_list[filePath],))
        t.start()

def compressPng():
    global compressFolders
    for pairs in compressFolders:
        compressPathPng(pairs[1])
    if changedCount > 0:
        saveMd5()
    else:
        print("no file changed \n")

def copyFolders(src,ignore):
    global inputDir
    global outputDir
    global zipFolders
    
    for root, dirs, files in os.walk(src):
        for dirName in dirs:
            bignore = False
            if dirName.find(".svn") <> -1:
                bignore = True
            else:
                for pair in ignore:
                    if dirName.find(pair[1]) <> -1:
                        bignore = True
            if not bignore:    
                #needZipFolder = False
                
                #for pair in zipFolders:
                #    filePath = os.path.join(root, dirName)
                #    if filePath.find(pair[1]) <> -1:
                #        needZipFolder = True
                #如果是需要压缩的文件夹 直接zip打包
                #if needZipFolder:
                #    outFileName = root.replace(inputDir,outputDir)
                #    zipName = outFileName+"\\" +dirName+ ".zip"
                #    make_zip(root+"\\"+dirName,zipName)
                copyFolders(dirName,ignore)
            
        for fileName in files:
            filePath = os.path.join(root, fileName)
            
            if filePath.find(".svn") <> -1:
                bignore = True
            else:
                for pair in ignore:
                    if filePath.find(pair[1]) <> -1:
                        bignore = True
            if not bignore:
                outFileName = filePath.replace(inputDir,outputDir)
                dirName = os.path.dirname(outFileName)
                #print(outFileName)
                if not os.path.exists(dirName):
                    os.makedirs(dirName)
                shutil.copy(filePath,outFileName)

def copyJsons(src):
    global inputDir
    global outputDir
    for root, dirs, files in os.walk(src):
        for dirName in dirs:
            bignore = False
            if dirName.find(".svn") <> -1:
                bignore = True
            if not bignore:    
                copyJsons(dirName)
            
        for fileName in files:
            filePath = os.path.join(root, fileName)
            
            if filePath.find(".svn") <> -1:
                bignore = True
            
            if not bignore:
                outFileName = filePath.replace(inputDir,outputDir)
                dirName = os.path.dirname(outFileName)
                if fileName.find(".json") <> -1:                    
                    if not os.path.exists(dirName):
                        os.makedirs(dirName)
                    shutil.copy(filePath,outFileName)                
                
def copyResource():
    global inputDir
    global outputDir
    global compressFolders
    copyFolders(inputDir,compressFolders)

    for pairs in compressFolders:
        copyJsons(inputDir+pairs[1])
    

def svnUpdate():
    global projectPath
    global outputDir
    os.system("svn update " + projectPath)
    os.system("svn update " + outputDir+"..\\")

def publishProject():
    global publishVersion
    global projectPath
    global runPath
    os.chdir(projectPath)
    os.system("egret publish --version  " + publishVersion)
    os.chdir(runPath)

def copyScripts():
    global outputDir
    global publishPath
    if os.path.exists(outputDir +"..\\js\\"):
        shutil.rmtree( outputDir +"..\\js\\" )
        
    shutil.copytree( publishPath +"\\js\\",outputDir+"..\\js\\")
    shutil.copy(publishPath+"\\index.html",outputDir+"..\\index.html")
    shutil.copy(publishPath+"\\manifest.json",outputDir+"..\\manifest.json")



def testPackJson():
    subJson = json.loads("{\"a\":[1,2,\"3\",0.05,4,5]}")
    print packDic(subJson)

def addTexturPackerPath():
    runPath = os.path.abspath('.')
    os.environ["PATH"] = os.environ["PATH"]+";"+ runPath+'/bin'

def change_coding():
    global ecodingFolders
    global outputDir
    for pairs in ecodingFolders:
        run_coding( outputDir + pairs[1])
    
def run():
        global runPath
        global publishVersion

        addTexturPackerPath()
        runPath = os.path.abspath('.')
        #记录更新时间点 当作发布版本号
        publishVersion=datetime.datetime.now().strftime('%Y%m%d%H%M')

        #加载配置文件
        loadConf()
        
        #更新项目svn目录
        svnUpdate()

        #发布目录
        publishProject()

        #拷贝编译脚本
        copyScripts()
        
        #加载md5文件
        loadMd5()
        #压缩需要压缩的文件
        compressPng()
        #拷贝其他资源文件
        copyResource()
        global inputDir
        #make_jsons_to_one(inputDir)
        make_jsons_to_buffer(inputDir)
        #testPackJson()
        change_coding()
        os.system("pause")


			
if __name__ == "__main__":
	run()
