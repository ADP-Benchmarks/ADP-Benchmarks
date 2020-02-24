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
from MDP.spaces.cube import Cube
from MDP.spaces.ball import Ball
from MDP.transition import Transition
from MDP.objective import Objective
from MDP.MDP import MDP

"""
Explanations
------------
    The following main function is used for testing different
    components of an MDP.  
"""
if __name__== "__main__":
    
    # Define a cube that is an instance of the "Space" class.
    C = Cube(intervals = np.asarray([[-2,3] , [4,6],
                                     [ 2,3] , [-6,5]]), isContinuous=True)
    
    # Test a simple implementation of sampling from a cube.
    C.sample(numSamples = 10)
    
    # Define a ball that is an instance of the "Space" class.
    B = Ball(center = np.asarray([1,3,-7]), radius = 2.5)
    
    # As an illustration, we define the following MDP transition kernel.
    T = Transition(C,B)
    
    # MDP cost/reward function can be defined using the "Objective" class.
    cost = Objective(C,C,False,False)
    
    # cost.exceptObjective(1,1)
    
    # Define a cube state space
    sC = Cube(intervals = np.asarray([[0,10] , [0,10],
                                     [ 0,10] , [0,10]]), isContinuous=False)
    # Define action space
    aC = Cube(intervals = np.asarray([[0,5],[0,5],[0,5],[0,5]]), isContinuous=False) 
    
    # Define exogenous noise space
    nC = Cube(intervals = np.asarray([[0,8],[0,8],[0,8],[0,8]]), isContinuous=False)  
    
    # As an illustration, we define the following MDP transition kernel.
    T = Transition(sC,aC)
    
    # MDP cost/reward function can be defined using the "Objective" class.
    O = Objective(sC,aC,False,False)
    
    # Construct a finite horizon MDP 
    mdp =  MDP( initState = np.array([5,5,5,5]),
                sSpace = sC,
                aSpace = aC,
                nSpace = nC,
                transition = T,
                objective  = O,
                isFiniteHorizon = 10,
                isAveCost = False,
                terminalStates=None)
    
    
    
