# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorMainPanel.ui'
#
# Created: Wed Aug 08 17:14:08 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EditorMainPanel(object):
    def setupUi(self, EditorMainPanel):
        EditorMainPanel.setObjectName(_fromUtf8("EditorMainPanel"))
        EditorMainPanel.resize(800, 700)
        EditorMainPanel.setMinimumSize(QtCore.QSize(800, 700))
        EditorMainPanel.setMaximumSize(QtCore.QSize(800, 700))
        EditorMainPanel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget = QtGui.QTabWidget(EditorMainPanel)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 671))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.list_proto = QtGui.QTableWidget(self.tab)
        self.list_proto.setGeometry(QtCore.QRect(0, 0, 341, 571))
        self.list_proto.setObjectName(_fromUtf8("list_proto"))
        self.list_proto.setColumnCount(1)
        self.list_proto.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.list_proto.setHorizontalHeaderItem(0, item)
        self.list_proto.verticalHeader().setVisible(False)
        self.btn_addProto = QtGui.QPushButton(self.tab)
        self.btn_addProto.setGeometry(QtCore.QRect(0, 590, 75, 41))
        self.btn_addProto.setObjectName(_fromUtf8("btn_addProto"))
        self.btn_deleteProto = QtGui.QPushButton(self.tab)
        self.btn_deleteProto.setGeometry(QtCore.QRect(266, 590, 75, 41))
        self.btn_deleteProto.setObjectName(_fromUtf8("btn_deleteProto"))
        self.table_protoColum = QtGui.QTableWidget(self.tab)
        self.table_protoColum.setGeometry(QtCore.QRect(350, 0, 421, 311))
        self.table_protoColum.setWordWrap(False)
        self.table_protoColum.setObjectName(_fromUtf8("table_protoColum"))
        self.table_protoColum.setColumnCount(3)
        self.table_protoColum.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_protoColum.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_protoColum.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_protoColum.setHorizontalHeaderItem(2, item)
        self.table_protoColum.horizontalHeader().setCascadingSectionResizes(False)
        self.table_protoColum.horizontalHeader().setDefaultSectionSize(100)
        self.table_protoColum.horizontalHeader().setMinimumSectionSize(100)
        self.table_protoColum.verticalHeader().setVisible(False)
        self.table_protoColum.verticalHeader().setCascadingSectionResizes(False)
        self.table_protoColum.verticalHeader().setMinimumSectionSize(20)
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(350, 320, 421, 251))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_2 = QtGui.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 40, 401, 201))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.btn_deleteColum = QtGui.QPushButton(self.tab)
        self.btn_deleteColum.setGeometry(QtCore.QRect(700, 590, 72, 41))
        self.btn_deleteColum.setObjectName(_fromUtf8("btn_deleteColum"))
        self.btn_addColum = QtGui.QPushButton(self.tab)
        self.btn_addColum.setGeometry(QtCore.QRect(350, 590, 72, 41))
        self.btn_addColum.setObjectName(_fromUtf8("btn_addColum"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.frame_4 = QtGui.QFrame(self.tab_3)
        self.frame_4.setGeometry(QtCore.QRect(350, 320, 421, 251))
        self.frame_4.setFrameShape(QtGui.QFrame.Box)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_4 = QtGui.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtGui.QFrame.Box)
        self.label_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit_3 = QtGui.QTextEdit(self.frame_4)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 40, 401, 201))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.btn_deleteProto_2 = QtGui.QPushButton(self.tab_3)
        self.btn_deleteProto_2.setGeometry(QtCore.QRect(266, 590, 75, 41))
        self.btn_deleteProto_2.setObjectName(_fromUtf8("btn_deleteProto_2"))
        self.table_protoColum_2 = QtGui.QTableWidget(self.tab_3)
        self.table_protoColum_2.setGeometry(QtCore.QRect(350, 0, 421, 311))
        self.table_protoColum_2.setWordWrap(False)
        self.table_protoColum_2.setObjectName(_fromUtf8("table_protoColum_2"))
        self.table_protoColum_2.setColumnCount(3)
        self.table_protoColum_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_protoColum_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_protoColum_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_protoColum_2.setHorizontalHeaderItem(2, item)
        self.table_protoColum_2.horizontalHeader().setCascadingSectionResizes(False)
        self.table_protoColum_2.horizontalHeader().setDefaultSectionSize(100)
        self.table_protoColum_2.horizontalHeader().setMinimumSectionSize(100)
        self.table_protoColum_2.verticalHeader().setVisible(False)
        self.table_protoColum_2.verticalHeader().setCascadingSectionResizes(False)
        self.table_protoColum_2.verticalHeader().setMinimumSectionSize(20)
        self.list_proto_2 = QtGui.QTableWidget(self.tab_3)
        self.list_proto_2.setGeometry(QtCore.QRect(0, 0, 341, 571))
        self.list_proto_2.setObjectName(_fromUtf8("list_proto_2"))
        self.list_proto_2.setColumnCount(1)
        self.list_proto_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.list_proto_2.setHorizontalHeaderItem(0, item)
        self.list_proto_2.verticalHeader().setVisible(False)
        self.btn_addProto_2 = QtGui.QPushButton(self.tab_3)
        self.btn_addProto_2.setGeometry(QtCore.QRect(0, 590, 75, 41))
        self.btn_addProto_2.setObjectName(_fromUtf8("btn_addProto_2"))
        self.btn_deleteColum_3 = QtGui.QPushButton(self.tab_3)
        self.btn_deleteColum_3.setGeometry(QtCore.QRect(700, 590, 72, 41))
        self.btn_deleteColum_3.setObjectName(_fromUtf8("btn_deleteColum_3"))
        self.btn_addColum_3 = QtGui.QPushButton(self.tab_3)
        self.btn_addColum_3.setGeometry(QtCore.QRect(350, 590, 72, 41))
        self.btn_addColum_3.setObjectName(_fromUtf8("btn_addColum_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.btn_deletestruct = QtGui.QPushButton(self.tab_2)
        self.btn_deletestruct.setGeometry(QtCore.QRect(266, 590, 75, 41))
        self.btn_deletestruct.setObjectName(_fromUtf8("btn_deletestruct"))
        self.table_structColum = QtGui.QTableWidget(self.tab_2)
        self.table_structColum.setGeometry(QtCore.QRect(350, 0, 421, 311))
        self.table_structColum.setWordWrap(False)
        self.table_structColum.setObjectName(_fromUtf8("table_structColum"))
        self.table_structColum.setColumnCount(3)
        self.table_structColum.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_structColum.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_structColum.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_structColum.setHorizontalHeaderItem(2, item)
        self.table_structColum.horizontalHeader().setCascadingSectionResizes(False)
        self.table_structColum.horizontalHeader().setDefaultSectionSize(100)
        self.table_structColum.horizontalHeader().setMinimumSectionSize(100)
        self.table_structColum.verticalHeader().setVisible(False)
        self.table_structColum.verticalHeader().setCascadingSectionResizes(False)
        self.table_structColum.verticalHeader().setMinimumSectionSize(20)
        self.list_struct = QtGui.QTableWidget(self.tab_2)
        self.list_struct.setGeometry(QtCore.QRect(0, 0, 341, 571))
        self.list_struct.setObjectName(_fromUtf8("list_struct"))
        self.list_struct.setColumnCount(1)
        self.list_struct.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.list_struct.setHorizontalHeaderItem(0, item)
        self.list_struct.horizontalHeader().setCascadingSectionResizes(False)
        self.list_struct.horizontalHeader().setHighlightSections(True)
        self.list_struct.verticalHeader().setVisible(False)
        self.btn_addstruct = QtGui.QPushButton(self.tab_2)
        self.btn_addstruct.setGeometry(QtCore.QRect(0, 590, 75, 41))
        self.btn_addstruct.setObjectName(_fromUtf8("btn_addstruct"))
        self.btn_addColum_2 = QtGui.QPushButton(self.tab_2)
        self.btn_addColum_2.setGeometry(QtCore.QRect(350, 590, 72, 41))
        self.btn_addColum_2.setObjectName(_fromUtf8("btn_addColum_2"))
        self.frame_3 = QtGui.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(350, 320, 421, 251))
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.Box)
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 401, 201))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit = QtGui.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 401, 201))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.btn_deleteColum_2 = QtGui.QPushButton(self.tab_2)
        self.btn_deleteColum_2.setGeometry(QtCore.QRect(700, 590, 72, 41))
        self.btn_deleteColum_2.setObjectName(_fromUtf8("btn_deleteColum_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.lineEdit = QtGui.QLineEdit(EditorMainPanel)
        self.lineEdit.setGeometry(QtCore.QRect(100, 610, 171, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(EditorMainPanel)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(EditorMainPanel)

    def retranslateUi(self, EditorMainPanel):
        EditorMainPanel.setWindowTitle(_translate("EditorMainPanel", "协议编辑器", None))
        self.list_proto.setSortingEnabled(True)
        item = self.list_proto.horizontalHeaderItem(0)
        item.setText(_translate("EditorMainPanel", "协议名称", None))
        self.btn_addProto.setText(_translate("EditorMainPanel", "添加协议", None))
        self.btn_deleteProto.setText(_translate("EditorMainPanel", "删除协议", None))
        item = self.table_protoColum.horizontalHeaderItem(0)
        item.setText(_translate("EditorMainPanel", "字段类型", None))
        item = self.table_protoColum.horizontalHeaderItem(1)
        item.setText(_translate("EditorMainPanel", "字段名", None))
        item = self.table_protoColum.horizontalHeaderItem(2)
        item.setText(_translate("EditorMainPanel", "值类型", None))
        self.label.setText(_translate("EditorMainPanel", "协议预览", None))
        self.btn_deleteColum.setText(_translate("EditorMainPanel", "删除字段", None))
        self.btn_addColum.setText(_translate("EditorMainPanel", "添加字段", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("EditorMainPanel", "客户端协议", None))
        self.label_4.setText(_translate("EditorMainPanel", "协议预览", None))
        self.btn_deleteProto_2.setText(_translate("EditorMainPanel", "删除协议", None))
        item = self.table_protoColum_2.horizontalHeaderItem(0)
        item.setText(_translate("EditorMainPanel", "字段类型", None))
        item = self.table_protoColum_2.horizontalHeaderItem(1)
        item.setText(_translate("EditorMainPanel", "字段名", None))
        item = self.table_protoColum_2.horizontalHeaderItem(2)
        item.setText(_translate("EditorMainPanel", "值类型", None))
        self.list_proto_2.setSortingEnabled(True)
        item = self.list_proto_2.horizontalHeaderItem(0)
        item.setText(_translate("EditorMainPanel", "协议名称", None))
        self.btn_addProto_2.setText(_translate("EditorMainPanel", "添加协议", None))
        self.btn_deleteColum_3.setText(_translate("EditorMainPanel", "删除字段", None))
        self.btn_addColum_3.setText(_translate("EditorMainPanel", "添加字段", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("EditorMainPanel", "服务端协议", None))
        self.btn_deletestruct.setText(_translate("EditorMainPanel", "删除结构体", None))
        item = self.table_structColum.horizontalHeaderItem(0)
        item.setText(_translate("EditorMainPanel", "字段类型", None))
        item = self.table_structColum.horizontalHeaderItem(1)
        item.setText(_translate("EditorMainPanel", "字段名", None))
        item = self.table_structColum.horizontalHeaderItem(2)
        item.setText(_translate("EditorMainPanel", "值类型", None))
        self.list_struct.setSortingEnabled(True)
        item = self.list_struct.horizontalHeaderItem(0)
        item.setText(_translate("EditorMainPanel", "结构体名称", None))
        self.btn_addstruct.setText(_translate("EditorMainPanel", "添加结构体", None))
        self.btn_addColum_2.setText(_translate("EditorMainPanel", "添加字段", None))
        self.label_2.setText(_translate("EditorMainPanel", "结构体预览:", None))
        self.btn_deleteColum_2.setText(_translate("EditorMainPanel", "删除字段", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("EditorMainPanel", "结构体", None))

