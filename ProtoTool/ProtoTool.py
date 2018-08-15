# coding:utf-8
__author__ = 'Administrator'

from PyQt4 import QtGui
from PyQt4 import QtCore

import EditorMainPanel
import sys
import ConfigParser
import json

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
protoTypeList = ["client", "server"]
paramTypeList = ["required", "optional", "repeated", "map", "map2"]
valueTypeList = ["string", "int32", "double"]#, "float"]


def optionxform(self, optionstr):
    return optionstr.lower()


class MyConfig(ConfigParser.ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.ConfigParser.__init__(self, defaults=defaults)

    # 这里重写了optionxform方法，直接返回选项名
    def optionxform(self, optionstr):
        return optionstr


# 初始化字段类型
def initParam():
    paramType = paramTypeList[0]
    valueType = valueTypeList[0]
    paramCfg = {
        'name': "undefine",
        'paramType': paramType,
        'valueType': valueType
    }
    return paramCfg


# 预览结构体
def Struct2String(name, structCfg):
    previewContent = "\""
    previewContent = previewContent + name + "\":{\n"

    count = len(structCfg)
    for key in range(0, count):
        # for key in structCfg:
        subConf = structCfg[key]
        dotSymbol = ""
        if str(count - 1) != str(key):
            dotSymbol = ","
        nameStr = ""
        if subConf['name'] != "":
            nameStr = " " + subConf['name']

        subParam = "\"" + subConf['paramType'] + " " + subConf['valueType'] + nameStr + "\":" + str(
            int(key) + 1) + dotSymbol + "\n"
        previewContent = previewContent + "\t" + subParam
    previewContent = previewContent + "}"
    return previewContent


class MainForm(QtGui.QMainWindow, EditorMainPanel.Ui_EditorMainPanel):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)

        self.ignoreListChange = False
        self.isRefreshProto = False
        self.isRefreshServerProto = False
        self.isRefreshMessage = False
        self.selectStructName = None
        self.selectProtoName = None
        self.selectServerProtoName = None
        # ---------------------------协议初始化------------------------------------------
        # 客户端协议列表
        self.protoList = {}
        #服务端协议列表
        self.serverProtoList = {}

        # 加载协议配置
        self.loadProtos()
        self.loadProtos2()

        self.structList = {}
        # 加载结构体配置
        self.loadStructs()

        self.list_proto.setColumnCount(1)
        self.list_proto.setColumnWidth(0, 250)
        self.table_protoColum.setColumnWidth(0, 100)
        self.table_protoColum.setColumnWidth(1, 220)
        self.table_protoColum.setColumnWidth(2, 100)

        self.list_proto_2.setColumnCount(1)
        self.list_proto_2.setColumnWidth(0, 250)
        self.table_protoColum_2.setColumnWidth(0, 100)
        self.table_protoColum_2.setColumnWidth(1, 220)
        self.table_protoColum_2.setColumnWidth(2, 100)

        self.connect(self.lineEdit,QtCore.SIGNAL(_fromUtf8("textChanged(const QString&)")),self.onFilterProto)
        self.connect(self.btn_deleteProto, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_deleteProtoClicked)
        self.connect(self.btn_deleteColum, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_deleteProtoParamClicked)
        self.connect(self.btn_addProto, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_addProtoClicked)
        self.connect(self.btn_addColum, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_addProtoParam)
        self.connect(self.list_proto, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.on_ProtoItemClicked)
        self.connect(self.list_proto, QtCore.SIGNAL('itemDoubleClicked(QTableWidgetItem*)'),
                     self.on_ProtoItemDoubleClicked)
        self.connect(self.list_proto, QtCore.SIGNAL('itemChanged(QTableWidgetItem*)'), self.on_currentProtoChanged)
        self.connect(self.table_protoColum, QtCore.SIGNAL('cellChanged(int,int)'), self.on_protoParamChanged)

        self.connect(self.btn_deleteProto_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_deleteProtoClicked2)
        self.connect(self.btn_deleteColum_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_deleteProtoParamClicked2)
        self.connect(self.btn_addProto_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_addProtoClicked2)
        self.connect(self.btn_addColum_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_addProtoParam2)
        self.connect(self.list_proto_2, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.on_ProtoItemClicked2)
        self.connect(self.list_proto_2, QtCore.SIGNAL('itemDoubleClicked(QTableWidgetItem*)'),
                     self.on_ProtoItemDoubleClicked2)
        self.connect(self.list_proto_2, QtCore.SIGNAL('itemChanged(QTableWidgetItem*)'), self.on_currentProtoChanged2)
        self.connect(self.table_protoColum_2, QtCore.SIGNAL('cellChanged(int,int)'), self.on_protoParamChanged2)

        # ---------------------------结构体初始化------------------------------------------
        self.list_struct.setColumnCount(1)
        self.list_struct.horizontalHeader().setDefaultSectionSize(280)
        self.table_structColum.setColumnWidth(0, 100)
        self.table_structColum.setColumnWidth(1, 220)
        self.table_structColum.setColumnWidth(2, 100)

        self.connect(self.btn_deletestruct, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_deleteStructClicked)
        self.connect(self.btn_deleteColum_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_deleteStructParamClicked)
        self.connect(self.btn_addstruct, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_addStructClicked)
        self.connect(self.btn_addColum_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_addStructParam)
        self.connect(self.list_struct, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.on_StructItemClicked)
        self.connect(self.list_struct, QtCore.SIGNAL('itemDoubleClicked(QTableWidgetItem*)'),
                     self.on_StructItemDoubleClicked)
        self.connect(self.list_struct, QtCore.SIGNAL('itemChanged(QTableWidgetItem*)'), self.on_currentStructChanged)
        self.connect(self.table_structColum, QtCore.SIGNAL('cellChanged(int,int)'), self.on_structParamChanged)

        # 默认选中协议页卡
        self.tabWidget.setCurrentIndex(0)

    # 获取所有数据类型的集合  除了基本数据类型  message也可以当作数据类型
    def getValueTypeList(self):
        typeList = []
        for idx in valueTypeList:
            typeList.append(idx)
        for key in self.structList:
            typeList.append(key)
        return typeList

    # ------------------------------------键盘监听函数------------------------------
    def keyPressEvent(self, event):
        key = event.key()
        # 按下Delete
        curIdx = self.tabWidget.currentIndex()
        if key == QtCore.Qt.Key_Delete:
            if self.tabWidget.currentIndex() == 0:
                self.on_deleteProtoParamClicked()
            elif self.tabWidget.currentIndex() == 1:
                self.on_deleteProtoParamClicked2()
            elif self.tabWidget.currentIndex() == 2:
                self.on_deleteStructParamClicked()
            # todo
        elif key == QtCore.Qt.Key_S and (event.modifiers() == QtCore.Qt.ControlModifier):
            self.saveProtos()

    def resetList(self):
        self.list_proto.setRowCount(len(self.protoList))
        curIdx = 0
        for protoName in self.protoList:
            newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
            self.list_proto.setItem(curIdx, 0, newItem)
            curIdx = curIdx + 1

        self.list_proto_2.setRowCount(len(self.serverProtoList))
        curIdx = 0
        for protoName in self.serverProtoList:
            newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
            self.list_proto_2.setItem(curIdx, 0, newItem)
            curIdx = curIdx + 1

        self.list_struct.setRowCount(len(self.structList))
        curIdx = 0
        for protoName in self.structList:
            newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
            self.list_struct.setItem(curIdx, 0, newItem)
            curIdx = curIdx + 1


    def onFilterProto(self,text):
        self.ignoreListChange = True
        self.resetList()
        if self.tabWidget.currentIndex() == 0:
            items = self.list_proto.findItems(text, QtCore.Qt.MatchContains)
            self.list_proto.clearContents()
            if len(items) == 0:
                self.ignoreListChange = False
                return
            self.list_proto.setRowCount(len(items))
            curIdx = 0
            for protoName in self.protoList:
                if protoName.find(text) <> -1:
                    newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
                    self.list_proto.setItem(curIdx, 0, newItem)
                    curIdx = curIdx + 1

        elif self.tabWidget.currentIndex() == 1:
            items = self.list_proto_2.findItems(text,QtCore.Qt.MatchContains)
            self.list_proto_2.clearContents()
            if len(items) == 0:
                self.ignoreListChange = False
                return
            self.list_proto_2.setRowCount(len(items))
            curIdx = 0
            for protoName in self.serverProtoList:
                if protoName.find(text) <> -1:
                    newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
                    self.list_proto_2.setItem(curIdx, 0, newItem)
                    curIdx = curIdx + 1
        elif self.tabWidget.currentIndex() == 2:
            items = self.list_struct.findItems(text,QtCore.Qt.MatchContains)
            self.list_struct.clearContents()
            if len(items) == 0:
                self.ignoreListChange = False
                return

            self.list_struct.setRowCount(len(items))
            curIdx = 0
            for protoName in self.structList:
                if protoName.find(text) <> -1:
                    newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
                    self.list_struct.setItem(curIdx, 0, newItem)
                    curIdx = curIdx + 1
        self.ignoreListChange = False
    # ---------------------------------------------------------------------------
    # ---------------------------协议--------------------------------------------
    # ---------------------------------------------------------------------------
    # 加载协议配置
    def loadProtos(self):
        iniPath = "clientproto.ini"
        cf = MyConfig()
        cf.read(iniPath)
        secList = cf.sections()

        for protoName in secList:
            jsonstr = cf.get(protoName, "proto")
            dic = json.loads(str(jsonstr))
            proto = {}
            for key in dic:
                proto.setdefault(int(key), dic[key])
            self.protoList.setdefault(protoName, proto)

        self.list_proto.setRowCount(len(self.protoList))

        curIdx = 0
        for protoName in self.protoList:
            newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
            self.list_proto.setItem(curIdx, 0, newItem)
            curIdx = curIdx + 1

    # 加载协议配置
    def loadProtos2(self):
        iniPath = "serverproto.ini"
        cf = MyConfig()
        cf.read(iniPath)
        secList = cf.sections()

        for protoName in secList:
            jsonstr = cf.get(protoName, "proto")
            dic = json.loads(str(jsonstr))
            proto = {}
            for key in dic:
                proto.setdefault(int(key), dic[key])
            self.serverProtoList.setdefault(protoName, proto)

        self.list_proto_2.setRowCount(len(self.serverProtoList))

        curIdx = 0
        for protoName in self.serverProtoList:
            newItem = QtGui.QTableWidgetItem(_fromUtf8(protoName))
            self.list_proto_2.setItem(curIdx, 0, newItem)
            curIdx = curIdx + 1

    # 保存协议配置文件
    def saveProtoCfg(self):
        iniPath = "clientproto.ini"
        file = open(iniPath, 'w+')
        file.write("")
        file.close()

        cf = MyConfig()
        cf.read(iniPath)

        protoKeys = self.protoList.keys()
        protoKeys.sort()

        for protoName in protoKeys:
            cf.add_section(protoName)
            protoCfg = self.protoList[protoName]
            cf.set(protoName, "proto", str(json.dumps(protoCfg)))

        cf.write(open(iniPath, 'w+'))

    # 保存协议配置文件
    def saveProtoCfg2(self):
        iniPath = "serverproto.ini"
        file = open(iniPath, 'w+')
        file.write("")
        file.close()

        cf = MyConfig()
        cf.read(iniPath)

        protoKeys = self.serverProtoList.keys()
        protoKeys.sort()

        for protoName in protoKeys:
            cf.add_section(protoName)
            protoCfg = self.serverProtoList[protoName]
            cf.set(protoName, "proto", str(json.dumps(protoCfg)))

        cf.write(open(iniPath, 'w+'))

    def exportProtoJson(self):
        serverProtoFile = 'serverProtos.json'
        clientProtoFile = 'clientProtos.json'

        clientContent = ""
        serverContent = ""


        protoKeys = self.structList.keys()
        protoKeys.sort()

        for messageName in protoKeys:
            content = Struct2String('message ' + messageName, self.structList[messageName])
            clientContent = clientContent + content + ",\n"
            serverContent = serverContent + content + ",\n"

        preClientContent = ""
        preServerContent = ""

        protoKeys = self.protoList.keys()
        protoKeys.sort()

        for protoName in protoKeys:
            content = Struct2String(protoName, self.protoList[protoName])

            preClientContent = clientContent + content
            clientContent = clientContent + content + ",\n"
        clientContent = preClientContent

        protoKeys = self.serverProtoList.keys()
        protoKeys.sort()

        for protoName in protoKeys:
            content = Struct2String(protoName, self.serverProtoList[protoName])
            preServerContent = serverContent + content
            serverContent = serverContent + content + ",\n"
        serverContent = preServerContent

        fileClient = open(clientProtoFile, 'w+')
        fileClient.write("{\n" + clientContent + "\n}")
        fileClient.close()

        serverClient = open(serverProtoFile, 'w+')
        serverClient.write("{\n" + serverContent + "\n}")
        serverClient.close()

    # 保存结构体配置文件
    def saveMessageCfg(self):
        messagePath = "message.ini"
        file = open(messagePath, 'w+')
        file.write("")
        file.close()

        mcf = MyConfig()
        mcf.read(messagePath)

        protoKeys = self.structList.keys()
        protoKeys.sort()

        for messageName in protoKeys:
            mcf.add_section(messageName)
            msgCfg = self.structList[messageName]
            mcf.set(messageName, "message", str(json.dumps(msgCfg)))

        mcf.write(open(messagePath, 'w+'))

    # 保存协议配置
    def saveProtos(self):
        self.saveProtoCfg()
        self.saveProtoCfg2()
        self.saveMessageCfg()
        self.exportProtoJson()

    # 添加协议
    def addProto(self, name):
        self.protoList[name] = {}
        self.displayProto(name,{})

    # 字段类型发生变化
    def paramTypeChanged(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamType(rowCount, ttype)

    # 值类型发生变化
    def valueTypeChanged(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamValueType(rowCount, ttype)

    # 显示协议参数
    def showProtoParam(self, protoCfg):
        self.isRefreshProto = True
        self.table_protoColum.clearContents()
        count = len(protoCfg)
        self.table_protoColum.setRowCount(count)
        for rowCount in protoCfg:
            cfg = protoCfg[rowCount]
            paramType = QtGui.QComboBox()
            paramType.setProperty('index', int(rowCount))
            paramType.addItems(paramTypeList)
            paramType.setCurrentIndex(paramType.findText(cfg['paramType']))
            self.table_protoColum.setCellWidget(int(rowCount), 0, paramType)

            paramName = QtGui.QTableWidgetItem(_fromUtf8(cfg['name']))
            self.table_protoColum.setItem(int(rowCount), 1, paramName)

            valueType = QtGui.QComboBox()
            valueType.setProperty('index', int(rowCount))
            valueType.addItems(self.getValueTypeList())
            valueType.setCurrentIndex(valueType.findText(cfg['valueType']))
            self.table_protoColum.setCellWidget(int(rowCount), 2, valueType)

            self.connect(paramType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.paramTypeChanged)
            self.connect(valueType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.valueTypeChanged)
        self.isRefreshProto = False

    # 展示协议字段信息和预览
    def displayProto(self, name, protoCfg):
        self.showProtoParam(protoCfg)
        self.preViewProto(name, protoCfg)

    # 预览结构体
    def preViewProto(self, name, protoCfg):
        previewContent = Struct2String(name, protoCfg)
        self.textEdit_2.setText(previewContent)

    # 获取结构体配置
    def getProto(self, protoName):
        if self.protoList.has_key(protoName):
            return self.protoList[protoName]

    # 更新结构体字段名字
    def updateProtoParamName(self, row):
        nameWidget = QtGui.QTableWidgetItem(self.table_protoColum.item(row, 1))
        name = str(nameWidget.text())

        if self.selectProtoName != None:
            cfg = self.getProto(self.selectProtoName)
            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())

            if cfg[row] != None:
                cfg[row]['name'] = name
            self.preViewProto(self.selectProtoName, cfg)

    # 更新结构体字段类型
    def updateProtoParamType(self, row, ttype):
        print("paramType :", row, str(ttype))
        if self.selectProtoName != None:
            cfg = self.getProto(self.selectProtoName)
            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())
            if cfg[row] != None:
                cfg[row]['paramType'] = str(ttype)
            self.preViewProto(self.selectProtoName, cfg)

    # 更新结构体值类型
    def updateProtoParamValueType(self, row, ttype):
        print("valueType :", row, str(ttype))
        if self.selectProtoName != None:
            cfg = self.getProto(self.selectProtoName)

            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())
            if cfg[row] != None:
                cfg[row]['valueType'] = str(ttype)

            self.preViewProto(self.selectProtoName, cfg)

    # -------------------------------------SIGNAL CALLBACK------------------------------------

    # 字段类型发生变化
    def messageParamTypeChanged(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamType(rowCount, ttype)

    # 值类型发生变化
    def messageValueTypeChanged(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamValueType(rowCount, ttype)

    # 添加协议字段
    def on_addProtoParam(self):
        if self.selectProtoName == None:
            return

        cfg = self.getProto(self.selectProtoName)
        if cfg == None:
            return
        rowCount = self.table_protoColum.rowCount()
        self.table_protoColum.setRowCount(int(rowCount) + 1)

        paramType = QtGui.QComboBox(self.table_protoColum)
        paramType.setProperty('index', int(rowCount))
        paramType.addItems(paramTypeList)
        self.table_protoColum.setCellWidget(int(rowCount), 0, paramType)

        paramName = QtGui.QTableWidgetItem(_fromUtf8("input param name"))
        self.table_protoColum.setItem(int(rowCount), 1, paramName)

        valueType = QtGui.QComboBox(self.table_protoColum)
        valueType.setProperty('index', int(rowCount))
        valueType.addItems(self.getValueTypeList())
        self.table_protoColum.setCellWidget(int(rowCount), 2, valueType)

        self.table_protoColum.editItem(paramName)

        strucCfg = self.getProto(self.selectProtoName)
        if strucCfg != None:
            if not strucCfg.has_key(rowCount):
                strucCfg.setdefault(rowCount, initParam())

        self.connect(paramType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.messageParamTypeChanged)
        self.connect(valueType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.messageValueTypeChanged)

    # 删除协议按钮点击回调
    def on_deleteProtoClicked(self):
        rowCount = self.list_proto.currentRow()
        if rowCount < 0:
            return
        nameWidget = QtGui.QTableWidgetItem(self.list_proto.item(rowCount, 0))
        protoName = str(nameWidget.text())
        del self.protoList[protoName]
        self.list_proto.removeRow(rowCount)

    # 删除协议字段回调
    def on_deleteProtoParamClicked(self):
        rowCount = self.table_protoColum.currentRow()
        if rowCount < 0:
            return

        self.table_protoColum.removeRow(rowCount)
        preLen = len(self.protoList[self.selectProtoName])
        del self.protoList[self.selectProtoName][rowCount]
        count = len(self.protoList[self.selectProtoName])
        if count == 0:
            self.table_protoColum.clearContents()
            self.displayProto(self.selectProtoName, self.protoList[self.selectProtoName])
            return

        if count - 1 >= rowCount:
            for i in range(rowCount, count):
                self.protoList[self.selectProtoName][i] = self.protoList[self.selectProtoName][i + 1]
        if self.protoList[self.selectProtoName].has_key(preLen - 1):
            del self.protoList[self.selectProtoName][preLen - 1]
        self.displayProto(self.selectProtoName, self.protoList[self.selectProtoName])

    # 添加协议按钮回调
    def on_addProtoClicked(self):
        self.selectProtoName = None
        newItem = QtGui.QTableWidgetItem(_fromUtf8("input proto name"))
        rowCount = self.list_proto.rowCount()
        self.list_proto.setRowCount(rowCount + 1)
        self.list_proto.setItem(rowCount, 0, newItem)
        self.list_proto.editItem(newItem)
        self.table_protoColum.clearContents()

    # 协议列表数据发生变化
    def on_currentProtoChanged(self, item):
        if self.ignoreListChange:
            return
        name = str(item.text())
        if name == None or name == 'input proto name':
            self.table_protoColum.clearContents()
            return

        preName = self.selectProtoName
        if None == preName or 'input proto name' == preName:
            self.selectProtoName = name
        else:
            if not self.protoList.has_key(name):
                self.protoList.setdefault(name, self.protoList[preName])
            else:
                self.protoList[name] = self.protoList[preName]
            self.selectProtoName = name
            del self.protoList[preName]

        if self.protoList.has_key(name):
            protoCfg = self.protoList[name]
            self.displayProto(name, protoCfg)
        else:
            self.addProto(name)

    # 协议项被点击
    def on_ProtoItemClicked(self, item):
        name = str(item.text())
        self.selectProtoName = name
        if self.protoList.has_key(name):
            protoCfg = self.protoList[name]
            self.displayProto(name, protoCfg)

    # 协议项被双击
    def on_ProtoItemDoubleClicked(self, item):
        print("on_ProtoItemDoubleClicked")

    # 结构体字段发生变化
    def on_protoParamChanged(self, row, colum):
        if self.isRefreshProto:
            return
        self.updateProtoParamName(row)
    #-----------------------------------服务端协议----------------------------------------
    # 添加协议
    def addProto2(self, name):
        self.serverProtoList[name] = {}
        self.displayProto2(name,{})

    # 字段类型发生变化
    def paramTypeChanged2(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamType2(rowCount, ttype)

    # 值类型发生变化
    def valueTypeChanged2(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamValueType2(rowCount, ttype)

    # 显示协议参数
    def showProtoParam2(self, protoCfg):
        self.isRefreshServerProto = True
        self.table_protoColum_2.clearContents()
        count = len(protoCfg)
        self.table_protoColum_2.setRowCount(count)
        for rowCount in protoCfg:
            cfg = protoCfg[rowCount]
            paramType = QtGui.QComboBox()
            paramType.setProperty('index', int(rowCount))
            paramType.addItems(paramTypeList)
            paramType.setCurrentIndex(paramType.findText(cfg['paramType']))
            self.table_protoColum_2.setCellWidget(int(rowCount), 0, paramType)

            paramName = QtGui.QTableWidgetItem(_fromUtf8(cfg['name']))
            self.table_protoColum_2.setItem(int(rowCount), 1, paramName)

            valueType = QtGui.QComboBox()
            valueType.setProperty('index', int(rowCount))
            valueType.addItems(self.getValueTypeList())
            valueType.setCurrentIndex(valueType.findText(cfg['valueType']))
            self.table_protoColum_2.setCellWidget(int(rowCount), 2, valueType)

            self.connect(paramType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.paramTypeChanged2)
            self.connect(valueType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.valueTypeChanged2)
        self.isRefreshServerProto = False

    # 展示协议字段信息和预览
    def displayProto2(self, name, protoCfg):
        self.showProtoParam2(protoCfg)
        self.preViewProto2(name, protoCfg)

    # 预览结构体
    def preViewProto2(self, name, protoCfg):
        previewContent = Struct2String(name, protoCfg)
        self.textEdit_3.setText(previewContent)

    # 获取结构体配置
    def getProto2(self, protoName):
        if self.serverProtoList.has_key(protoName):
            return self.serverProtoList[protoName]

    # 更新结构体字段名字
    def updateProtoParamName2(self, row):
        nameWidget = QtGui.QTableWidgetItem(self.table_protoColum_2.item(row, 1))
        name = str(nameWidget.text())

        if self.selectServerProtoName != None:
            cfg = self.getProto2(self.selectServerProtoName)
            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())

            if cfg[row] != None:
                cfg[row]['name'] = name
            self.preViewProto2(self.selectServerProtoName, cfg)

    # 更新结构体字段类型
    def updateProtoParamType2(self, row, ttype):
        print("paramType :", row, str(ttype))
        if self.selectServerProtoName != None:
            cfg = self.getProto2(self.selectServerProtoName)
            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())
            if cfg[row] != None:
                cfg[row]['paramType'] = str(ttype)
            self.preViewProto2(self.selectServerProtoName, cfg)

    # 更新结构体值类型
    def updateProtoParamValueType2(self, row, ttype):
        print("valueType :", row, str(ttype))
        if self.selectServerProtoName != None:
            cfg = self.getProto2(self.selectServerProtoName)

            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())
            if cfg[row] != None:
                cfg[row]['valueType'] = str(ttype)

            self.preViewProto2(self.selectServerProtoName, cfg)

    # -------------------------------------SIGNAL CALLBACK------------------------------------

    # 字段类型发生变化
    def messageParamTypeChanged2(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamType2(rowCount, ttype)

    # 值类型发生变化
    def messageValueTypeChanged2(self, ttype):
        rowCount = self.sender().property('index').toInt()[0]
        self.updateProtoParamValueType2(rowCount, ttype)

    # 添加协议字段
    def on_addProtoParam2(self):
        if self.selectServerProtoName == None:
            return

        cfg = self.getProto2(self.selectServerProtoName)
        if cfg == None:
            return
        rowCount = self.table_protoColum_2.rowCount()
        self.table_protoColum_2.setRowCount(int(rowCount) + 1)

        paramType = QtGui.QComboBox(self.table_protoColum_2)
        paramType.setProperty('index', int(rowCount))
        paramType.addItems(paramTypeList)
        self.table_protoColum_2.setCellWidget(int(rowCount), 0, paramType)

        paramName = QtGui.QTableWidgetItem(_fromUtf8("input param name"))
        self.table_protoColum_2.setItem(int(rowCount), 1, paramName)

        valueType = QtGui.QComboBox(self.table_protoColum_2)
        valueType.setProperty('index', int(rowCount))
        valueType.addItems(self.getValueTypeList())
        self.table_protoColum_2.setCellWidget(int(rowCount), 2, valueType)

        self.table_protoColum_2.editItem(paramName)

        strucCfg = self.getProto2(self.selectServerProtoName)
        if strucCfg != None:
            if not strucCfg.has_key(rowCount):
                strucCfg.setdefault(rowCount, initParam())

        self.connect(paramType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.messageParamTypeChanged2)
        self.connect(valueType, QtCore.SIGNAL('currentIndexChanged(QString)'), self.messageValueTypeChanged2)

    # 删除协议按钮点击回调
    def on_deleteProtoClicked2(self):
        rowCount = self.list_proto_2.currentRow()
        if rowCount < 0:
            return
        nameWidget = QtGui.QTableWidgetItem(self.list_proto_2.item(rowCount, 0))
        protoName = str(nameWidget.text())
        del self.serverProtoList[protoName]
        self.list_proto_2.removeRow(rowCount)

    # 删除协议字段回调
    def on_deleteProtoParamClicked2(self):
        rowCount = self.table_protoColum_2.currentRow()
        if rowCount < 0:
            return

        self.table_protoColum_2.removeRow(rowCount)
        preLen = len(self.serverProtoList[self.selectServerProtoName])
        del self.serverProtoList[self.selectServerProtoName][rowCount]
        count = len(self.serverProtoList[self.selectServerProtoName])
        if count == 0:
            self.table_protoColum_2.clearContents()
            self.displayProto2(self.selectServerProtoName, self.serverProtoList[self.selectServerProtoName])
            return

        if count - 1 >= rowCount:
            for i in range(rowCount, count):
                self.serverProtoList[self.selectServerProtoName][i] = self.serverProtoList[self.selectServerProtoName][i + 1]
        if self.serverProtoList[self.selectServerProtoName].has_key(preLen - 1):
            del self.serverProtoList[self.selectServerProtoName][preLen - 1]
        self.displayProto2(self.selectServerProtoName, self.serverProtoList[self.selectServerProtoName])

    # 添加协议按钮回调
    def on_addProtoClicked2(self):
        self.selectServerProtoName = None
        newItem = QtGui.QTableWidgetItem(_fromUtf8("input proto name"))
        rowCount = self.list_proto_2.rowCount()
        self.list_proto_2.setRowCount(rowCount + 1)
        self.list_proto_2.setItem(rowCount, 0, newItem)
        self.list_proto_2.editItem(newItem)
        self.table_protoColum_2.clearContents()

    # 协议列表数据发生变化
    def on_currentProtoChanged2(self, item):
        if self.ignoreListChange:
            return
        name = str(item.text())
        if name == None or name == 'input proto name':
            self.table_protoColum_2.clearContents()
            return

        preName = self.selectServerProtoName
        if None == preName or 'input proto name' == preName:
            self.selectServerProtoName = name
        else:
            if not self.serverProtoList.has_key(name):
                self.serverProtoList.setdefault(name, self.serverProtoList[preName])
            else:
                self.serverProtoList[name] = self.serverProtoList[preName]
            self.selectServerProtoName = name
            del self.serverProtoList[preName]

        if self.serverProtoList.has_key(name):
            protoCfg = self.serverProtoList[name]
            self.displayProto2(name, protoCfg)
        else:
            self.addProto2(name)

    # 协议项被点击
    def on_ProtoItemClicked2(self, item):
        name = str(item.text())
        self.selectServerProtoName = name
        if self.serverProtoList.has_key(name):
            protoCfg = self.serverProtoList[name]
            self.displayProto2(name, protoCfg)

    # 协议项被双击
    def on_ProtoItemDoubleClicked2(self, item):
        print("on_ProtoItemDoubleClicked")

    # 结构体字段发生变化
    def on_protoParamChanged2(self, row, colum):
        if self.isRefreshServerProto:
            return
        self.updateProtoParamName2(row)

    # ---------------------------------------------------------------------------
    # ---------------------------结构体------------------------------------------
    # ---------------------------------------------------------------------------

    # 加载结构体配置
    def loadStructs(self):
        iniPath = "message.ini"
        cf = MyConfig()
        cf.read(iniPath)
        secList = cf.sections()
        for messageName in secList:
            jsonstr = cf.get(messageName, "message")
            dic = json.loads(str(jsonstr))
            message = {}
            for key in dic:
                message.setdefault(int(key), dic[key])

            self.structList.setdefault(str(messageName), message)

        self.list_struct.setRowCount(len(self.structList))
        curIdx = 0
        for messageName in self.structList:
            newItem = QtGui.QTableWidgetItem(_fromUtf8(messageName))
            self.list_struct.setItem(curIdx, 0, newItem)
            curIdx = curIdx + 1

    # 添加结构体
    def addStruct(self, name):
        self.structList[name] = {}
        self.displayStruct(name,{})

    # 显示结构体参数
    def showStructParam(self, structCfg):
        self.isRefreshMessage = True
        self.table_structColum.clearContents()
        count = len(structCfg)
        self.table_structColum.setRowCount(count)
        for rowCount in structCfg:
            cfg = structCfg[rowCount]
            paramType = QtGui.QComboBox(self.table_structColum)
            paramType.addItems(paramTypeList)
            paramType.setCurrentIndex(paramType.findText(_fromUtf8(cfg['paramType'])))
            self.table_structColum.setCellWidget(int(rowCount), 0, paramType)

            paramName = QtGui.QTableWidgetItem(_fromUtf8(cfg['name']))
            self.table_structColum.setItem(int(rowCount), 1, paramName)

            valueType = QtGui.QComboBox(self.table_structColum)

            valueType.addItems(self.getValueTypeList())
            valueType.setCurrentIndex(valueType.findText(cfg['valueType']))
            self.table_structColum.setCellWidget(int(rowCount), 2, valueType)

            # 字段类型发生变化
            def paramTypeChanged(ttype):
                self.updateStructParamType(rowCount, ttype)

            # 值类型发生变化
            def valueTypeChanged(ttype):
                self.updateStructParamValueType(rowCount, ttype)

            self.connect(paramType, QtCore.SIGNAL('currentIndexChanged(QString)'), paramTypeChanged)
            self.connect(valueType, QtCore.SIGNAL('currentIndexChanged(QString)'), valueTypeChanged)
        self.isRefreshMessage = False

    # 展示结构体段信息和预览
    def displayStruct(self, name, structCfg):
        self.showStructParam(structCfg)
        self.preViewStruct(name, structCfg)

    # 预览结构体
    def preViewStruct(self, name, structCfg):
        previewContent = Struct2String(name, structCfg)
        # self.label_3.setText(previewContent)
        self.textEdit.setText(previewContent)

    # 获取结构体配置
    def getStruct(self, structName):
        if self.structList.has_key(structName):
            return self.structList[structName]

    # 更新结构体字段名字
    def updateStructParamName(self, row):
        nameWidget = QtGui.QTableWidgetItem(self.table_structColum.item(row, 1))
        name = str(nameWidget.text())

        if self.selectStructName != None:
            cfg = self.getStruct(self.selectStructName)
            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())

            if cfg[row] != None:
                cfg[row]['name'] = name
            self.preViewStruct(self.selectStructName, cfg)

    # 更新结构体字段类型
    def updateStructParamType(self, row, ttype):
        print("paramType :", str(ttype))
        if self.selectStructName != None:
            cfg = self.getStruct(self.selectStructName)

            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())
            if cfg[row] != None:
                cfg[row]['paramType'] = str(ttype)
            self.preViewStruct(self.selectStructName, cfg)

    # 更新结构体值类型
    def updateStructParamValueType(self, row, ttype):
        print("valueType :", str(ttype))
        if self.selectStructName != None:
            cfg = self.getStruct(self.selectStructName)

            if not cfg.has_key(row):
                cfg.setdefault(row, initParam())
            if cfg[row] != None:
                cfg[row]['valueType'] = str(ttype)

            self.preViewStruct(self.selectStructName, cfg)

    # -------------------------------------SIGNAL CALLBACK------------------------------------
    # 删除协议按钮点击回调
    def on_deleteStructClicked(self):
        rowCount = self.list_struct.currentRow()
        if rowCount < 0:
            return
        nameWidget = QtGui.QTableWidgetItem(self.list_struct.item(rowCount, 0))
        structName = str(nameWidget.text())
        del self.structList[structName]
        self.list_struct.removeRow(rowCount)

    # 删除协议字段回调
    def on_deleteStructParamClicked(self):
        rowCount = self.table_structColum.currentRow()
        if rowCount < 0:
            return

        self.table_structColum.removeRow(rowCount)
        preLen = len(self.structList[self.selectStructName])
        del self.structList[self.selectStructName][rowCount]
        count = len(self.structList[self.selectStructName])
        if count == 0:
            self.table_structColum.clearContents()
            self.displayStruct(self.selectStructName, self.structList[self.selectStructName])
            return

        if count - 1 >= rowCount:
            for i in range(rowCount, count):
                self.structList[self.selectStructName][i] = self.structList[self.selectStructName][i + 1]
        if self.structList[self.selectStructName].has_key(preLen - 1):
            del self.structList[self.selectStructName][preLen - 1]
        self.displayStruct(self.selectStructName, self.structList[self.selectStructName])

    # 添加结构体字段
    def on_addStructParam(self):
        if self.selectStructName == None:
            return

        cfg = self.getStruct(self.selectStructName)
        if cfg == None:
            return
        rowCount = self.table_structColum.rowCount()
        self.table_structColum.setRowCount(rowCount + 1)

        paramType = QtGui.QComboBox(self.table_structColum)
        paramType.addItems(paramTypeList)
        self.table_structColum.setCellWidget(rowCount, 0, paramType)

        paramName = QtGui.QTableWidgetItem(_fromUtf8("input param name"))
        self.table_structColum.setItem(rowCount, 1, paramName)

        valueType = QtGui.QComboBox(self.table_structColum)
        valueType.addItems(self.getValueTypeList())
        self.table_structColum.setCellWidget(rowCount, 2, valueType)

        self.table_structColum.editItem(paramName)

        strucCfg = self.getStruct(self.selectStructName)
        if strucCfg != None:
            if not strucCfg.has_key(rowCount):
                strucCfg.setdefault(rowCount, initParam())

        # 字段类型发生变化
        def paramTypeChanged(ttype):
            self.updateStructParamType(rowCount, ttype)

        # 值类型发生变化
        def valueTypeChanged(ttype):
            self.updateStructParamValueType(rowCount, ttype)

        self.connect(paramType, QtCore.SIGNAL('currentIndexChanged(QString)'), paramTypeChanged)
        self.connect(valueType, QtCore.SIGNAL('currentIndexChanged(QString)'), valueTypeChanged)

    # 添加结构体按钮回调
    def on_addStructClicked(self):
        self.selectStructName = None
        newItem = QtGui.QTableWidgetItem(_fromUtf8("input struct name"))
        rowCount = self.list_struct.rowCount()
        self.list_struct.setRowCount(rowCount + 1)
        self.list_struct.setItem(rowCount, 0, newItem)
        self.list_struct.editItem(newItem)
        self.table_structColum.clearContents()

    # 结构体列表数据发生变化
    def on_currentStructChanged(self, item):
        if self.ignoreListChange:
            return
        name = str(item.text())
        if name == None or name == 'input struct name':
            self.table_structColum.clearContents()
            return

        preName = self.selectStructName
        if None == preName or 'input struct name' == preName:
            self.selectStructName = name
        else:
            if not self.structList.has_key(name):
                self.structList.setdefault(name, self.structList[preName])
            else:
                self.structList[name] = self.structList[preName]
            self.selectStructName = name
            del self.structList[preName]

        if self.structList.has_key(name):
            structCfg = self.structList[name]
            self.displayStruct(name, structCfg)
        else:
            self.addStruct(name)

    # 结构体项被点击
    def on_StructItemClicked(self, item):
        name = str(item.text())
        self.selectStructName = name
        if self.structList.has_key(name):
            structCfg = self.structList[name]
            self.displayStruct(name, structCfg)

    # 结构体被双击
    def on_StructItemDoubleClicked(self, item):
        print("on_StructItemDoubleClicked")

    # 结构体字段发生变化
    def on_structParamChanged(self, row, colum):
        if self.isRefreshMessage:
            return
        self.updateStructParamName(row)


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()

    app.exec_()


if __name__ == '__main__':
    main()
