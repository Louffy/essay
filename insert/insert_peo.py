#!/usr/bin/python
#usage ./insert_peo  "file_name" "vcs"                                                                 

import sys
sys.path.append(sys.path[0] + '/..')
from service.mongoDB import mongoDB
import service.mod_config

header=['repo','name','cpm']
dict_vcs={'svn':'svn_peo', 'git':'git_peo', 'hg':'hg_peo', 'bazaar':'baz_peo'}
dbname = service.mod_config.getConfig('db.conf','database','dbname')
db = mongoDB(dbname)

def readData():
    in_file = open(sys.argv[1])
    ret = []
    for line in in_file:
        item = {}
        line = line.strip('\n')
        sp = line.split(';')
        for i in range(0, len(sp)):
            item[header[i]] = sp[i]
        ret.append(item)
    return ret

def insertDB(vcs, data):
    if vcs not in dict_vcs.keys():
        usage.__call__()
    else:
        collection = dict_vcs[vcs]
        for i in range(0, len(data)):
            db.insert(collection, data[i])

def usage():
    print "usage:"
    print sys.argv[2] + ' svn|git|hg|bazaar'

data = readData()
insertDB(sys.argv[2], data)
