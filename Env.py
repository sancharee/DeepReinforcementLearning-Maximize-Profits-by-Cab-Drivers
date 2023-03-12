# Import routines

import numpy as np
import math
import random
from itertools import permutations

# Defining hyperparameters
m = 5 # number of cities, ranges from 0 ..... m-1
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [(0,0)] + list(permutations([i for i in range(m)], 2))
        self.state_space = [(X,T,D) for X in range(m) for T in range(t) for D in range(d)]
        self.state_init = random.choice(self.state_space)

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        state_encod = [0] * (m + t + d)
        state_encod[state[0]] = 1 
        state_encod[m+state[1]] = 1
        state_encod[m+t+state[2]] = 1
        return state_encod

    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 0:
            requests = np.random.poisson(2)
        elif location == 1:
            requests = np.random.poisson(12)
        elif location == 2:
            requests = np.random.poisson(4)
        elif location == 3:
            requests = np.random.poisson(7)
        elif location == 4:
            requests = np.random.poisson(8)

        if requests >15:
            requests =15

        possible_actions_index = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_index]        
        actions.append((0,0))
        possible_actions_index.append(0) # appending index for (0,0) action
        return possible_actions_index,actions   

    
    def time_day_update_func(self, time, day, ride_duration):
        """Takes current time of the day, the current day of the week and the ride_duration and returns the time and day post ride."""
        day = (day + ((time + ride_duration) // t)) % d
        time = (time + ride_duration) % t
        return time, day

    
    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        curr_loc, curr_time, curr_day = state
        pickup_loc, drop_loc = action
        
        if action == (0,0):
            reward = -1 * C
        
        else:
            # time from curr_loc to reach pickup_loc
            t1 = int(Time_matrix[curr_loc][pickup_loc][curr_time][curr_day])
            curr_time, curr_day = self.time_day_update_func(curr_time, curr_day, t1)
            # time from pickup_loc to reach drop_loc
            t2 = int(Time_matrix[pickup_loc][drop_loc][curr_time][curr_day])
            
            reward = (R * t2) - (C * (t1 + t2))
        
        return reward


    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        curr_loc, curr_time, curr_day = state
        pickup_loc, drop_loc = action
        
        rewards = self.reward_func(state, action, Time_matrix)
        total_time = 0
        
        if action == (0,0):
            # update time by 1 hour
            curr_time, curr_day = self.time_day_update_func(curr_time, curr_day, 1)
            next_state = (curr_loc, curr_time, curr_day)
            total_time = 1
        else:
            # time from curr_loc to reach pickup_loc
            t1 = int(Time_matrix[curr_loc][pickup_loc][curr_time][curr_day])
            curr_time, curr_day = self.time_day_update_func(curr_time, curr_day, t1)
            
            # time from pickup_loc to reach drop_loc
            t2 = int(Time_matrix[pickup_loc][drop_loc][curr_time][curr_day])
            curr_time, curr_day = self.time_day_update_func(curr_time, curr_day, t2)
               
            total_time = t1 + t2
            next_state = (drop_loc, curr_time, curr_day)
        
        return next_state, rewards, total_time


    def reset(self):
        return self.action_space, self.state_space, self.state_init
