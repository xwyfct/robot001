from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import QSize
import sys
import requests
from PIL import Image
from  io import BytesIO
from tcp_connect import *
import re
# from ppp import *

class Ui_self(QtWidgets.QWidget,App):
    def __init__(self,sock=None):
        # host = '127.0.0.1'
        # port = 8888
        # sock = socket(AF_INET,SOCK_STREAM,0)
        # sock.connect((host,port))
        super(Ui_self,self).__init__(sock=sock)

        
        self.setObjectName("self")
        self.resize(968, 843)
        self.setWindowIcon(QIcon("/home/tarena/桌面/淘淘/jiqi4.jpg"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.623762 rgba(38, 197, 253, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 9)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 2, 7)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/tarena/桌面/淘淘/image/20.png"))

        self.label_2.setObjectName("label_2")
        self.label.setFixedHeight(40)
        self.label_2.setFixedWidth(90)

        self.gridLayout.addWidget(self.label_2, 1, 7, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 7, 3, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 5, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 6, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 0, 2, 7)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 7, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 5, 8, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.textBrowser.setOpenExternalLinks(True)
        # self.textBrowser.setText("<a href=\"http://blog.csdn.net/fron_csl\">linkLabelTest")
        #按钮透明
        self.pushButton.setFlat(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_3.setFlat(True)
        self.pushButton_4.setFlat(True)
        self.pushButton_5.setFlat(True)
        self.pushButton_8.setFlat(True)
        self.pushButton_9.setFlat(True)
        #按钮绑定图片
        self.pushButton.setIcon(QIcon("/home/tarena/桌面/淘淘/image/font1.png"))
        self.pushButton_2.setIcon(QIcon("/home/tarena/桌面/淘淘/image/font2.png"))
        self.pushButton_3.setIcon(QIcon("/home/tarena/桌面/淘淘/image/font3.png"))
        self.pushButton_4.setIcon(QIcon("/home/tarena/桌面/淘淘/image/font4.png"))
        self.pushButton_5.setIcon(QIcon("/home/tarena/桌面/淘淘/image/font5.png"))
        self.pushButton_8.setIcon(QIcon("/home/tarena/桌面/淘淘/image/font6.png"))
        self.pushButton_9.setIcon(QIcon("/home/tarena/桌面/淘淘/image/font7.png"))
        self.setWindowTitle("self")
        self.pushButton_6.setText("发送")
        self.pushButton_7.setText("清除")
        QtCore.QMetaObject.connectSlotsByName(self)
        #按钮绑定事件实现功能　　　　信号槽
        self.pushButton.clicked.connect(self.showDialog)
        self.pushButton_2.clicked.connect(self.choicecolor)
        self.pushButton_3.clicked.connect(self.openfile)
        self.pushButton_4.clicked.connect(self.robot)
        self.pushButton_5.clicked.connect(self.getfile)
        self.pushButton_8.clicked.connect(self.cart)
        self.pushButton_9.clicked.connect(self.pain)
        self.pushButton_6.clicked.connect(self.pushButton6)
        self.pushButton_7.clicked.connect(self.textEdit.clear)
        self.center()
        self.font_family="Ubuntu"
        self.font_pointSize = "15"
        self.col = "black"
        self.font_bold = 0 
        self.font_italic = 0
        # 背景平铺
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background,QBrush(QPixmap("/home/tarena/桌面/淘淘/image/timg.jpg")))
        self.setPalette(self.palette)   
        
    #确认关闭对话框
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are you sure to quit?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.user_exit()
            event.accept()


        else:
            event.ignore()
    #改变字体
    def showDialog(self):
        font, ok = QFontDialog.getFont()#getFont方法返回字体名字和布尔值，如果用户点击了ok，布尔值为true；否则为false。
        if ok:
            self.font_family = font.family()
            self.font_pointSize = font.pointSize()
            self.font_bold = font.bold()
            self.font_italic = font.italic()
            print(self.font_family)
            self.textEdit.setFont(font)#如果点击了OK按钮，文本输入框字体会改变。
    #改变文本颜色
    def choicecolor(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.col = col.name()
            self.textEdit.setTextColor(col)
    #上传文件
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件','./')
        if fname[0]:
            with open(fname[0], 'r',encoding='utf-8',errors='ignore') as f:
                self.textEdit.setText(f.read())
    #上传图片
    def getfile(self):
        fname, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        # self.le.setPixmap(QPixmap(fname))
        self.img='<img src="%s">'%fname
        
        self.textEdit.append(self.img)
        # self.img1=1
        
    #居中显示   
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #发送事件
    def pushButton6(self):
        if False:
            
            userid = 'I:'
            text = self.textEdit.toPlainText()

            text="•"+text
            text_style = "font-family:{};font-size:{}px;color:{};"\
                .format(self.font_family,
                        self.font_pointSize,
                        self.col)
            userid_style = "font-family:{};font-size:{}px;color:{};"\
                .format("ubuntu",
                        "15",
                        "green")
            if self.font_bold:
                text_style +="font-weight:bold;"
                userid_style +="font-weight:bold;"

            if self.font_italic:
                text_style +="font-style:italic;"
                userid_style +="font-style:italic;"

            text_format = '<span style="{}"><pre>{}</pre></span>'.format(text_style,text)
            userid_format = '<span style="{}">{}</span>'.format(userid_style,userid)
            # image2 = QImage('/home/tarena/桌面/淘淘/image/touxiang5.jpg')
            # cursor = self.textBrowser.textCursor()
            # document = self.textBrowser.document()
            # document.addResource(QTextDocument.ImageResource, QUrl("image2"), image2)
            # cursor.insertImage("image2")
            # lbl.setScaledContents (True)
            # 获取系统现在的时间
            time = QDateTime.currentDateTime() 
            # 设置系统时间显示格式
            timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")

            me="<font color='green' size=3 font-weight='normal'>%s   %s</font>"% (userid,timeDisplay)        
            self.textBrowser.append(me)
            # self.textBrowser.append(userid)
            self.textBrowser.append(text_format)
            # self.textBrowser.append(self.img)
            self.textBrowser.append("")
            self.textEdit.clear()
        else:
            userid = '%s:'%self.nicheng
            text = self.textEdit.toPlainText()
            self.talk_select(text)


            text="•"+text
            text_style = "font-family:{};font-size:{}px;color:{};"\
                .format(self.font_family,
                        self.font_pointSize,
                        self.col)
            userid_style = "font-family:{};font-size:{}px;color:{};"\
                .format("ubuntu",
                        "15",
                        "green")
            if self.font_bold:
                text_style +="font-weight:bold;"
                userid_style +="font-weight:bold;"

            if self.font_italic:
                text_style +="font-style:italic;"
                userid_style +="font-style:italic;"

            text_format = '<span style="{}"><pre>{}</pre></span>'.format(text_style,text)
            userid_format = '<span style="{}">{}</span>'.format(userid_style,userid)
            # image2 = QImage('/home/tarena/桌面/淘淘/image/touxiang5.jpg')
            # cursor = self.textBrowser.textCursor()
            # document = self.textBrowser.document()
            # document.addResource(QTextDocument.ImageResource, QUrl("image2"), image2)
            # cursor.insertImage("image2")
            # lbl.setScaledContents (True)
            # 获取系统现在的时间
            time = QDateTime.currentDateTime() 
            # 设置系统时间显示格式
            timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")

            me="<font color='green' size=3 font-weight='normal'>%s   %s</font>"% (userid,timeDisplay)        
            self.textBrowser.append(me)
            # self.textBrowser.append(userid)
            self.textBrowser.append(text_format)
            self.textBrowser.append("")
            self.textEdit.clear()
            #下面是返回的对话
            msg3=self.talk_select(text)
            
            time = QDateTime.currentDateTime() 
            # 设置系统时间显示格式
            timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd");
            xiaobu="<font color=blue size=3 font-weight='normal'> 小布   %s</font>"%timeDisplay
            patter = r'^\d+#'
            self.image={}
            if re.search(patter,msg3):
                msg3 = msg3[:-1]
                
                books = msg3.split('&')#多有商品信息的列表
                # print(books)
                for i in books:#编列单个商品
                    book_noe = i.split('#')
                    print(book_noe)
                    #单个商品#隔开ID,,介绍连接
                    response = requests.get(book_noe[1])
                    image1 = Image.open(BytesIO(response.content))#对得到的二进制数据进行操作
                    image1.save('%s.png'%book_noe[0])#保存网络图片到本地
                    del image1#删除图片对象(虽说会自己释放)，没有这个，会出现各种问题
                    # image2 = QImage('/home/tarena/桌面/淘淘/image/3.jpg')
                    # cursor = self.textBrowser.textCursor()
                    # document = self.textBrowser.document()
                    # document.addResource(QTextDocument.ImageResource, QUrl("image2"), image2)
                    # cursor.insertImage("image2")
                    # 获取系统现在的时间
                    time = QDateTime.currentDateTime() 
                    # 设置系统时间显示格式
                    timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd");
                    xiaobu="<font color=blue size=3 font-weight='normal'> 小布   %s</font>"%timeDisplay
                    self.textBrowser.append(xiaobu)
                    self.textBrowser.append("<a style='color: green;' href=\'%s'>点击此处查看"%book_noe[2])

                    
                    self.image[i] = QImage('%s.png'%book_noe[0])
                    
                    # self.textBrowser.append("<a style='color: green;' href=\%s>点击此处查看"%book_noe[2])
                    a="<head>\
                      <meta charset='UTF-8'>\
                      <title>Document</title>\
                      <style>\
                            body,p,h1,h2,h3,h4,h5,h6,ul,ol{\
                                margin:0;\
                            }\
                            body{\
                                font-size:12px;\
                            }\
                            img{\
                                vertical-align:bottom;\
                            }\
                            #container{\
                                width:990px;\
                                margin:0 auto;\
                            }\
                      </style>\
                     </head>\
                     <body>\
                            <p>\
                                <a  href='%s'\
                                    <img src='%s'>\
                                </a>\
                            </p>\
                            <a href=\'%s'>\
                                <img src='images/cart.png'>\
                            </a>\
                            <p>'%s'</p>\
                     </body>"%(book_noe[2],book_noe[1],book_noe[2],book_noe[0])
                    print(a)
                    self.textBrowser.append("<head>\
                      <meta charset='UTF-8'>\
                      <title>Document</title>\
                      <style>\
                            body,p,h1,h2,h3,h4,h5,h6,ul,ol{\
                                margin:0;\
                            }\
                            body{\
                                font-size:12px;\
                            }\
                            img{\
                                vertical-align:bottom;\
                            }\
                            #container{\
                                width:990px;\
                                margin:0 auto;\
                            }\
                      </style>\
                     </head>\
                     <body>\
                            <p>\
                                <a  href='%s'\
                                    <img src='%s'>\
                                </a>\
                            </p>\
                            <a href=\'%s'>\
                                <img src='images/cart.png'>\
                            </a>\
                            <p>'%s'</p>\
                     </body>"%(book_noe[2],book_noe[1],book_noe[2],book_noe[0]))
                    #                     <div>\
                    #     &yen;188.00/1份\
                    # </div>\
                    # self.textBrowser.insertPlainText("aaa")
                    # self.textBrowser.append('<a href="http://taobao.cyberhome.cn/"><img src="http://www.cyberhome.cn/images/girl/PLMM_C.jpg"></a>')
                    # self.textBrowser.append('<img src="/home/tarena/桌面/淘淘/image/3.jpg">')
                    # self.textBrowser.append('<div width="1190px"><p><a href="#"><img src="/home/tarena/桌面/淘淘/image/1-270x270-430-9RBRWTU9.jpg"></a></p></div>')
                    cursor = self.textBrowser.textCursor()
                    document = self.textBrowser.document()
                    document.addResource(QTextDocument.ImageResource, QUrl("image%s"%i), self.image[i])
                    cursor.insertImage("image%s"%i)
                    self.textBrowser.append("")
                    # self.img1=0
            else:
                print(msg3)
                self.textBrowser.append(xiaobu)
                self.textBrowser.append(msg3)


            
    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)
    
    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())
    #智能机器人
    def robot(self):
        pass
    #人工客服
    def service(self):
        pass
    #购物车
    def cart(self):
        pass
    #支付
    def pain(self):
        pass

    #聊天框显示网址和图片文件
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        # http://f10.baidu.com/it/u=2881303562,336932824&fm=72   试用地址
        # http://img5.imgtn.bdimg.com/it/u=732110664,2088490163&fm=27&gp=0.jpg
        # response = requests.get(self.textEdit.toPlainText())#使用requests库进行网络请求获取内容
        response = requests.get('http://f10.baidu.com/it/u=2881303562,336932824&fm=72')
        image1 = Image.open(BytesIO(response.content))#对得到的二进制数据进行操作
        image1.save('xxx.png')#保存网络图片到本地
        del image1#删除图片对象(虽说会自己释放)，没有这个，会出现各种问题
        # image2 = QImage('/home/tarena/桌面/淘淘/image/3.jpg')
        # cursor = self.textBrowser.textCursor()
        # document = self.textBrowser.document()
        # document.addResource(QTextDocument.ImageResource, QUrl("image2"), image2)
        # cursor.insertImage("image2")
        # 获取系统现在的时间
        time = QDateTime.currentDateTime() 
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd");
        xiaobu="<font color=blue size=3 font-weight='normal'> 小布   %s</font>"%timeDisplay
        self.textBrowser.append(xiaobu)
        
        image = QImage('xxx.png')
        print(image)
        self.textBrowser.append("<a style='color: green;' href=\"http://blog.csdn.net/fron_csl\">点击此处查看")
        self.textBrowser.append(' <head>\
          <meta charset="UTF-8">\
          <title>Document</title>\
          <style>\
                body,p,h1,h2,h3,h4,h5,h6,ul,ol{\
                    margin:0;\
                }\
                body{\
                    font-size:12px;\
                }\
                img{\
                    vertical-align:bottom;\
                }\
                #container{\
                    width:990px;\
                    margin:0 auto;\
                }\
          </style>\
         </head>\
         <body>\
                <p>\
                    <a  href="#"\
                        <img src="/home/tarena/桌面/淘淘/image/1-270x270-430-9RBRWTU9.jpg">\
                    </a>\
                </p>\
                <a href=\"http://www.bmw.com.cn/zh/all-models/x-series/X1/2017/overview.html">\
                    <img src="images/cart.png">\
                </a>\
                <p>欢乐时光水果礼篮</p>\
                <div>\
                    &yen;188.00/1份\
                </div>\
         </body>')
        # self.textBrowser.insertPlainText("aaa")
        self.textBrowser.append('<a href="http://taobao.cyberhome.cn/"><img src="http://img2.imgtn.bdimg.com/it/u=2473758249,2536588353&fm=200&gp=0.jpg"></a>')
        # self.textBrowser.append('<img src="/home/tarena/桌面/淘淘/image/3.jpg">')
        # self.textBrowser.append('<div width="1190px"><p><a href="#"><img src="/home/tarena/桌面/淘淘/image/1-270x270-430-9RBRWTU9.jpg"></a></p></div>')
        cursor = self.textBrowser.textCursor()
        document = self.textBrowser.document()
        document.addResource(QTextDocument.ImageResource, QUrl("image"), image)
        cursor.insertImage("image")
        self.textBrowser.append("")
        # self.textBrowser.append("<h1>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<\h1>")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    icon = Ui_self()
    icon.show()
    # 设置10s后自动退出
    # QTimer.singleShot(10000, app.quit) 
    sys.exit(app.exec_())
