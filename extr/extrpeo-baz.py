#!/usr/bin/python
                                                                
# coding=utf-8

import re
import sys
import time
import os

class people:
    def __init__(self,name,commits,t_commits):
        self.name = name
        self.commits = commits
        self.t_commits = t_commits

class t_commit:
    def __init__(self,time,commit):
        self.time = time
        self.commit = commit

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
            if(os.path.isfile(path + '/' + d + '/' + f)):
                in_file = open(path + '/' + d + '/' + f)
                peo_dic = {}
                key = ''
                for line in in_file:
                    match = com.match(line)
                    if match:
                        key = line[11:-1]
                        continue
                    match = timestamp.match(line)
                    if match:
                        match = time_spe.search(line)
                        timeArray = time.strptime(match.group(), "%Y-%m-%d %H:%M:%S")
                        t = int(time.mktime(timeArray))
                        tt = time.strftime("%Y%m",time.localtime(t))
                        if key not in peo_dic.keys():
                            t_c = t_commit(tt,1)
                            t_dic = {}
                            t_dic[tt] = t_c
                            p = people(key,1,t_dic)
                            peo_dic[key] = p
                        else:
                            t_dic = peo_dic[key].t_commits
                            if tt not in t_dic.keys():
                                t_c = t_commit(tt,1)
                                t_dic[tt] = t_c
                            else:
                                t_dic[tt].commit += 1
                if len(peo_dic) > 0:
                    for peo in peo_dic:
                        print d+ '/' + f + ';' + peo + ';' + '{',
                        for t_c in peo_dic[peo].t_commits:
                            print peo_dic[peo].t_commits[t_c].time + ':' + str(peo_dic[peo].t_commits[t_c].commit) + ';',
                        print '}'    
