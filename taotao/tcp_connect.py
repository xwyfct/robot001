import os,sys,time
from socket import *
import hashlib

class App():
    def __init__(self,sock=None):
        self.sock = sock
        

    def login(self,userno,password):#登录
        # 加密
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        password = hl.hexdigest()

        data = 'L'+'&'+userno+'&'+password
        self.userno = userno
        self.sock.send(data.encode())
        msg = self.sock.recv(2048).decode()
        
        return msg
        # if msg == '登录成功':
        #     print('成功')
        # elif msg == '密码有误': 
        #     print('账号或密码不正确,请从新输入')
        # elif msg == '用户不存在,请先注册。'
        #     print('账号不存在,请先注册')

    def register(self,userno,password,user_name):#注册
        # 加密
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        password = hl.hexdigest()

        data = 'R'+'&'+userno+'&'+password+'&'+user_name
        self.sock.send(data.encode())
        msg = self.sock.recv(2048).decode()
        return msg
        # if msg == 'Y';
        #     print('注册成功')
        # else:
        #     print('已存在')


    def talk_select(self,data):#咨询
            self.sock.send(data.encode())
            msg = self.sock.recv(2048).decode()
            return msg
            # if msg[0] == '&':
            #     books = msg.split('&')#多有商品信息的列表
            #     for book in books:#编列单个商品
            #         book_noe = book.split('#')
            #         return book_noe#单个商品#隔开ID,,介绍连接
            #         book_noe[0]
            #         book_noe[1]
            #         book_noe[2]
            # else:
            #     print(msg)

    def user_exit(self):#退出
        self.sock.send('quit'.encode())
        time.sleep(1)
        self.sock.send(b'E')
        os._exit(0)

def main(data):
    host = '127.0.0.1'
    port = 8888
    sock = socket(AF_INET,SOCK_STREAM,0)
    sock.connect((host,port))
    app = App(sock)
    welcome = sock.recv(2048).decode()
    print(welcome)
    # while True:
    #     data = int(input('输入:'))#用户的请求类型，根据类型调用
    #     if data == 1:#登录
    #         app.login(userno,password)
    #     elif data == 2:#注册
    #         pass
    #     elif data == 3:#聊天
    #         app.talk()
    #     elif data == 4:#商品查询
    #         app.select()
    #     elif data == 5:#加入购物车
    #         pass
    #     elif data == 6:#支付
    #         pass
    #     elif data == :#退出
    #         app.user_exit()
    #         sock.close()

if __name__ == '__main__':
    main(data)




