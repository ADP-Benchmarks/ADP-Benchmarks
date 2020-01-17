#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:39:02 2020

@author: parshan
"""
from continuousSpace import ContinuousSpace
from numpy import ndarray


class Ball(ContinuousSpace):
    
    def __init__(self):
        self.center = None
        self.radius = None
        self.norm   = None
    
    def defBall(self,center,radius,norm):
        assert isinstance(center, ndarray) or isinstance(center, list)
        assert isinstance(radius, float) or isinstance(radius, int)
        assert (callable(norm))
        
        
    
if __name__== "__main__":
    s = Ball()
    s.defBall([0], 2, abs)