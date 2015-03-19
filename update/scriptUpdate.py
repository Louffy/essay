#!/usr/bin/python

import sys
from pyupdate import update
sys.path.append(sys.path[0] + '/..')
import service.mod_config

dic_header = {'na':'name', 'lo':'loc', 'ca':'cate', 'in':'in', 'ou':'out', 'de':'des'}

class scriptUpdate:

    def __init__(self):
        self.up = update()
    
    def update_perl(self, ids, arg):
    	tran_arg = self.translate_arg(arg)
    	return self.up.update('script_perl', ids, tran_arg)

    def translate_arg(self, arg):
    	sp = arg.split(';')
    	size = len(sp) / 2
    	tran_arg = {}
    	for i in range(0, size):
    		key = dic_header[sp[i*2]]
    		val = sp[i*2+1]
    		tran_arg[key] = val
    	return tran_arg