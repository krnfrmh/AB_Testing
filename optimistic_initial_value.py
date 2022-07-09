import matplotlib.pyplot as plt
import numpy as np

NUM_TRIALS = 10000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class Bandit:
  
  def __init__(self, p):
    self.p = p
    self.p_estimate = 5
    self.N = 1
