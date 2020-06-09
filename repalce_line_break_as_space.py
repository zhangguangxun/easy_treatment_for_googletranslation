# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:43:09 2020

@author: Administrator
"""

with open('新建文本文档.txt','r') as f:
    string = f.read()
    string = string.replace('\n',' ')
with open('output.txt','w') as fout:
    fout.write(string)

