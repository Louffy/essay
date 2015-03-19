#!/usr/bin/python

import sys
from pyupdate import update
sys.path.append(sys.path[0] + '/..')
import service.mod_config

dict_vcs = {'svn':'svn_info', 'git':'git_info', 'hg':'hg_info', 'bazaar':'baz_info'}
dic_header = {'vc':'vcs', 're':'repo', 'pr':'prj', 'np':'n_peo', 'nc':'n_cmt', 'bt':'b_time', 'et':'e_time', 'sp':'span', 'll':'log_loc', 'sl':'src_loc'}

class logUpdate:

    def __init__(self):
        self.up = update()
    
    def update_log(self, vcs, ids, arg):
    	tran_arg = self.translate_arg(arg)
    	return self.up.update(dict_vcs[vcs], ids, tran_arg)

    def translate_arg(self, arg):
    	sp = arg.split(';')
    	size = len(sp) / 2
    	tran_arg = {}
    	for i in range(0, size):
    		key = dic_header[sp[i*2]]
    		val = sp[i*2+1]
    		tran_arg[key] = val
    	return tran_arg