#!/usr/bin/python

import sys
sys.path.append(sys.path[0] + '/..')
import service.mod_config
from service.mongoDB import mongoDB

class find:
    
    def __init__(self):
        dbname = service.mod_config.getConfig('db.conf','database','dbname')
        self.db = mongoDB(dbname).get_db()
    
    def __REGEX__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$regex' : str(val)}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __EQ__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : val})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __NE__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$ne' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __LT__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$lt' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __GT__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$gt' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __LTE__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$lte' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __GTE__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$gte' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    
    def __IN__(self, collection, key, *val):
        posts = self.db[str(collection)].find({str(key) : {'$in' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __NIN__(self, collection, key, *val):
        posts = self.db[str(collection)].find({str(key) : {'$nin' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __ALL__(self, collection, key, *val):
        posts = self.db[str(collection)].find({str(key) : {'$all' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __AND__(self, collection, arg):
        posts = self.db[str(collection)].find(arg)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
#sort

    def __REGEXs__(self, collection, key, val, sor):
        posts = self.db[str(collection)].find({str(key) : {'$regex' : str(val)}}).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __EQs__(self, collection, key, val, sor):
        posts = self.db[str(collection)].find({str(key) : val}).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __NEs__(self, collection, key, val, sor):
        posts = self.db[str(collection)].find({str(key) : {'$ne' : val}}).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __LTs__(self, collection, key, val, sor):
        posts = self.db[str(collection)].find({str(key) : {'$lt' : val}}).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __GTs__(self, collection, key, val, sor):
        posts = self.db[str(collection)].find({str(key) : {'$gt' : val}}).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __LTEs__(self, collection, key, val, sor):
        posts = self.db[str(collection)].find({str(key) : {'$lte' : val}}).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __GTEs__(self, collection, key, val, sor):
        posts = self.db[str(collection)].find({str(key) : {'$gte' : val}}).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    
    def __ANDs__(self, collection, arg, sor):
        posts = self.db[str(collection)].find(arg).sort(sor)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
         

    def get_header(self, collection):
        posts = self.db[str(collection)].find_one({})
        ret = []
        for key in posts:
            ret.append(key)
        return ret
