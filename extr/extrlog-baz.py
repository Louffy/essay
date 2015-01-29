#!/usr/bin/python
                                                                
# coding=utf-8

import re
import sys
import time
import os

path = '/home/lj/log/bazaar'

rev = re.compile(r'revno:')
com = re.compile(r'committer:')
timestamp = re.compile(r'timestamp:')
time_spe = re.compile(r'\d+-\d+-\d+ \d+:\d+:\d+')

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
                        key = line[11:-1]
                        if key not in com_dic.keys():
                            com_dic[key] = 1
                            ncom = ncom + 1
                        continue
                    match = timestamp.match(line)
                    if match:
                        match = time_spe.search(line)
                        timeArray = time.strptime(match.group(), "%Y-%m-%d %H:%M:%S")
                        t = int(time.mktime(timeArray))
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
                    print 'bazaar;' + d + ';' + str(ncom) + ';' + str(nrev) + ';' + str(time.strftime("%Y%m",time.localtime(start))) + ';' + str(time.strftime("%Y%m",time.localtime(end))) + ';' + path + '/' + d + '/' + f
