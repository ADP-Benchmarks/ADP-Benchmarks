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
# from scipy.stats import uniform


class CubeSampler():
    """
    Description
    -----------
        This class provides an implementation of a uniform sampling from a hypercube.
    """     
    def __init__(self,cube):
        """
        Inputs
        ------
            cube [Cube]: a Cube object
                
        Raises/Returns
        --------------
        
        Explanations
        ------------
            The constructor of CubeSampler object.
        """
        
        self.intervals = cube.intervals
        self.low = cube.low
        self.high = cube.high
        self.dim       = cube.dim
        self.shape = cube.shape
        self.isContinuous = cube.isContinuous
        
    
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
        
        sample = np.random.uniform(low=self.low, 
                                   high=self.high,
                                   size=(numSamples,self.shape[0])) 
        if self.isContinuous:
            # return np.asarray([list(uniform(self.intervals[i][0],
            #                               self.intervals[i][1]).rvs(numSamples))
            #                 for i in range(self.dim)]
            #                 ).T
            
            # vectorized sampling
            # widths = self.high - self.low
            # return self.low + widths*np.random.uniform(
            #                               size=(numSamples, self.shape[0]))
            return sample
        
        else:

            sample = np.floor(sample)

            return sample.astype('int32')            

class BallSampler():
    """
    Description
    -----------
        This class provides an implementation of a uniform sampling from a ball.
    """      
    def __init__(self, ball):
        """
        Inputs
        ------
            ball [Ball]: a Ball object
                
        Raises/Returns
        --------------
        
        Explanations
        ------------
            The constructor of BallSampler object.
        """
        
        self.center = ball.center
        self.radius = ball.radius
        self.isContinuous = ball.isContinuous
    
    
    def sample(self,numSamples):
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
        if self.isContinuous:
            raise NotImplementedError
        else:
            raise NotImplementedError