import numpy as np
import math
from mean_sd import get_mean_sd
from variance_cal import calc_var
import scipy.stats as stats


def normal_distribution(X, sample=None):
    if sample:
        mean, sd = get_mean_sd(sample)
    else:
        mean = 0
        sd = 1
    y = (1 / (calc_var(sample) * math.sqrt(2 * math.pi))) * math.exp((-1/2 * (X - mean)**2) / sd)
    return y


def pdf(a, b, sample=None, N=100):
    x = np.linspace(a, b, N)
    f = normal_distribution(x, sample=sample)


def integrate(a, b, N, sample=None):
    x = np.linspace(a + (b-a) / (2 * N), b -(b-a)/(2 * N), N)
    fx = np.sin(x)
    area = np.sum(fx)*(b - a) / N
    return area


print(integrate(0, np.pi/2, 100))
print(stats.norm.pdf(1, 0, 1))
print(stats.norm.cdf(1, 0, 1))

