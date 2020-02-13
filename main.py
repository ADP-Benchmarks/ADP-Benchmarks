#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub Homepage
----------------        
    https://github.com/ADP-Benchmarks

Contact information
-------------------  
    ADP.Benchmarks@gmail.com.

License
-------
    The MIT License  
"""

import numpy as np
from spaces.cube import Cube
from spaces.ball import Ball
from MDP.transition import Transition
from MDP.objective import Objective

"""
Explanations
------------
    The following main function is used for testing different
    components of an MDP.  
"""
if __name__== "__main__":
    
    # Define a cube that is an instance of the "Space" class.
    C = Cube(intervals = np.asarray([[-2,3] , [4,5],
                                     [ 2,3] , [-6,5]]))
    
    # Test a simple implementation of sampling from a cube.
    C.sample(numSamples = 10)
    
    # Define a ball that is an instance of the "Space" class.
    B = Ball(center = np.asarray([1,3,-7]), radius = 2.5)
    
    # As an illustration, we define the following MDP transition kernel.
    T = Transition(C,B)
    
    # MDP cost/reward function can be defined using the "Objective" class.
    cost = Objective(C,C,False,True)
    
    # cost.exceptObjective(1,1)
    
