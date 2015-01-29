#!/usr/bin/python

import sys
sys.path.append(sys.path[0] + '/..')
from search.bugFind import bugFind
from search.mailFind import mailFind
from search.logFind import logFind
from search.scriptFind import scriptFind
from search.pyfind import find
import service.mod_config

class cAPI(object):
    
    def __init__(self):
#init find        
        self.bf = bugFind()
        self.lf = logFind()
        self.mf = mailFind()
        self.sf = scriptFind()
        self.pf = find()

#init logFind's var        

        self.svninfo = service.mod_config.getConfig('collection.conf','log','svninfo')
        self.hginfo = service.mod_config.getConfig('collection.conf','log','hginfo')
        self.gitinfo = service.mod_config.getConfig('collection.conf','log','gitinfo')
        self.bazaarinfo = service.mod_config.getConfig('collection.conf','log','bazaarinfo')
        self.log = {}
        self.log['svn'] = self.svninfo
        self.log['hg'] = self.hginfo
        self.log['baz'] = self.bazaarinfo
        self.log['git'] = self.gitinfo
        
#init bugFind's var

        self.bugOne = service.mod_config.getConfig('collection.conf','bug','bugone')
        self.bug = {}
        self.bug['bug1'] = self.bugOne        

#init scriptFind's var
        
        self.scPerl = service.mod_config.getConfig('collection.conf','script','perl')
        self.script = {}
        self.script['perl'] = self.scPerl
        
#getter
                
    def get_bf(self):
        return self.bf
        
    def get_lf(self):
        return self.lf
        
    def get_mf(self):
        return self.mf

    def get_header(self, collection):
        return self.pf.get_header(collection)

#log_info
        
    def log_sp_sc(self, vcs, arg):
        return self.lf.find_span_scope(self.log[vcs], int(arg[0]), int(arg[1]))
        
    def log_sp_lte(self, vcs, arg):
        return self.lf.find_span_lte(self.log[vcs], int(arg[0]))
        
    def log_sp_gte(self, vcs, arg):
        return self.lf.find_span_gte(self.log[vcs], int(arg[0]))
    
        
    def log_bt_sc(self, vcs, arg):
        return self.lf.find_btime_scope(self.log[vcs], int(arg[0]), int(arg[1]))
            
    def log_bt_lte(self, vcs, arg):
        return self.lf.find_btime_lte(self.log[vcs], int(arg[0]))
        
    def log_bt_gte(self, vcs, arg):
        return self.lf.find_btime_gte(self.log[vcs], int(arg[0]))
        
    
    def log_et_sc(self, vcs, arg):
        return self.lf.find_etime_scope(self.log[vcs], int(arg[0]), int(arg[1]))
            
    def log_et_lte(self, vcs, arg):
        return self.lf.find_etime_lte(self.log[vcs], int(arg[0]))
        
    def log_et_gte(self, vcs, arg):
        return self.lf.find_etime_gte(self.log[vcs], int(arg[0]))
        
    
    def log_nc_sc(self, vcs, arg):
        return self.lf.find_ncmt_scope(self.log[vcs], int(arg[0]), int(arg[1]))
            
    def log_nc_lte(self, vcs, arg):
        return self.lf.find_ncmt_lte(self.log[vcs], int(arg[0]))
        
    def log_nc_gte(self, vcs, arg):
        return self.lf.find_ncmt_gte(self.log[vcs], int(arg[0]))
    
    
    def log_np_sc(self, vcs, arg):
        return self.lf.find_npeo_scope(self.log[vcs], int(arg[0]), int(arg[1]))
            
    def log_np_lte(self, vcs, arg):
        return self.lf.find_npeo_lte(self.log[vcs], int(arg[0]))
        
    def log_np_gte(self, vcs, arg):
        return self.lf.find_npeo_gte(self.log[vcs], int(arg[0]))
    
    
    def log_re_re(self, vcs, arg):
        return self.lf.find_repo_regex(self.log[vcs], arg[0])
        
        
    def log_pr_re(self, vcs, arg):
        return self.lf.find_prj_regex(self.log[vcs], arg[0])
        
#bug 

    def bug_sp_sc(self, lev, arg):
        return self.bf.find_span_scope(self.bug[lev], int(arg[0]), int(arg[1]))
        
    def bug_sp_lte(self, lev, arg):
        return self.bf.find_span_lte(self.bug[lev], int(arg[0]))
        
    def bug_sp_gte(self, lev, arg):
        return self.bf.find_span_gte(self.bug[lev], int(arg[0]))
    
        
    def bug_bt_sc(self, lev, arg):
        return self.bf.find_btime_scope(self.bug[lev], int(arg[0]), int(arg[1]))
            
    def bug_bt_lte(self, lev, arg):
        return self.bf.find_btime_lte(self.bug[lev], int(arg[0]))
        
    def bug_bt_gte(self, lev, arg):
        return self.bf.find_btime_gte(self.bug[lev], int(arg[0]))
        
    
    def bug_et_sc(self, lev, arg):
        return self.bf.find_etime_scope(self.bug[lev], int(arg[0]), int(arg[1]))
            
    def bug_et_lte(self, lev, arg):
        return self.bf.find_etime_lte(self.bug[lev], int(arg[0]))
        
    def bug_et_gte(self, lev, arg):
        return self.bf.find_etime_gte(self.bug[lev], int(arg[0]))
        
    
    def bug_nb_sc(self, lev, arg):
        return self.bf.find_nbug_scope(self.bug[lev], int(arg[0]), int(arg[1]))
            
    def bug_nb_lte(self, lev, arg):
        return self.bf.find_nbug_lte(self.bug[lev], int(arg[0]))
        
    def bug_nb_gte(self, lev, arg):
        return self.bf.find_nbug_gte(self.bug[lev], int(arg[0]))
    
    
    def bug_np_sc(self, lev, arg):
        return self.bf.find_npeo_scope(self.bug[lev], int(arg[0]), int(arg[1]))
            
    def bug_np_lte(self, lev, arg):
        return self.bf.find_npeo_lte(self.bug[lev], int(arg[0]))
        
    def bug_np_gte(self, lev, arg):
        return self.bf.find_npeo_gte(self.bug[lev], int(arg[0]))
    
    
    def bug_re_re(self, lev, arg):
        return self.bf.find_repo_regex(self.bug[lev], arg[0])
        
#mail

    
    

        
#script
    
    def sc_na_re(self, lang, arg):
        return self.sf.find_name_regex(self.script[lang], arg[0])
        
    def sc_ca_re(self, lang, arg):
        return self.sf.find_cata_regex(self.script[lang], arg[0])
        
        
      
