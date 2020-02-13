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

from spaces.space import Space
from numpy import ndarray
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
            intervals [ndarray]: intervals define ranges of the hypercube.
                                 For example, the following array 
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
        assert(isinstance(intervals,ndarray))
        
        super(Cube, self).__init__(isContinuous=isContinuous,
                                   dim=intervals.shape[0])
        self.intervals = intervals
    
    
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
        
