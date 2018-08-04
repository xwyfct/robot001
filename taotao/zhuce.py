# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuce.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_registor(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_registor,self).__init__()
        self.setObjectName("self")
        self.resize(504,215)
        self.setMinimumSize(QtCore.QSize(504,0))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(71, 51, 53, 23))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(130, 51, 146, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 84, 146, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(71, 84, 38, 23))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(282,117, 85, 33))
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(71, 117, 45, 23))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 120, 146, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)#不允许复制粘贴
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)#不允许复制粘贴
        self.lineEdit_2.setPlaceholderText("6-15位的数字和字母")#只接收１５位以内的
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)#设置成密码模式，也就是输入内容显示为实心的圆
        regx = QRegExp("[0-9A-Za-z]{15}$") #密码匹配规则  长度不能超过15位
        validator = QRegExpValidator(regx, self.lineEdit_2)#构造验证器
        self.lineEdit_2.setValidator(validator)
        regx1 = QRegExp("\S{100}$") #用户名不能有空格
        validator1 = QRegExpValidator(regx1, self.lineEdit)
        validator1 = QRegExpValidator(regx1, self.lineEdit_3)
        self.lineEdit.setValidator(validator1)
        self.lineEdit_3.setValidator(validator1)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)#设置成普通模式（默认）
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)#设置成普通模式（默认）
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(130, 160, 141, 20))
        self.label_10.setObjectName("label_4")
        # self.label_4.setText("密码输入错误")
        self.label_10.setStyleSheet("color: rgb(255, 0, 0);")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.center()
        
    def center(self):
        #居中显示模块
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def retranslateUi(self):
        # _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle( "Form")
        self.label.setText("用户名 :")
        self.label_2.setText( "密码 :")
        self.pushButton_3.setText( "注册")
        self.label_3.setText( "昵称：")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    icon = Ui_registor()
    icon.show()
    sys.exit(app.exec_())