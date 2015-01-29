#!/usr/bin/python

import sys
from pyfind import find
sys.path.append(sys.path[0] + '/..')
import service.mod_config

class scriptFind:

    def __init__(self):
        self.pf = find()
    
    
    def find_cata_regex(self, collection, val):
        return self.pf.__REGEX__(collection, 'cata', val)  
    
    
    def find_name_regex(self, collection, val):
        return self.pf.__REGEX__(collection, 'name', val)
        
    
