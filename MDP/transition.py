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
from MDP.spaces.space import Space

class Transition():
    """
    Description
    -----------
        This class provides a generic implementation of the MDP transition kernel.
        It covers both the MDP transition matrix for discrete MDPs and the 
        probability density defining the next state of a continuous state MDP.
    """ 
    
    def __init__(self,sSpace,aSpace):
        """
        Inputs
        ------
            sSpace [Space]: MDP state space. It is needed mostly to check
                            the feasibility of a state.

            aSpace [Space]: MDP action space. It is needed mostly to check
                            the feasibility of a state.
                            
        Raises/Returns
        --------------
        
        Explanations
        ------------
            The constructor of Space object.
        """
        # assert(isinstance(sSpace,Space))
        # assert(isinstance(aSpace,Space))
        
        self.sSpace = sSpace
        self.aSpace = aSpace

    def getNextState(self, curState,curAction,numNextState=None):
        """
        Inputs
        ------
            curState [list]: current state vector, that is the list of
                             components of the current state.
            
            curAction [list]: current action vector, that is the list of
                              components of the current action.    
                             
            numNextState [int]: if the transition is deterministic, then
                                numNextState should be None. Else, this
                                input shows the number of samples used 
                                for generating the next state.
        Raises/Returns
        --------------
            [list]: a list of next states
        
        Explanations
        ------------
            This function generates a batch of MDP next states.
        """
        
        assert(self.sSpace.isStateFeasble(curState))
        assert(self.aSpace.isStateActionFeasble(curState,curAction))
        
        pass
    
    def getNextStateWithExoSamples(self, curState,curAction,exoSamples):
        """
        Inputs
        ------
            curState [list]: current state vector, that is the list of
                             components of the current state.
            
            curAction [list]: current action vector, that is the list of
                              components of the current action.    
                             
            exoSamples [list]: a list of exogenous samples that can be
                               used for generating the next states.
                               
        Raises/Returns
        --------------
            [list]: a list of next states
        
        Explanations
        ------------
            This function generates a batch of MDP next states.
        """
        assert(self.sSpace.isStateFeasble(curState))
        assert(self.aSpace.isStateActionFeasble(curState,curAction))
        raise NotImplementedError

