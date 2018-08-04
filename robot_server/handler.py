#!/usr/bin/env python3
# coding=utf-8

'''
author:xiewei
date:20180531
func:智能导购机器人后端处理模块
'''
import pymysql
import re
import time

# 导入文本解析模块
from resolver import *
# 自动回复功能模块
from conversation import *

class Handler:
	def __init__(self):
	    self.conn = pymysql.connect("localhost", "root", "123456", "robot")
	    self.cur = self.conn.cursor()

	def login(self, c, name, passwd):
	    sql_select_name = \
	    "select name,passwd,nickname from user where name='%s';" % name
	    self.cur.execute(sql_select_name)
	    data = self.cur.fetchone()
	    if data != None:
	    	print(data)
	    	if data[1] == passwd:
	    		c.send(('登录成功'+" "+data[2]).encode())
	    		return True
	    	else:
	    		c.send('密码有误'.encode())
	    else:
	    	c.send('用户不存在,请先注册。'.encode())
	    
	def register(self, c, name, passwd, nickname):
		# print(type(name))
		# print(type(passwd))
		# print(type(nickname))
		# 数据查询
		self.cur.execute\
		("select name from user where name='%s';" % name)
		data = self.cur.fetchall()
		# 判断用户名是否存在

		# 如果未查询到则返回空
		if data == ():
		    # 将数据插入到数据库中
		    self.cur.execute\
		    ("insert into user(name,passwd,nickname) values ('%s','%s','%s');"\
		    	% (name,passwd,nickname))
		    self.conn.commit()
		    c.send(b'Y')
		else:
		    # 查询到结果　向客户端发出命令      
		    c.send(b'N')
	    
	    


	def chat(self):
	    pass

	def query1(self, client_data):
	    data = resolver(client_data)
	    sql = "select id,image_url,detail_url from product where key_word regexp '%s'" % data
	    self.cur.execute(sql)
	    goods_info_tuple = self.cur.fetchall()
	    # 商品信息元组格式((id1,image_url1,detail_url1),\
	    # (id2,image_url2,detail_url2),(id3,image_url3,detail_url3))
	    if goods_info_tuple:
	        resolved_data = goods_info_tuple
	    else:
	        resolved_data = data

	    if isinstance(resolved_data, tuple):
	        response = ""
	        for i in goods_info_tuple:
	            response += "#".join(i)
	            response += "&"
	    else:
	    	response = conversation(resolved_data)
	    return response



	def query2(self, product_id):
	    pass

	def add_to_cart(self):
	    pass

	def pay(self):
	    pass
