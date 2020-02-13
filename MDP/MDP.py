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

from spaces.space import  Space
from transition import Transition
from objective import Objective

class MDP:
    """
    Description
    -----------
        This class provides a generic implementation for continuous- and 
        discrete- state MDPs. Finite and infinite -time horizon MDPs as
        well as average- and discounted- cost MDPs can be handled.
    
    """
    
    def __init__(self,   sSpace = None,
                         aSpace = None,
                         transition = None,
                         objective  = None,
                         ifFiniteHorizon = False,
                         isAveCost = False):
        
        """
        Inputs
        ------
            sSpace [Space]: MDP state space.

            aSpace [Space]: MDP action space.  
            
            transition [Transition]: MDP stochastic kernel (e.g., MDP 
                                     transition matrix for discrete MDPs).
            
            objective [Objective]: the MDP cost/reward function.
            
            ifFiniteHorizon [bool]: if True, MDP is finite-time horizon,
                                    else it is infinite-time horizon.
            
            isAveCost [bool]: if True, MDP is average-cost, else it is
                              discounted-cost.    
                              
        Raises/Returns
        --------------
            
        Explanations
        ------------
            The constructor of MDP class.
        """
        
        assert(isinstance(sSpace,Space))
        assert(isinstance(aSpace,Space))
        assert(isinstance(transition,Transition))
        assert(isinstance(objective,Objective))        
        
        self.sSpace = sSpace
        self.aSpace = aSpace
        self.sDim = self.sSpace.dim
        self.aDim = self.aSpace.dim        
        self.transition = transition
        self.objective = objective
        self.isFiniteHorizon = ifFiniteHorizon
        self.isAveCost = isAveCost
 
       

    
        
        
        
