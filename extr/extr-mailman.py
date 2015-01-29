#!/usr/bin/python
                                                                
# coding=utf-8

import re
import sys
import time
import os
import gzip

path = '/home/lj/email/mailman'

fro = re.compile(r'From: ')
mes = re.compile(r'Message-ID: ')
gz = re.compile(r'.gz')
save_file = open('err','w')

dirs = os.listdir(path)
for d in dirs:
    if(os.path.isdir(path + '/' + d)):
        repos = os.listdir(path + '/' + d)
        for repo in repos:
            if(os.path.isdir(path + '/' + d + '/' + repo)):
                files = os.listdir(path + '/' + d + '/' + repo)
                for f in files:
                    nemail = 0
                    n_peo = 0
                    peo_dic = {}
                    if(os.path.isfile(path + '/' + d + '/' + repo + '/' + f)):
                        sufix = os.path.splitext(f)[1][1:]
                        if sufix == 'gz':
                            try:
                                in_file = gzip.open(path + '/' + d + '/' + repo + '/' + f)
                                for line in in_file:
                                    match = mes.match(line)
                                    if match:
                                        nemail = nemail + 1
                                        continue
                                    match = fro.match(line)
                                    if match:
                                        key = line[6:-1]
                                        if key not in peo_dic.keys():
                                            n_peo = n_peo + 1
                                            peo_dic[key] = 1
                                            continue
                            except:
                                save_file.write(path + '/' + d + '/' + repo + '/' + f + '\n')
                                continue
                        else:
                            try:
                                in_file = open(path + '/' + d + '/' + repo + '/' + f)
                                for line in in_file:
                                    match = mes.match(line)
                                    if match:
                                        nemail = nemail + 1
                                        continue
                                    match = fro.match(line)
                                    if match:
                                        key = line[6:-1]
                                        if key not in peo_dic.keys():
                                            n_peo = n_peo + 1
                                            peo_dic[key] = 1
                                            continue
                            except:
                                save_file.write(path + '/' + d + '/' + repo + '/' + f + '\n')
                                continue
                    if(nemail > 0):
                        print 'mailman;' + d + ';' + repo + ';' + str(nemail) + ';' + str(n_peo) + ';' +  path + '/' + d + '/' + repo + '/' + f
