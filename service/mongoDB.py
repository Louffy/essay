#!/usr/bin/python
                                                                
import pymongo
import sys
import mod_config
from bson import ObjectId

class mongoDB:

    def __init__(self, db):
        dbhost = mod_config.getConfig('db.conf','database','dbhost')
        dbport = mod_config.getConfig('db.conf','database','dbport')
        client = pymongo.MongoClient(dbhost, int(dbport))
        self.db = client[db]
    
    def get_db(self):
        return self.db
    
    def insert(self, collection, document):
        collection = self.db[collection]
        collection.insert(document)
        
    def update(self, collection, post):
        collection = self.db[collection]
        OID = post["_id"]
        post.pop("_id")
        collection.update({"_id":OID},{"$set":post})
    
    
