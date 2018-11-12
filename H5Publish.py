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
pre_versionconf = {}
compressFolders = {}
ecodingFolders={}
packFolders = {}
zipFolders={}
changedCount = 0
publishVersion = ""
projectPath = ""
publishPath = ""
runPath = ""
jpgQualityValue=str(30)
pngQualityValue=str(30)
totalBytes = 0
remoteCfgJson = {}
resVersion="1.0"

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
                fileCoding  = coding.get('encoding')
                if not (fileCoding =='utf-8'):
                  print(files_name)
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

def make_jsons_to_Multi_buffer(src):
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
                    make_Mult_Buffer(root+"\\"+dirName)
                    

def make_Mult_Buffer(source_dir):
  pre_len = len(os.path.dirname(source_dir))
  global inputDir
  global outputDir
  global totalBytes
  global remoteCfgJson
  
  typeDic = 1
  typeList = 2
  typeStr = 3
  typeNum = 4
  typeJsonKey = 80
  remoteCfgJson = {}
  content = ""
  outName = ""
  preName = ""
  cfgKeys = ""
  outPath = ""
  fileCount = 0
  output_dir = source_dir.replace(inputDir,outputDir)
  for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
      if filename.find('.json')<>-1:
        outName = "dataPart" + str(ord(filename[0:1].lower()) - ord('a'))
        
        if not (preName == outName) and not (preName =="") :
          outPath = output_dir+'/'+preName+'.dat'
          relativePath = outPath.replace(outputDir,'')
          remoteCfgJson.setdefault(preName + '_dat',relativePath)
          
          countRet = struct.pack('!i',fileCount)
          of = open(outPath,'wb+')
          of.write(countRet+content)
          of.close()
          fileCount = 0
          content = ""
          
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

        preName = outName
        
    relativePath = outPath.replace(outputDir,'')
    remoteCfgJson.setdefault(outName + '_dat',relativePath);
    
    
    countRet = struct.pack('!i',fileCount)
    of = open(outPath,'wb+')
    of.write(countRet+content)
    of.close()
    fileCount = 0
    content = ""
          
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
    global pre_md5conf
    global pre_versionconf

    if folder.find(".svn") <> -1:
        return
    for root, dirs, files in os.walk(folder):
        for dirName in dirs:
            if folder.find(".svn") <> -1:
                continue
            else:
                subforlder = os.path.join(root, dirName)
                walkFolder(subforlder, rlist)
        for fileName in files:
                filePath = os.path.join(root, fileName)
                if os.path.abspath(filePath).find(".svn") <> -1:
                    continue
                if os.path.abspath(filePath) == filePath:
                    fileMd5 = GetFileMd5(filePath)
                    relativePath = filePath.replace(inputDir,"")

                    preVer = "0"
                    rlist[relativePath] = filePath
                    if pre_md5conf.has_key(relativePath):
                        preVer = pre_versionconf[relativePath]
                        preMd5 = pre_md5conf[relativePath]
                        if not (fileMd5 == preMd5 ):
                            pre_versionconf[relativePath] = str(int(preVer)+1)
                            preVer = pre_versionconf[relativePath]
                        pre_md5conf[relativePath] = fileMd5
                        pre_versionconf[relativePath] = preVer
                    else:
                        rlist[relativePath] = filePath
                        pre_md5conf.setdefault(relativePath,fileMd5)
                        pre_versionconf.setdefault(relativePath,preVer)


#load file md5 list
def loadMd5():
    global runPath
    global outputDir
    global pre_versionconf
    global pre_md5conf
    path = outputDir + "..\\fileMd5"
    if not os.path.exists(path):
        return 
    md5file = open(path,"r")
    
    for text in md5file.readlines():
        part = text.split('\t\t\t')
        filePath = part[0].strip()
        md5 = str(part[1]).strip()
        ver = str(part[2]).strip()
        pre_versionconf.setdefault(filePath,ver)
        pre_md5conf.setdefault(filePath,md5)
    md5file.close()
    print("load md5 sucess")
    
#save file md5 list    
def saveMd5():
    global runPath
    global pre_md5conf
    global pre_versionconf
    path = outputDir + "..\\fileMd5"
    md5file = open(path, 'w+')
    filecontent = ""
    for filePath in pre_md5conf :
        ver = ""
        if pre_versionconf.has_key(filePath):
            ver = pre_versionconf[filePath]
        filecontent = filecontent + filePath + '\t\t\t' + pre_md5conf[filePath] +'\t\t\t'+ ver +'\n'
    
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

    outFileName = filePath.replace(inputDir,outputDir)
    key = filePath.replace(inputDir,'')
    currentVersion = ""
    #if pre_versionconf.has_key(key):
    #todo  增量更新  版本号  
    #
    if a <> -1:    
        dirName = os.path.dirname(outFileName)
        if not os.path.exists(dirName):
            os.makedirs(dirName)

        cmd = "pngquant.exe --force --output "+ outFileName + " --quality "+pngQualityValue+"-"+pngQualityValue+" %s"%(filePath)
        os.popen(cmd)
	
	print(filePath + "\n")
    elif b <> -1:
        dirName = os.path.dirname(outFileName)
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        
        cmd = "TexturePacker " + filePath + " --jpg-quality "+ jpgQualityValue +" --allow-free-size --disable-rotation --padding 0  --sheet " + outFileName
        print(filePath + "\n")
        os.popen(cmd)
    else:
        dirName = os.path.dirname(outFileName)
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        shutil.copy(filePath,outFileName)
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
    global packFolders
    global resVersion
    iniPath = runPath + "\\config.ini" 
    cf=ConfigParser.ConfigParser()
    cf.read(iniPath)
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
    if (cf.has_section('packfolder')):
        packFolders = cf.items("packfolder")
    
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
            bignore=False
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
            bignore=False
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

#生成资源管理的json
def make_resJson():
    global outputDir
    global inputDir
    global packFolders
    global pre_versionconf
    global pre_md5conf
    global resVersion
    global publishVersion
    #resource下所有需要打包的文件
    file_path = {}
    for dir in packFolders:
        walkFolder(inputDir+dir[1],file_path)

    resjsonPath = inputDir+'default.res.json'
    f = open(resjsonPath,'r')
    
    jsonObj = json.loads(f.read())
    f.close()

    print(len(jsonObj["groups"]))
    jsonObj["resources"] = []
    fileTypeKind = {}
    fileTypeKind["png"] = "image"
    fileTypeKind["jpg"] = "image"
    fileTypeKind["json"] = "json"
    fileTypeKind["webp"] = "image"
    fileTypeKind["fnt"] = "font"
    fileTypeKind["pvr"] = "pvr"
    fileTypeKind["mp3"] = "sound"
    fileTypeKind["sheet"] = "sheet"
    fileTypeKind["exml"] = "text"
    fileTypeKind["zip"] = "zip"
    fileTypeKind["mif"] = "bin"
    fileTypeKind["bin"] = "bin"


    binKeys=""
    binKeysPre=""
    for resPath in file_path:
        cfg = {}
        fileName, fileType = os.path.splitext(resPath)
        kind = fileType.replace('.','')
        if( kind == "exml" or kind == ""):
          continue
        #print fileName ,kind
        #合图的json需要按照sheet来解析
        newVersion = ""
        if(pre_versionconf.has_key(resPath)) and int(pre_versionconf[resPath]) > 0 :
            newVersion = str(pre_versionconf[resPath])

        oldName = resPath
        #newName = fileName + newVersion + fileType
        #不能用这种方式   只能用文件夹来当版本号
        tmpDirName = os.path.dirname(resPath)
        index = tmpDirName.find('/')
        if(index < 0):
            index = tmpDirName.find('\\')
        firstFolder = tmpDirName
        if index >= 0:
          firstFolder = tmpDirName[0:index]
        versionDir=tmpDirName
        if(newVersion != ""):
          versionDir = tmpDirName.replace(firstFolder,firstFolder+"_ver"+newVersion,1)
        newName = resPath.replace(os.path.dirname(resPath),versionDir)
        unuse ,fileName = os.path.split(resPath)
        fileName = fileName.replace(fileType,'')
        fileKey = fileName + "_"+kind
        isSheet=False
        sheetName=""
        if( kind == "json"):
            sheetJson = open(inputDir+resPath, 'r')
            sheetJsonObj = json.loads(sheetJson.read())
            sheetJson.close()
            if isinstance(sheetJsonObj,dict) and sheetJsonObj.has_key("file") and sheetJsonObj.has_key("frames"):
                cfg.setdefault("url", newName)
                cfg.setdefault("type", "sheet")
                isSheet = True
                sheetName=sheetJsonObj["file"]
                cfg.setdefault("name", fileName + "_" + kind)
                subkeys = ""
                subkeysPre = ""
                for subkey in sheetJsonObj["frames"].keys():
                    subkeysPre = subkeys + subkey
                    subkeys = subkeys + subkey + ','
                subkeys = subkeysPre
                sheetJson = open(outputDir + resPath, 'w+')
                contents = json.dumps(sheetJsonObj)
                sheetJson.write(contents)
                sheetJson.close()
                cfg.setdefault("subkeys", subkeys)
            else:
                cfg.setdefault("url", newName)
                cfg.setdefault("type", fileTypeKind[kind])
                cfg.setdefault("name", fileName + "_" + kind)
        else:
            cfg.setdefault("url", newName)
            cfg.setdefault("type", fileTypeKind[kind])
            cfg.setdefault("name", fileName + "_"+kind)
        jsonObj["resources"].append(cfg)
        
        if not os.path.exists(outputDir+versionDir):
            os.makedirs(outputDir+ versionDir)
        if not os.path.exists(outputDir+newName):
            shutil.copy(outputDir + oldName, outputDir + newName)

        if isSheet:
            if os.path.exists(outputDir + tmpDirName + "/" + sheetName):
                os.remove(outputDir + tmpDirName + "/" + sheetName)
            shutil.copy(inputDir + tmpDirName+"/"+sheetName, outputDir + tmpDirName + "/" + sheetName)
        #移除bin生成文件
        if kind == "bin":
            binKeysPre=binKeys+fileKey  
            binKeys=binKeysPre+","
            os.remove(inputDir+resPath)

    binKeys = binKeysPre
    binGroupCfg={}
    binGroupCfg.setdefault("name","binConfig")
    binGroupCfg.setdefault("keys",binKeys)
    jsonObj["groups"].append(binGroupCfg)
    
    #先添加配置分组
    fileContents = json.dumps(jsonObj,indent=0,separators=(',', ':'))
    fileContents = fileContents.replace('\\\\', '/')
    fileContents = fileContents.replace(': ', ':')


    publishIniPath = outputDir + "..\\publish.ini"
    cf = ConfigParser.ConfigParser()
    cf.read(publishIniPath)
    mainVersion = cf.get("version","mainVersion");
    subVersion = cf.get("version", "subVersion");
    f = open(outputDir+'default.res'+ mainVersion + "." + subVersion + '.json','w+')
    f.write(fileContents)
    f.close()
    cf.set("version","subVersion",str(int(subVersion)+1))
    cf.set("version","publishTime",publishVersion)
    cf.write(open(outputDir + "..\\publish.ini","wb"))

def compressJsons():
    global packFolders
    global outputDir
    for pairs in packFolders:
        compressCfg( outputDir + pairs[1])

def compressCfg(file_dir):
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for i in files:
            files_name = os.path.join(root, i)
            compressCfgFile(files_name)

def compressCfgFile(files_name):
    if files_name.find('.json') <> -1:
      f = open(files_name,'r')
      content = f.read()
      coding=chardet.detect(content)
      fileCoding  = coding.get('encoding')
      if not (fileCoding =='utf-8'):
        content=codecs.decode(content,'gbk')
        content = codecs.encode(content,'utf-8')
      jsonObj = json.loads(content)
      f.close()
      fileContents = json.dumps(jsonObj,ensure_ascii=False,indent=0,separators=(',', ':'))
      f = codecs.open(files_name,'w+','utf-8')
      f.write(fileContents)
      f.close()


def compress_cfg(source_dir):
  pre_len = len(os.path.dirname(source_dir))
  global inputDir
  global outputDir
  global totalBytes
  global remoteCfgJson
  
  
  typeDic = 1
  typeList = 2
  typeStr = 3
  typeNum = 4
  typeJsonKey = 80
  remoteCfgJson = {}
  content = ""
  outName = ""
  preName = ""
  cfgKeys = ""
  outPath = ""
  
  for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
      if filename.find('.json')<>-1:        
        pathfile = os.path.join(parent, filename)
        outPath = pathfile.replace('.json','_json')
        
        arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
        f = open(pathfile,'r')
        nameKey = filename.replace('.json','_json')
        subJson = json.loads(f.read())
        f.close()
        binFileContent=""
        fileContent = ""
        #文件key
        ret = struct.pack('!i',len(nameKey))
        param = str(len(nameKey))+'s'
        ret = ret + struct.pack(param,nameKey)
        #文件内容
        totalBytes=0
        fileContent = packData(subJson)
        ret = ret + struct.pack('!i',totalBytes)
        #字节流文件 文件头信息+文件内容
        binFileContent = ret + fileContent
        
        countRet = struct.pack('!i',1)
        of = open(outPath,'wb+')
        of.write(countRet+binFileContent)
        of.close()

        zipFileName=pathfile.replace('.json','.bin')
        if(os.path.exists(zipFileName)):
          os.remove(zipFileName)
        zipf = zipfile.ZipFile(zipFileName, 'w',zipfile.ZIP_DEFLATED)
        zipf.write(outPath, nameKey)
        zipf.close()
        
        os.remove(outPath)


def compress_cfg2(source_dir):
    global inputDir
    global outputDir

    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.find('.json') <> -1:
                pathfile = os.path.join(parent, filename)
                nameKey = filename.replace('.json', '_json')
                zipFileName = pathfile.replace('.json', '.bin')

                if (os.path.exists(zipFileName)):
                    os.remove(zipFileName)

                zipf = zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED)
                zipf.write(pathfile, nameKey)
                zipf.close()

def run():
        global runPath
        global publishVersion
        global inputDir
        global zipFolders
        
        addTexturPackerPath()
        runPath = os.path.abspath('.')
        #记录更新时间点 当作发布版本号
        publishVersion=datetime.datetime.now().strftime('%Y%m%d%H%M')

        #加载配置文件
        loadConf()
        
        #更新项目svn目录
        svnUpdate()

        #压缩配置
        for pair in zipFolders:
          #compress_cfg(inputDir+pair[1])
          compress_cfg2(inputDir+pair[1])
        #发布目录
        publishProject()
                
        #拷贝编译脚本
        copyScripts()
        
        #加载md5文件
        loadMd5()
        #压缩需要压缩的文件
        #compressPng()
        #拷贝其他资源文件
        copyResource()
        #make_jsons_to_one(inputDir)
        #make_jsons_to_buffer(inputDir)
        
        #testPackJson()
        #compressJsons()
        #打包配置文件
        #make_jsons_to_Multi_buffer(inputDir)
        #生成增量更新的resJson
        make_resJson()

        change_coding()

        saveMd5()
        os.system("pause")

			
if __name__ == "__main__":
	run()
