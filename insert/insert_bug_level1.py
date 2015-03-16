#!/usr/bin/python
#usage ./insert_script "file_name"                                                                

import sys
import time
sys.path.append(sys.path[0] + '/..')
from service.mongoDB import mongoDB
import service.mod_config

header=['its','repo','n_peo','n_bug','b_time','e_time','span','loc','_id']
dbname = service.mod_config.getConfig('db.conf','database','dbname')
db = mongoDB(dbname)

def readData():
    try:
        in_file = open(sys.argv[1])
        ret = []
        count = 1
        for line in in_file:
            item = {}
            line = line.strip('\n')
            sp = line.split(';')
            sp[2] = int(sp[2])
            sp[3] = int(sp[3])
            sp[4] = int(sp[4])
            sp[5] = int(sp[5])
            sp[6] = int(sp[6])
            for i in range(0, len(sp)):
                item[header[i]] = sp[i]
            item[header[-1]] = time.time()
            ret.append(item)
        return ret
    except:
        usage.__call__()

def insertDB(data):
    collection = 'bug_level1'
    for i in range(0, len(data)):
        db.insert(collection, data[i])

def usage():
    print 'usage: ./insert_bug_level1 "file_name" '

data = readData()
insertDB(data)
