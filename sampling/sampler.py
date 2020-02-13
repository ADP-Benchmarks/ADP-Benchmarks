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

from numpy import asarray
from scipy.stats import uniform


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
        self.dim       = cube.dim
        self.isContinuous = cube.isContinuous
        
    
    def sample(self,numSamples):
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
        if self.isContinuous:
            return asarray([list(uniform(self.intervals[i][0],
                                         self.intervals[i][1]).rvs(numSamples))
                            for i in range(self.dim)]
                           ).T
        else:
            raise NotImplementedError   

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