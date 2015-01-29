#!/usr/bin/python
                                                                
# coding=utf-8

import re
import sys
import time
import os

path = '/home/lj/email'


#month = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

#date = re.compile(r'Date: ')
#date_spe = re.compile(r'\d+ \S+ \d+ \d+:\d+:\d+')
fro = re.compile(r'From: ')
to = re.compile(r'To: ')
mes = re.compile(r'Message-ID: ')

dirs = os.listdir(path)
for d in dirs:
    if(os.path.isdir(path + '/' + d)):
        files = os.listdir(path + '/' + d)
        for f in files:
            nemail = 0
            #start = 0
            #end = 0
            n_fro = 0
            n_to = 0
            n_peo = 0
            fro_dic = {}
            to_dic = {}
            peo_dic = {}
            if(os.path.isfile(path + '/' + d + '/' + f)):
                in_file = open(path + '/' + d + '/' + f)
                for line in in_file:
                    match = mes.match(line)
                    if match:
                        nemail = nemail + 1
                        continue
                    match = fro.match(line)
                    if match:
                        key = line[6:-1]
                        if key not in fro_dic.keys():
                            n_fro = n_fro + 1
                            fro_dic[key] = 1
                        if key not in peo_dic.keys():
                            n_peo = n_peo + 1
                            peo_dic[key] = 1
                        continue
                    match = to.match(line)
                    if match:
                        key = line[4:-1]
                        if key not in to_dic.keys():
                            n_to = n_to + 1
                            to_dic[key] = 1
                        if key not in peo_dic.keys():
                            n_peo = n_peo + 1
                            peo_dic[key] = 1
                        continue
                    #match = date.match(line)
                    #if match:
                    #    match = date_spe.search(line)
                    #    if match:
                    #        l = match.group().split(' ')
                    #        t = l[2] + month[l[1]] + l[0] 
                    #        if start == 0:
                    #            start = t
                    #            end = t
                    #        else:
                    #            if start > t: 
                    #                start = t
                    #            if end < t:
                    #                end = t
                    #        continue
                if(nemail > 0):
                    print 'mbox;' + d + ';' + str(nemail) + ';' + str(n_peo) + ';' + str(n_fro) + ';' + str(n_to) + ';'+ path + '/' + d + '/' + f
                    #print 'mbox;' + d + ';' + str(nemail) + ';' + str(n_peo) + ';' + str(n_fro) + ';' + str(n_to) + ';' + start + ';' + end + ';'+ path + '/' + d + '/' + f
