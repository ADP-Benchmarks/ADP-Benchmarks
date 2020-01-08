# %% Load Prequisites
import numpy as np
import copy
from gym import spaces
from gym.utils import seeding

# %% Create MDP Class
class MDP(object):
    """
    Creates a Markov Decision Process problem.
    
    TODO: Environment to compute policy for. Must have nS and nA as attributes
    and state and action spaces like open ai gym.
     
    Parameters
    ----------
    init_state:  (int) or (np.ndarray) 
        Initial state each episode starts from
    trans_func: (function) or (dict) or (np.ndarray) or (list) 
        Transition function that governs the states evolution. Takes a state,
        action, and a noise outcome as parameters. Returns the next state.
    reward_func: (function) or (dict) or (np.ndarray) or (list) 
         TODO Convex/ non-convex
        Reward function. Takes a state, action, and a noise outcome
        as parameters. Returns a scalar.
    states: (np.ndarray) or (list), optional
        This parameter can be specified for tabular MDPs to define the 
        state space.
    actions: (np.ndarray) or (list), optional
        This parameter can be specified for tabular MDPs to define the 
        action space.
    noise: (Python class) TODO should be made optional
        Class to define the exogenuous random variable. Must have a sample 
        method, see example noise class defined below.
    finite_horizon: (int), optional
        Sets the horizon length of the problem is an integer is provided.
        Else, the MDP is assumed to have an infinite horizon.
    terminal_states: (list), optional
        Sets the terminal states in case of a episodic/SSP problems.
    discount_factor: (float)
        Discount factor. Number in range [0, 1]
    """
    def __init__(self,
                 init_state,
                 trans_func,
                 reward_func,
                 states=None,
                 actions=None,
                 noise=None,
                 finite_horizon=None,
                 terminal_states=None,
                 discount_factor=0.99,
                ):
        # Set initial state
        self.init_state = init_state
        # Set current state as the initial state
        self.curr_state = copy.deepcopy(self.init_state)
        # Set discount factor (required for algorithms)
        self.discount_factor = discount_factor
        # Set exogenous random variable class
        self.noise = noise()
        # Check finite/infinite horizon MDP & set horizon length in former case
        self.finite_horizon = finite_horizon
        # Set starting period to zero for the finite horizon case
        self.t = 0
        # Set terminal states
        self.terminal_states = terminal_states
        
        # Check transition function 
        if isinstance(trans_func, dict) or isinstance(trans_func, list) \
            or isinstance(trans_func, np.ndarray):
            self.trans_func = trans_func
            # Tabular MDP
            self.Tabular = True
        # If transition function is a python function    
        elif hasattr(trans_func, '__call__'):
            self.trans_func = trans_func
            # NonTabular MDP
            self.Tabular = False
            
        # Check reward function 
        if isinstance(reward_func, dict) or isinstance(reward_func, list) \
            or isinstance(reward_func, np.ndarray):
            self.reward_func = reward_func
            # Tabular MDP
            self.Tabular = True
        # If transition function is a python function    
        elif hasattr(reward_func, '__call__'):
            self.reward_func = reward_func
            # NonTabular MDP
            self.Tabular = False
        
        if isinstance(actions, list) or isinstance(actions, np.ndarray):
            # if actions is a list or ndarray, all states have the same actions
            self.actions = list(actions)
            
        elif isinstance(actions, int):
            # if actions is an integer,  all states have the same actions 
            # from 0 to len(actions)-1
            self.actions = np.arange(actions).tolist()

        elif isinstance(actions, dict):
            # if actions is a dict, different actions for each state
            self.actions = actions
        else:
            # if actions = None
            self.actions = actions
        
 

    def step(self, action, force_noise=None):
        '''
        Takes one step in the MDP.

        Parameters
        ----------
        action : TYPE
            DESCRIPTION.
        force_noise : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        next_state:
            State at t+1.
        reward: (float)
            Scalar reward
        done: (boolean)
            True if an absorbing state is reached, for the case of absorbing 
            MDPs.
        info: (dict)
            Provides info about the noise outcome and current period in finite
            horizon case
        '''
        #TODO assert self.action_space.contains(action)
        if not force_noise:
            noise = self.noise.sample()
        else:
            noise = force_noise

        print(self.curr_state, action, noise)
        self.curr_state = self.trans_func(self.curr_state, action, noise)

        reward = self.reward_func(self.curr_state, action, noise)
           
        if self.finite_horizon:
            # Increment the period
            self.t += 1
            t = self.t
            curr_state = self.curr_state
            if self.t >= self.finite_horizon:
                self.reset()
            return curr_state, reward, {'t': t, 'noise': noise}
        

        # If infinite horizon and episodic MDP    
        elif self.terminal_states:
            done = self.curr_state in self.terminal_states
            return self.curr_state, reward, done, {'noise': noise}            
        else:
            return self.curr_state, reward, {'noise': noise}
         
        
    
    def reset(self,):
        '''Resets the state back to the initial state'''
        self.curr_state = copy.deepcopy(self.init_state)
        if self.finite_horizon:
            self.t = 0
            return (self.curr_state,self.t)
        else:
            return self.curr_state
    
    def sample(self, parameter_list):
        pass

    def seed(self, seed=None):
        ''' Sets the seed for the envirnment'''
        self.noise.np_random, seed = seeding.np_random(seed)
        return [seed] 
    
    def render(self,):
        '''
        Renders the environment
        '''
        pass


# Testing
    
# %% Create Example: infinite horizon 
class ex_noise_class():
    
    def __init__(self, seed=None):
        self.np_random, self.seed = seeding.np_random(seed)
        
    def sample(self,):
        return self.np_random.randint(0,21)

def ex_reward_func(state, action, noise):
    return 3*min(state + action, noise) - 1*action

def ex_trans_func(state, action, noise):
    return state + action - noise        
        
ex_init_state = 20

m = MDP(ex_init_state, ex_trans_func, ex_reward_func, noise=ex_noise_class)
       
# %% Create Example: finite horizon 
n = MDP(ex_init_state, ex_trans_func, 
        ex_reward_func, noise=ex_noise_class,
        finite_horizon=3)
# %% Create Example: SSP
ex_SSP_init_state=0
def ex_SSP_reward_func(state, action, noise):
    if state==4:    
        return 1
    else:
        return 0

def ex_SSP_trans_func(state, action, noise):
    print(state, action, noise)
    if state==4:
        return 4 
    else:
        if state==0 and action==0:
            if noise==0:
                return 0
            elif noise==1:
                return 1
        elif state==0 and action==1:
            if noise==0:
                return 1
            elif noise==1:
                return 0            
        elif 1 <= state < 4 and action==1:
            if noise==0:
                return state + 1
            if noise==1:
                return state - 1
        elif 1<= state < 4 and action==0:
            if noise==0:
                return state - 1
            if noise==1:
                return state + 1
            
states=np.arange(5)
actions=[0,1] # 0 is left and 1 is right
finite_horizon=None
ex_SSP_terminal_states=[4]
class ex_SSP_noise_class():
    def __init__(self, seed=None):
        self.np_random, self.seed = seeding.np_random(seed)
    def sample(self,):
        return self.np_random.choice(2, p=[0.8, 0.2])

ssp = MDP(ex_SSP_init_state,
          ex_SSP_trans_func, 
          ex_SSP_reward_func, 
          noise=ex_SSP_noise_class,
          terminal_states=ex_SSP_terminal_states,
          finite_horizon=None,)    
    