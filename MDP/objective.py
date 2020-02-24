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

class Objective:
    """
    Description
    -----------
        This class provides a generic implementation of MDP immediate cost
        or reward function. This class handles deterministic and 
        stochastic objectives.
    """    
    def __init__(self, sSpace,
                       aSpace,
                       isDeterministic = True,
                       isMinCost = True):
        
        """
        Inputs
        ------
            sSpace [Space]: MDP state space. It is needed mostly to check
                            the feasibility of a state.

            aSpace [Space]: MDP action space. It is needed mostly to check
                            the feasibility of a state.
            
            isDeterministic [bool]: if True, the cost function is deterministic,
                                    else it is stochastic.
            
            isMinCost [bool]: if True, MDP is min-cost, else it is
                              max-reward.    
                              
        Raises/Returns
        --------------
            
        Explanations
        ------------
            The constructor of MDP objective function class.
        """
        
        # assert(isinstance(sSpace,Space))
        # assert(isinstance(aSpace,Space))
        assert(isinstance(isMinCost,bool))
        assert(isinstance(isDeterministic,bool))
        
        self.sSpace = sSpace
        self.aSpace = aSpace
        self.isMinCost = isMinCost
        self.isDeterministic = isDeterministic
    
    def exceptObjective(self,curState,curAction,numNextState=None):
        """
        Inputs
        ------
            curState [list]: current state vector, that is the list of
                             components of the current state.
            
            curAction [list]: current action vector, that is the list of
                             components of the current action.    
                             
            numNextState [int]: if the objective is deterministic, then
                                numNextState should be None. Else, this
                                input shows the number of samples used 
                                for approximating the expected cost/reward.
        Raises/Returns
        --------------
            [float]: cost/expected cost     
        
        Explanations
        ------------
            This function computes cost/expected cost given a state-action pair
            and the number of samples needed for sample average approximation.
        """
        
        assert(self.sSpace.isStateFeasble(curState))
        assert(self.aSpace.isStateActionFeasble(curState,curAction))
        pass
    
        
    def getObjectiveWithExoSamples(self,curState,curAction,exoSamples):
        """
        Inputs
        ------
            curState [list]: current state vector, that is the list of
                             components of the current state.
            
            curAction [list]: current action vector, that is the list of
                             components of the current action.    
                             
            exoSamples [list]: a list of exogenous samples that can be
                               used for sample average approximating the
                               expected cost function.
                
        Raises/Returns
        --------------
            [float]: cost/expected cost     
        
        Explanations
        ------------
            This function computes cost/expected cost given a state-action pair 
            and a list of samples used in sample average approximation.
        """        
        assert(self.sSpace.isStateFeasble(curState))
        assert(self.aSpace.isStateActionFeasble(curState,curAction))
        raise NotImplementedError
    
    
        