#!/usr/bin/env python3
#-*- encoding:utf-8 -*-  

'''
Copyright 2018 xw <xw@XIEWEI>
data:20180612
此模块功能如下:
读取文件，文件每行是一个文档,计算得到idf文件.
求idf得步骤： 
1.对所有文档进行分词，去停用词，结果放入二维list，其中每个元素是set 
2.得到文档数目；生成所有词的set 
3.对每个词计算idf,idf = log(n / docs(w, D)) 
注意：默认每个文件是一篇文档
此文件问初始化文件，在主函数运行时自动调用。
''' 
import os  
import jieba  
import jieba.analyse  
import math  
import sys  

class ComputeIdf:  
    file_path = u""  
    idf_path = ''  
    stopwords_file = ""  
    selfdict_file = ""  
    def __init__(self,file_path="",idf_path="",stopwords_file="",\
        selfdict_file=""):  
        self.stopwords_file = stopwords_file  
        self.selfdict_file = selfdict_file  
        self.file_path = file_path  
        self.idf_path = idf_path  
        #jieba.analyse.set_stop_words(stopwords_file)  
  
    def cal_and_save_idf(self):  
        f = open(self.file_path, "r")  
        # 获取停用词  
        stopwords = {}.fromkeys([line.rstrip() for line in \
            open(self.stopwords_file)])  
        # 得到idf的字典  
        idf_dict = self.compute_idf(f, stopwords)  
        # 存储  
        self.save(idf_dict, self.idf_path)  
  
    def compute_idf(self,f, stopwords):  
        # 所有分词后文档  
        D = []  
        # 所有词的set  
        W = set()  
        for i, line in enumerate(f):  
            # 新闻原始数据  
            content = line  
            content = content.replace("\n","")  
            d = self.seg(content, stopwords)  
            D.append(d)  
            W = W | d  
            print("第" + str(i) + "个文档 共4796065")  
        # 计算idf  
        idf_dict = {}  
        n = len(W)  
        print("词典生成完成，共"+str(n)+"个词")  
        # idf = log(n / docs(w, D))  
        k=0  
        for w in list(W):  
            idf = math.log(n * 1.0 / self.docs(w, D))  
            idf_dict[w] = idf  
              
            k=k+1  
        print("idf计算完成")  
        return idf_dict  
  
    def seg(self,content, stopwords):  
        '''
        分词并去除停用词 
        '''  
        segs = jieba.cut(content, cut_all=True)  
        segs = [w for w in list(segs)]  # 特别注意此处转换  
  
        seg_set = set(set(segs) - set(stopwords))  
        return seg_set  
  
    def docs(self,w, D):  
        c = 0  
        for d in D:  
            if w in d:  
                c = c + 1;  
        return c  
  
    def save(self,idf_dict, path):  
        f = open(path, "a+")  
        f.truncate()  
        # write_list = []  
        for key in idf_dict.keys():  
            # write_list.append(str(key)+" "+str(idf_dict[key]))  
            f.write(str(key) + " " + str(idf_dict[key]) + "\n")  
        f.close()  
  
def run():  
    file_path = u"./conversations.txt"  
      
    idf_path = u'./conver_idf.txt.big'  
    stopwords_file = "./stop_words.txt"  
    selfdict_file = ""  
  
    c = ComputeIdf(file_path=file_path,idf_path=idf_path,\
        stopwords_file=stopwords_file)  
  
    c.cal_and_save_idf()  
    return  
  
if __name__ == '__main__':
    run()
 