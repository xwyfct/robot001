'''
author:xiewei
date:2018-06-11
conversation.py
输入一个关键字实现自动回复功能
'''
import re
import random

def conversation(key_word):
    try:
        fd = open('conversations.txt')
    except IOError:
        print("语料库不存在")
    lines = fd.readlines()
    fd.close()

    pattern = r'\w*%s\w*'%key_word
    obj = re.compile(pattern, re.I)
    i = 0
    responses = []
    for line in lines:
        i += 1
        s = obj.findall(line)
        if (s != []) and (lines[i][0:3] != '- -'):
            responses.append(lines[i])
    try:
        response = random.sample(responses, 1)[0][4:]
    except Exception:
        return "对不起，不清楚您的问题，请描述清楚。"
    else:
        return response

if __name__ == '__main__':
    while 1:
        key_word = input(">>")
        response = conversation(key_word)
        print(response)

    



