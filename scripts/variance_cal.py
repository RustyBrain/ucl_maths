import numpy as np


def calc_var(sample):
    mean = np.mean(sample)
    size = len(sample)
    total = 0
    for i in sample:
        total += (i - mean)**2
    return total/(size - 1)
