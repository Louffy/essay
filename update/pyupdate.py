#!/usr/bin/python

import sys
sys.path.append(sys.path[0] + '/..')
import service.mod_config
from service.mongoDB import mongoDB

class update:
    
    def __init__(self):
        dbname = service.mod_config.getConfig('db.conf','database','dbname')
        self.db = mongoDB(dbname).get_db()
    
    def update(self, collection, ids, arg):
        header = self.get_header(collection) 
        for key in arg.keys():
            posts = self.db[str(collection)].update({"_id" : ids},{"$set":{key : arg[key]}})
        return self.db[str(collection)].find({"_id" : ids})[0]

    def insert(self, collection, arg):
        header = self.get_header(collection)


    def delete(self, collection, ids):
        header = self.get_header(collection)

    def get_header(self, collection):
        posts = self.db[str(collection)].find_one({})
        ret = []
        for key in posts:
            ret.append(key)
        return ret
         