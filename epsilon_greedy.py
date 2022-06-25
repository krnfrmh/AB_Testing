from __future__ import print_function, division
from builtins import range
import matplotlib.pyplot as plt
import numpy as np

NUM_TRIALS = 10000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class BanditArm:
  
  def __init__(self, p):
    # p: the win rate
    self.p = p
    self.p_estimate = 0.
    self.N = 0 # num samples collected so far

  def pull(self):
    # draw a 1 with probability p
    return np.random.random() < self.p

  def update(self, x):
    self.N += 1.
    self.p_estimate = ((self.N - 1)*self.p_estimate + x) / self.N
    
def choose_random_argmax(a):
  idx = np.argwhere(np.amax(a) == a).flatten()
  return np.random.choice(idx)

def experiment():
  bandits = [BanditArm(p) for p in BANDIT_PROBABILITIES]

  rewards = np.zeros(NUM_TRIALS)
  num_times_explored = 0
  num_times_exploited = 0
  num_optimal = 0
  optimal_j = np.argmax([b.p for b in bandits])
  
  for i in range(NUM_TRIALS):

    # use epsilon-greedy to select the next bandit
    if np.random.random() < EPS:
      num_times_explored += 1
      j = np.random.randint(len(bandits))
    else:
      num_times_exploited += 1
      j = choose_random_argmax([b.p_estimate for b in bandits])
      
    x = bandits[j].pull()
    # update rewards
    rewards[i] = x

    # update the distribution for the bandit whose arm we pulled
    bandits[j].update(x)
