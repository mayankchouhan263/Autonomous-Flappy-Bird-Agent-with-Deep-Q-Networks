from collections import deque
import random

class ReplayMemory():
    
    # create FIFO queue - experience replay
    # Seed is for random samples 
    def __init__(self, maxlen, seed=None):
        self.memory = deque([], maxlen=maxlen)

    # Add elements func
    def append(self, new_exp):
        self.memory.append(new_exp)

    # Get random samples
    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)

    # current buffer size
    def __len__(self):
        return len(self.memory)