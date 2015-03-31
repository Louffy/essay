#!/usr/bin/python
#usage: "collection search_cmds(split by " ")"
import sys
from console_api import cAPI

log = ['svn','git','baz','hg']
bug = ['bug1']
script = ['perl']
mail = ['mbox','mman']

class web_api:
	def __init__(self):
		ca = cAPI()
		
	def cmd(c):
	    sp = c[1].split(';')
	    f = sp[0] + '_' + sp[1]
	    if c[0] in log:
	        f = 'log_' + f
	    elif c[0] in bug:
	        f = 'bug_' + f
	    elif c[0] in script:
	        f = 'sc_' + f
	    callf = getattr(ca, f)
	    arg = []
	    for i in range(2, len(sp)):
	        arg.append(sp[i])
	    return callf(c[0], arg)
	        
	def cmds(c):
	    exists = set()
	    ret = []
	    for i in range(1, len(c)):
	        cc = []
	        cc.append(c[0])
	        cc.append(c[i])
	        tmp = cmd(cc)
	        for tt in tmp:
	            if str(tt) in exists:
	                ret.append(tt)
	            else:
	                exists.add(str(tt))
	    return ret        
    
	def commands(c):
	    elif len(c) == 2:        
	        tmp = self.cmd(c)
			return tmp
	    elif len(c) > 2:
	        tmp =  self.cmds(c)
	        return tmp
            

