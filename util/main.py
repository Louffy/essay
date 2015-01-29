#!/usr/bin/python
import sys
from console_api import cAPI

ca = cAPI()
log = ['svn','git','baz','hg']
bug = ['bug1']
script = ['perl']
mail = ['mbox','mman']

def help():
    print 'exit: '

def usage():
    print 'usage: "collection search_cmds(split by " ")"'

def pr(tmp):
    for t in tmp:
        print t

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
    flag = True
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

print 'You can input command now'
flag = True
while flag:
    cc = raw_input('>>')
    c = cc.split(' ')
    if len(c) == 1:
        if c[0] == 'help':
            help.__call__()
        elif c[0] == 'exit':
            print 'bye'
            sys.exit(0)
        else:
            usage.__call__()
    elif len(c) == 2:        
        tmp = cmd.__call__(c)
        pr(tmp)
    else:
        tmp =  cmds.__call__(c)
        pr(tmp)
            
            
