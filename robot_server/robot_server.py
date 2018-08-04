#!/usr/bin/env python3
#coding=utf-8

'''
author:xiewei
date:20180531
func:智能导购机器人服务器
'''

from socket import *
from threading import *
import os, sys
from time import sleep

# 导入后端逻辑与数据处理模块
from handler import *

# 定义全局变量
HOST = '127.0.0.1'
PORT = 8888

# 接收客户端请求，解析交给后端处理，并将后端处理后的数据发给前端
def client_handler(c):
    # 循环接收客户端购物请求，直到客户端退出登录时，结束循环并关闭相应客户端通信套接字
    while 1:
        # 接收客户端购物请求
        client_list = c.recv(1024).decode().split('&')
        # print(client_list)
        try:
            client_data = client_list[0]
        except Exception as e:
            print(e)
        # 创建后端处理对象
        hd = Handler()
        # 根据不同请求标示符号调用不同后端处理方法
        # 登录模块
        if client_data == 'L':
            name = client_list[1]
            passwd = client_list[2]
            ret = hd.login(c, name, passwd)
            # 如果登录成功进入商品查询模块及自动回复模块
            if ret:
                print(name,"登录成功")
                while 1:
                    # print("开始接收消息")
                    client_data = c.recv(2048).decode()
                    # print("******",client_data)
                    if client_data == "quit":
                        break
                    response = hd.query1(client_data)
                    # print("===",response)
                    c.send(response.encode())

        # 注册模块
        elif client_data == 'R':
            name = client_list[1]
            passwd = client_list[2]
            nickname = client_list[3]
            hd.register(c, name, passwd, nickname)
        # 聊天模块，保留待用
        elif client_data == 'C':
            hd.chat()
                
        # 加入购物车模块
        elif client_data == 'A':
            hd.add_to_car()
        # 支付模块
        elif client_data == 'P':
            hd.pay()
        # 客户端退出
        elif client_data == 'E':
            break
    print(c.getpeername(),name,"客户端已经退出")
    c.close()
    

# 定义服务端主控制流程函数
def main():
    # 创建套接字，绑定，监听，设置端口可重用
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)

    # 主线程循环等待接收客户端连接
    while 1:
        try:
            print('等待客户端连接')
            c, addr = s.accept()
            print(addr, "已连接服务器")
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(e)
            continue

        # 创建分支线程处理客户端请求，参数c属于全局变量，随时变化，需要传参
        t = Thread(target=client_handler, args=(c,))
        # 主线程退出，子线程自动退出
        t.setDaemon(True)
        t.start()
    s.close()

if __name__ == '__main__':
    main()
    
