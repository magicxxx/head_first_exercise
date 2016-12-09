#!/usr/bin/env python
#-*- encoding:utf-8 -*-
files = ['james.txt','julie.txt','mikey.txt','sarah.txt']
data = {}
for fi in files:
    with open(fi) as f:
        value = f.readline()
        data[fi.split('.')[0]] = value.strip().split(',')
for k, v in data.items():
    print k, v
