import numpy as np
import math
import functools


def factorial(n):
    if n < 2:
        return 1
    return functools.reduce(lambda x, y: x * y, range(2, int(n) + 1))


def binom_prob(successes, probability_success_per_trial, number_of_trials, polarity='lower'):
    x = 1 - probability_success_per_trial
    a = number_of_trials - successes
    b = successes + 1
    c = a + b - 1
    prob = 0
    for j in range(a, c + 1):
        prob += factorial(c) / (factorial(j) * factorial(c - j)) * x**j * (1 - x)**(c - j)
    if polarity == 'lower':
        return prob
    elif polarity == 'higher':
        return 1 - prob


print(binom_prob(17, 0.2, 100))
