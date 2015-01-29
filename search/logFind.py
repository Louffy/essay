#!/usr/bin/python

from pyfind import find
import sys
sys.path.append(sys.path[0] + '/..')
import service.mod_config

class logFind(object):
    
    def __init__(self):
        self.pf = find()
        self.span = service.mod_config.getConfig('header.conf','log','span')
        self.btime = service.mod_config.getConfig('header.conf','log','btime')
        self.etime = service.mod_config.getConfig('header.conf','log','etime')
        self.ncmt = service.mod_config.getConfig('header.conf','log','ncmt')
        self.npeo = service.mod_config.getConfig('header.conf','log','npeo')
        self.repo = service.mod_config.getConfig('header.conf','log','repo')
        self.prj = service.mod_config.getConfig('header.conf','log','prj')
        
        
    def find_span_scope(self, collection, low, high):
        arg = {self.span:{'$gte':int(low),'$lte':int(high)}}
        return self.pf.__AND__(collection, arg)
    
    def find_span_lte(self, collection, val):
        return self.pf.__LTE__(collection, self.span, val)
        
    def find_span_gte(self, collection, val):
        return self.pf.__GTE__(collection, self.span, val)    
    
        
    def find_btime_scope(self, collection, low, high):
        arg = {self.btime:{'$gte':int(low),'$lte':int(high)}}
        return self.pf.__AND__(collection, arg)
            
    def find_btime_lte(self, collection, val):
        return self.pf.__LTE__(collection, self.btime, val)
        
    def find_btime_gte(self, collection, val):
        return self.pf.__GTE__(collection, self.btime, val)
    
        
    def find_etime_scope(self, collection, low, high):
        arg = {self.etime:{'$gte':int(low),'$lte':int(high)}}
        return self.pf.__AND__(collection, arg)    
        
    def find_etime_lte(self, collection, val):
        return self.pf.__LTE__(collection, self.etime, val)
        
    def find_etime_gte(self, collection, val):
        return self.pf.__GTE__(collection, self.etime, val)
    
    
    def find_ncmt_scope(self, collection, low, high):
        arg = {self.ncmt:{'$gte':int(low),'$lte':int(high)}}
        return self.pf.__AND__(collection, arg)
            
    def find_ncmt_lte(self, collection, val):
        return self.pf.__LTE__(collection, self.ncmt, val)
        
    def find_ncmt_gte(self, collection, val):
        return self.pf.__GTE__(collection, self.ncmt, val)
    
    
    def find_npeo_scope(self, collection, low, high):
        arg = {self.npeo:{'$gte':int(low),'$lte':int(high)}}
        return self.pf.__AND__(collection, arg)
            
    def find_npeo_lte(self, collection, val):
        return self.pf.__LTE__(collection, self.npeo, val)
        
    def find_npeo_gte(self, collection, val):
        return self.pf.__GTE__(collection, self.npeo, val)
        
        
    def find_repo_regex(self, collection, val):
        return self.pf.__REGEX__(collection, self.repo, val)
        
        
    def find_prj_regex(self, collection, val):
        return self.pf.__REGEX__(collection, self.prj, val)
        
