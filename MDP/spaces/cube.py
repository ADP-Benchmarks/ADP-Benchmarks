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
from sampling.sampler import CubeSampler

class Cube(Space):
    """
    Description
    -----------
        This class provides an implementation of d-dimensional hypercube.
        A hypercube object can be used to define the MDP state/action space.
    """ 
    
    def __init__(self,intervals,isContinuous=True):
        """
        Inputs
        ------
            intervals [np.ndarray]: intervals define ranges of the hypercube.
                                 For estateample, the following array 
                                 np.asarray([[-2,3] , [4,5], [2,3] , [-6,5]])
                                 defines 4-dimensional hypercube given by
                                 [-2,3]*[4,5]*[2,3]*[-6,5].
                
        Raises/Returns
        --------------
        
        Explanations
        ------------
            The constructor of Cube object.
        """
        
        assert(isinstance(isContinuous,bool))
        assert(isinstance(intervals,np.ndarray))
        
        super(Cube, self).__init__(isContinuous=isContinuous,
                                   dim=intervals.shape[0])
        self.intervals = intervals
        if len(self.intervals.shape) == 1:
            self.low  = self.intervals[0]
            self.high = self.intervals[1]
            self.shape = (1,)
        else:
            self.low  = self.intervals[:,0]
            self.high = self.intervals[:,1]
            self.shape = self.low.shape 
    
    
    def sample(self,numSamples=1):
        """
        Inputs
        ------
            numSamples [int]: the number of samples.
            
        Raises/Returns
        --------------
            [list]: a list of samples from the hypercube. 
            
        Explanations
        ------------
            This function samples a batch of uniform points in a hypercube.
        """ 
        assert(isinstance(numSamples,int))
        return CubeSampler(self).sample(numSamples)
    
    
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
        
        '''
        TODO: 
            my understanding is s is a single state.
            if I'm correct, we may want to add something like s = s.reshape(-1)
        '''
        
        s = np.array(s)  if isinstance(s, list) else s
        return s.shape == self.shape and np.all(s >= self.low) and np.all(s <= self.high)

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
        
        '''
        TODO: 
            I think this is kind of confusing. This function indicates that the state space and the action space 
            are the same since they both use self.low and self.high to judge. But this might not be true.
        '''
        if isinstance(a, list):
            a = np.array(a)  
        elif isinstance(a, int):    
            a = np.array([a])  
        return a.shape == self.shape and np.all(a >= self.low) and np.all(a <= self.high)
        
