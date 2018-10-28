import math
import numpy as np


def get_mean_sd(sample):
    mean = np.mean(sample)
    n = len(sample)
    standard_deviation = 0
    if n == 0:
        standard_deviation = 0
    else:
        for x in sample:
            standard_deviation += (x - mean) ** 2
        standard_deviation = math.sqrt(standard_deviation / (n - 1))
    return mean, standard_deviation