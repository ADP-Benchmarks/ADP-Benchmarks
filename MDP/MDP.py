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

from MDP.spaces.space import  Space
from MDP.transition import Transition
from MDP.objective import Objective
import copy

class MDP:
    """
    Description
    -----------
        This class provides a generic implementation for continuous- and 
        discrete- state MDPs. Finite and infinite -time horizon MDPs as
        well as average- and discounted- cost MDPs can be handled.
    
    """
    
    def __init__(self,   initState = None,
                         sSpace = None,
                         aSpace = None,
                         nSpace = None,
                         transition = None,
                         objective  = None,
                         isFiniteHorizon = False,
                         isAveCost = False,
                         terminalStates=None,):
        
        """
        Inputs
        ------
            initState [list]: initial state vector, that is the list of
                              components of the starting state.
        
            sSpace [Space]: MDP state space.

            aSpace [Space]: MDP action space.  
            
            nSpace [Space]: MDP exogenous noise space.  
            
            transition [Transition]: MDP stochastic kernel (e.g., MDP 
                                     transition matrix for discrete MDPs).
            
            objective [Objective]: the MDP cost/reward function.
            
            isFiniteHorizon [int]: if int, MDP is finite-time horizon of length
                                   isFiniteHorizon, else if False,
                                   it is infinite-time horizon.
            
            isAveCost [bool]: if True, MDP is average-cost, else it is
                              discounted-cost. 
            
            terminalStates [list]: list of absorbing state for episodic MDPs
                                   
                              
        Raises/Returns
        --------------
            
        Explanations
        ------------
            The constructor of MDP class.
        """
        
        # assert(isinstance(sSpace,Space))
        # assert(isinstance(aSpace,Space))
        # assert(isinstance(nSpace,Space))
        assert(isinstance(transition,Transition))
        assert(isinstance(objective,Objective))  
        assert sSpace.isStateFeasble(initState), 'Intial state should belong to\
                                                  the state space'
        
        #TODO initState -> initDist
        self.initState = initState
        self.terminalStates = terminalStates
        self.sSpace = sSpace
        self.aSpace = aSpace
        self.nSpace = nSpace
        self.sDim = self.sSpace.dim
        self.aDim = self.aSpace.dim
        self.nDim = self.nSpace.dim          
        self.transition = transition
        self.objective = objective
        self.isFiniteHorizon = isFiniteHorizon
        self.isAveCost = isAveCost
        self.reset()
        
        
    def step(self, action, force_noise=None):     
        '''
        Takes one step in the MDP.
        --------------------------
        Inputs
        ------
        action [list]: current action vector, that is the list of
                       components of the current action
           
        force_noise [list]: optional, an exogenous noise vector used to 
                            evaluate next state and reward. If not provided,
                            the noise vector will be sampled randomly
                            
        Returns
        -------
        nextState [list]: next state at t+1
            
        reward [float]: Scalar reward/cost
            
        done [boolean]: True if an absorbing state is reached,
                        for the case of absorbing MDPs
                        
        info [dict]: Provides info about the noise outcome and current period 
                    in the finite horizon case
            
        '''
        
        #TODO This function should support generating a list of next states
        
        if not force_noise:
            noise = self.nSpace.sample()[0]
        else:
            noise = force_noise
            
        nextState = self.transition.getNextStateWithExoSamples(self.currState,
                                                               action,
                                                               noise)
        reward = self.objective.getObjectiveWithExoSamples(self.currState,
                                                      action,
                                                      noise)
        self.currState = nextState
        if self.isFiniteHorizon:
            # Increment the period
            self.t += 1
            if self.t >= self.isFiniteHorizon:
                self.reset()
            return nextState, reward, {'t': self.t, 'noise': noise}
        
        # Infinite horizon MDP    
        elif self.terminalStates:
            done = nextState in self.terminalStates
            return nextState, reward, done, {'noise': noise}            
        else:
            return nextState, reward, {'noise': noise} 
        
        
    def reset(self,):
        '''
        Resets the state back to the initial state
        ------------------------------------------
        
        Returns
        -------
        initState [list]: initial state vector, that is the list of
                          components of the starting state.
                          
        t [int]: starting period t for finit horizon MDPs           
                              
        '''
        self.currState = copy.deepcopy(self.initState)
        if self.isFiniteHorizon:
            self.t = 0
            return (self.currState,self.t)
        else:
            return self.currState
            
            
        
 

           

    
        
        
        
