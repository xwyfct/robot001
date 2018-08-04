# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from untitled2 import Ui_MainWindow   #导入该对象所在文件
# Ui_MainWindow = untitled2.Ui_MainWindow
#指定Ui_MainWindow 为untitled2文件下的Ui_MainWindow对象。
# from tcp_connect import App
from zhuce import Ui_registor
from lianxi3 import Ui_self
from tcp_connect import *
class Icon(QtWidgets.QWidget,App):
    def __init__(self,sock, parent=None):
        self.sock = sock
        super().__init__(sock=sock)#父类　　由过程式改为面向对象
        self.setupUi()
        
        


    def setupUi(self):
        self.setWindowIcon(QIcon("/home/tarena/桌面/淘淘/jiqi4.jpg")) #图标
        self.setObjectName("self")
        self.resize(589, 488)
        self.setFixedWidth(589)
        self.setFixedHeight(488)
        self.setMinimumSize(QtCore.QSize(504, 0))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(220, 311, 53, 23))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(278, 388, 150, 28))
        # self.checkBox.setChecked(False)
        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect( lambda:self.btnstate(self.checkBox) )
        # layout.addWidget(self.checkBox)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(279, 314, 146, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(279, 353, 146, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)#不允许复制粘贴
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)#不允许复制粘贴
        self.lineEdit_2.setPlaceholderText("6-15位的数字和字母")#只接收１５位以内的
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)#设置成密码模式，也就是输入内容显示为实心的圆
        regx = QRegExp("[0-9A-Za-z]{15}$") #密码匹配规则  长度不能超过15位
        validator = QRegExpValidator(regx, self.lineEdit_2)#构造验证器
        self.lineEdit_2.setValidator(validator)
        regx1 = QRegExp("\S{100}$") #用户名不能有空格
        validator1 = QRegExpValidator(regx1, self.lineEdit)
        self.lineEdit.setValidator(validator1)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)#设置成普通模式（默认）
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(220, 350, 38, 23))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(431, 311, 85, 33))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(431, 350, 85, 33))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFlat(True) #按钮透明
        self.pushButton_3.setFlat(True)
        # 按钮绑定图片 self.pushButton_4.setIcon(QIcon("桌面/淘淘/image/u=2175952382,3079738696&fm=27&gp=0.jpg"))
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(315, 431, 81, 33))
        self.pushButton.setStyleSheet("background-color: rgb(213, 241, 255);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(419, 431, 81, 33))
        self.pushButton_2.setStyleSheet("background-color: rgb(213, 241, 255);")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(-19, -9, 621, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/tarena/桌面/淘淘/image/u=2175952382,3079738696&fm=27&gp=0.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 111, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/home/tarena/桌面/淘淘/image/jiqi4.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(180, 430, 111, 21))
        self.label_5.setObjectName("label_5")
        # self.label_5.setText("密码输入错误")
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 621, 531))
        self.widget.setStyleSheet("background-color: rgb(143,225,246);")
        self.widget.setObjectName("widget")
        self.pushButton.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.checkBox.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlags(Qt.CustomizeWindowHint)  #无标题栏
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.self)#登录按钮绑定二级界面
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_3.clicked.connect(self.registor)
        self.center()
        f = open('记住密码文档.txt','r')
        a=f.readline()
        L=a.split(" ")
        self.lineEdit.setText(L[0])
        self.lineEdit_2.setText(L[1])
        
    def btnstate(self,btn):
        chk1Status = self.checkBox.text()+", isChecked="+  str( self.checkBox.isChecked() ) + ', chekState=' + str(self.checkBox.checkState())   +"\n"        
        print(self.checkBox.isChecked())
    def center(self):
        #居中显示模块
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def self(self):
        user=self.lineEdit.text()#返回用户名
        password=self.lineEdit_2.text()#返回密码
        print(user,password)
        msg1=self.login(user,password)
        L1 = msg1.split(" ")
        #密码登录规则
        if L1[0]== '登录成功':
            print('成功')
            self.liaotian = Ui_self(self.sock)
            self.liaotian.show()
            self.liaotian.nicheng = L1[1]
            self.liaotian.pushButton_6.clicked.connect(self.fasong)

           
                    


            if self.checkBox.isChecked():
                f = open('记住密码文档.txt','w',encoding='utf-8')
                a = user+" "+password
                f.write(a)
                f.close()
            else:
                f.write("")
            print(user,password)
            icon.close() #登陆后关闭一级界面
        elif msg1 == '密码有误': 
            self.label_5.setText('账号或密码不正确,请从新输入')
        elif msg1 == '用户不存在,请先注册':
            self.label_5.setText('账号不存在,请先注册')




    def registor(self):
        self.regi = Ui_registor()
        self.regi.show()
        self.regi.pushButton_3.clicked.connect(self.zhuce)
        print("进入注册界面")
    def zhuce(self):
        
        user=self.regi.lineEdit.text()#返回用户名
        password=self.regi.lineEdit_2.text()#返回密码
        userid = self.regi.lineEdit_3.text()#返回昵称
        msg2=self.register(user,password,userid)
        if msg2 == 'Y':
            print('注册成功')
            f = open('昵称.txt','a',encoding='utf-8')
            a = user + " "+ userid
            f.write(a)
            f.close()
            self.regi.close()

        else:
            print('注册失败')
            self.label_10.setText("密码输入错误")

        
    def retranslateUi(self):
        
        self.setWindowTitle( "Form")
        self.label.setText( "用户名 :")
        self.checkBox.setText( "记住用户名和密码")
        self.label_2.setText("密码 :")
        self.pushButton_3.setText( "注册")
        self.pushButton_4.setText("找回密码")
        self.pushButton.setText( "登录")
        self.pushButton_2.setText("退出")
        

    def fasong(self):
        pass
# class LoadingGifWin( QWidget):
#     def __init__(self,parent=None):
#         super(LoadingGifWin, self).__init__(parent)
#         self.label =  QLabel('', self)
#         self.setFixedSize(128,128)
#         self.setWindowFlags( Qt.Dialog| Qt.CustomizeWindowHint)
#         self.movie =  QMovie("./images/loading.gif")
#         self.label.setMovie(self.movie)
#         self.movie.start()
# class Ui_nihao(QtWidgets.QWidget):
#     def __init__(self):
#         super(Ui_nihao,self).__init__()
#         self.setObjectName("nihao")
#         self.resize(400, 300)
#         self.setWindowTitle("消息")
#         self.label = QtWidgets.QLabel(self)
#         self.label.setGeometry(QtCore.QRect(100, 80, 181, 91))
#         font = QtGui.QFont()
#         font.setPointSize(55)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.label.setText("你好！")
#         Icon.center(self)

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8888
    sock = socket(AF_INET,SOCK_STREAM,0)
    sock.connect((host,port))
    print("连接服务端")
    app = QtWidgets.QApplication(sys.argv)
    icon = Icon(sock)
    icon.show()
    sys.exit(app.exec_())
