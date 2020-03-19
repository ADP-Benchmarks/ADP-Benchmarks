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
        
        '''
        TODO: 
            shall we consider latin hypercube sampling? it is more uniformly distributed in high dimesion.
        '''
        
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
        self.dim = ball.dim
        self.shape = ball.shape
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
        
        def random_vector_in_unit_ball():
            """
            Returns
            --------------
                [ndarray] numSamples random points in a unit ball.
            
            Explanations
            ------------
                The algorithm is according to Theorem 1 of https://arxiv.org/pdf/math/0503650.pdf 
            """
            x = np.random.normal(loc=0.0, scale=1.0, size=(numSamples, self.dim))
            z = np.random.exponential(scale=1.0, size=(numSamples,))
            d = (np.sum(np.square(x), axis=1) + z) ** 0.5
            d = d[:, np.newaxis]
            return x / d
        
        unit_sample = random_vector_in_unit_ball()
        sample = unit_sample * self.radius + self.center
        if self.isContinuous:
            return sample.tolist()
        else:
            sample_center_zero = sample - self.center
            sample_center_zero_discrete = sample_center_zero.astype(int) # remove the decimal directly
            sample_discrete = sample_center_zero_discrete + self.center
            return sample_discrete