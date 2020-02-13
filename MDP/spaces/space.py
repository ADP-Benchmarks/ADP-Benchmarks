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

class Space():
    """
    Description
    -----------
        This class provides a generic implementation of a space. It is used to 
        define the MDP state and action space. I can incorporate continuous and
        discrete states with complex structures.
    """ 
    
    def __init__(self,isContinuous,dim):
        """
        Inputs
        ------
            isContinuous [bool]: if True, Space is treated as continuous, else
                                 it is assumed to be discrete.
                
            dim [int]: the dimensionality of the space.
        Raises/Returns
        --------------
        
        Explanations
        ------------
            The constructor of Space object.
        """
        assert(isinstance(isContinuous,bool))
        assert(isinstance(dim,int))
        assert(dim > 0)
        
        self.isContinuous = isContinuous
        self.dim          = dim  
        
    def sample(self,numSamples=1):
        """
        Inputs
        ------
            numSamples [int]: the number of samples.
            
        Raises/Returns
        --------------
            [list]: a list of samples from the space.
            
        Explanations
        ------------
            This function samples a batch of uniform points in the Space.
        """ 
        raise NotImplementedError
    
        
    def isStateFeasble(self,curState):
        """
        Inputs
        ------
            curState [list]: the current state.
            
        Raises/Returns
        --------------
            [bool]: True if the curState is feasible, False otherwise.
            
        Explanations
        ------------
            Checks if the current state is feasible to MDP state space or not?
        """ 
        raise NotImplementedError
        

    def getObjectiveWithExoSamples(self,curState,curAction):
        """
        Inputs
        ------
            curState [list]: the current state.
            curAction [list]: the current state.
            
        Raises/Returns
        --------------
            [bool]: True if the curAction is a feasible action from state curState,
                    False otherwise.
            
        Explanations
        ------------
            Checks if the current action is feasible from current state or not?
        """ 
        raise NotImplementedError       
        
        
        
        
        
        
        
        