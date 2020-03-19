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

from MDP.spaces.space import Space
import numpy as np
from numpy import ndarray
from sampling.sampler import BallSampler

class Ball(Space):
    """
    Description
    -----------
        This class provides an implementation of d-dimensional balls.
        A ball object can be used to define the MDP state/action space.
    """   
    def __init__(self,center,radius,isContinuous=True):
        """
        Inputs
        ------
            center [ndarray]: the vector defining center of the ball.
            
            radius [float]: the radius of the ball.
            
            isContinuous [bool]: if True, the ball is considered as a
                                 continuous set, else it is treated as a
                                 discrete set
            
        Raises/Returns
        --------------
            
            
        Explanations
        ------------
            The constructor of Ball object.
        """
        
        assert(isinstance(isContinuous,bool))
        assert(isinstance(center,ndarray))
        assert(center.ndim==1)
        assert(isinstance(radius,float))  
        assert(radius>=0)
        
        super(Ball,self).__init__(isContinuous,center.shape[0])
        
        self.center = center
        self.radius = radius
        self.shape = center.shape
    
    def sample(self,numSamples=1):
        """
        Inputs
        ------
            numSamples [int]: the number of samples.
            
        Raises/Returns
        --------------
            [list]: a list of samples from the ball.
            
        Explanations
        ------------
            This function samples a batch of uniform points in a ball.
        """
        
        assert(isinstance(numSamples,int))
        return BallSampler(self).sample(numSamples)
        
    def isStateFeasble(self, s):
        """
        Inputs
        ------
            s [list]: state vector.
            
        Raises/Returns
        --------------
            [bool]: True if the state is feasible, False otherwise.
            
        Explanations
        ------------
            Checks if the provided state is feasible in the MDP state space 
        """ 
        
        s = np.array(s) if isinstance(s, list) else s
        return s.shape == self.shape and np.sum(np.square(s - self.center)) <= self.radius ** 2

    def isStateActionFeasble(self, s, a):
        """
        Inputs
        ------
            s [list]: the state vecor.
            
            a [list]: the action vector
            
        Raises/Returns
        --------------
            [bool]: True if the provided action is feasible, False otherwise.
            
        Explanations
        ------------
            Checks if the current action is feasible in the given state
        """ 
        if isinstance(a, list):
            a = np.array(a)  
        elif isinstance(a, int):    
            a = np.array([a])  
        pass
        