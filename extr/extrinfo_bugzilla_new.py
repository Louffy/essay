#!/usr/bin/python
                                                                
# coding=utf-8

import re
import sys
import time
import os

loc = open('info_level1_loc')
save_file = open('result','w')

com = re.compile(r'who_name=(.*?);')
timestamp = re.compile(r'bug_when=(\d+-\d+-\d+ \d+:\d+:\d+) ')

for f in loc:
    ncom = 0
    start = 0
    end = 0
    count = 0
    com_dic = {}
    fname = f.strip('\n')
    in_file = open(fname)
    for line in in_file:
        match = com.findall(line)
        if match:
            for key in match:
                if key not in com_dic.keys():
                    com_dic[key] = 1
                    ncom = ncom + 1
        match = timestamp.findall(line)
        if match: 
            for times in match:
                timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
                t = int(time.mktime(timeArray))
                if start == 0:
                    start = t
                    end = t
                else:
                    if start > t: 
                        start = t
                    if end < t:
                        end = t
        count = count + 1
        print fname + ' ' + str(count)
    save_file.write('bugzilla;' + ';' + str(ncom) + ';' + str(count) + ';' + str(time.strftime("%Y%m",time.localtime(start))) + ';' + str(time.strftime("%Y%m",time.localtime(end))) + ';' + fname)
