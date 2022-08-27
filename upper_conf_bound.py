import numpy as np

NUM_TRIALS = 100000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class Bandit:
  def __init__(self, p):
    self.p = p # win rate
    self.p_estimate = 0.
    self.N = 0. 
    
  def pull(self):
    return np.random.random() < self.p

  def update(self, x):
    self.N += 1.
    self.p_estimate = ((self.N - 1)*self.p_estimate + x) / self.N
    
