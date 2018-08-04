#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright 2018 xw <xw@XIEWEI>
data:20180602
此模块通过输入一段字符串，提取出前三个关键字
'''
# 导入中文分词模块
import jieba
import jieba.analyse

from goods import *

# 关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径
jieba.analyse.set_idf_path("conver_idf.txt.big")

# 定义文本解析函数
def resolver(client_data):
    # 考虑存在外部goods.py文件中
    key_word_list = Goods().key_word_list
    seg_list = jieba.cut(client_data, cut_all=True, HMM=False)
    # 去除重复分词
    seg_set = set(seg_list)
    

    # 提取关键词
    tags = jieba.analyse.extract_tags(client_data, topK=1)
    # tags = jieba.analyse.textrank(client_data, topK=5, withWeight=True, \
    # allowPOS=('ns', 'n', 'vn', 'v'))
    # 判断文本分析结果类型
    valid_key_word = []
    for i in seg_set:
        if i in key_word_list:
            valid_key_word.append(i)
    if valid_key_word != []:
        print(valid_key_word)
        return valid_key_word[0]
    else:
        try:
            print(tags)
            return tags[0]
        except Exception:
            return

if __name__ == '__main__':
    while 1:
    	client_data = input("client_data：")
    	key_word = resolver(client_data)
    	print(key_word)
