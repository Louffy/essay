#!/usr/bin/python

import sys
sys.path.append(sys.path[0] + '/..')
from search.pyfind import find
from bson import ObjectId


class test:

    def __init__(self):
        self.db = find()
        
    def test_update(self):
        post = { "_id" : ObjectId("549a29241d41c80d05aaf465"), "cata" : "bug", "des" : "", "in" : 121321, "loc" : "/store1/bug/launch/d.perl", "name" : "d.perl", "out" : "" }
        print self.db.update('script',post)
        
    def test__LT__(self):
        ret = self.db.__LT__('svn_info', 'n_cmt', 2)
        print ret
    
    def test__GT__(self):
        ret = self.db.__GT__('svn_info', 'n_cmt', 100000)
        print ret
        
    def test__EQ__(self):
        ret = self.db.__EQ__('script', 'name', 'extr.perl')
        print ret
        
    def test__AND__(self, arg):
        #arg = {'span':{'$lt':100,'$gt':90},'n_cmt':{'$lt':100000,'$gt':1000}}
        ret = self.db.__AND__('svn_info', arg)
        for r in ret:
            print r['log_loc'] + ';' + r['src_loc']
