#!/usr/bin/python
                                                                
# coding=utf-8

import re
import sys
import time
import os

path = '/home/lj/log/git'

month = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
rev = re.compile(r'commit')
com = re.compile(r'Author:')
timestamp = re.compile(r'Date:')
time_spe = re.compile(r'\S+ \d+ \d+:\d+:\d+ \d+')

dirs = os.listdir(path)
for d in dirs:
    if(os.path.isdir(path + '/' + d)):
        files = os.listdir(path + '/' + d)
        for f in files:
            nrev = 0
            ncom = 0
            start = 0
            end = 0
            com_dic = {}
            if(os.path.isfile(path + '/' + d + '/' + f)):
                in_file = open(path + '/' + d + '/' + f)
                for line in in_file:
                    match = rev.match(line)
                    if match:
                        nrev = nrev + 1
                        continue
                    match = com.match(line)
                    if match:
                        key = line[8:-1]
                        if key not in com_dic.keys():
                            com_dic[key] = 1
                            ncom = ncom + 1
                        continue
                    match = timestamp.match(line)
                    if match:
                        match = time_spe.search(line)
                        if match:
                            l = match.group().split(' ')
                            t = l[3] + month[l[0]]
                            if start == 0:
                                start = t
                                end = t
                            else:
                                if start > t: 
                                    start = t
                                if end < t:
                                    end = t
                            continue
                if(ncom > 0):
                    print 'git;' + d + ';' + str(ncom) + ';' + str(nrev) + ';' + start + ';' + end + ';' + path + '/' + d + '/' + f
