#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:28:41 2020

@author: parshan
"""
from discreteSpace import DiscreteSpace
from continuousSpace import ContinuousSpace

class Space:
    
    def __init__(self):
        self.dSpace = None
        self.cSpace = None
        self.dDim = None
        self.cDim = None
        
    def setSpaces(self,dSpace=None,cSpace=None):
        if not dSpace is None:
            assert isinstance(dSpace, DiscreteSpace)
            self.dSpace = dSpace
            self.dDim = dSpace.dim
            
        if not cSpace is None:
            assert isinstance(cSpace, ContinuousSpace)
            self.cSpace = cSpace
            self.cDim = cSpace.dim

if __name__== "__main__":
    s = Space()
    s.setSpaces(DiscreteSpace(),ContinuousSpace())
    