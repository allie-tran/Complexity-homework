from random import randint
import argparse
import time
import math

import matplotlib.pyplot as plt
from sympy import *
from numpy import zeros


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n", type=int, default = 4, nargs='?')
parser.add_argument("-a", "--a", type=int, default=1234, nargs='?')
parser.add_argument("-b", "--b", type=int, default=4321, nargs='?')
args = parser.parse_args()



# a.
def multiply_tradi(a, b, n):
    result = 0
    place = 1
    while b > 0:
        last_digit = b % 10
        result  += last_digit * a * place
        place *= 10
        b /= 10

    return result

# b
def multiply_new(a, b, n):
    assert n % 2 == 0, 'Please enter an even number of n'

    a1 = a / 10 ** int(n/2)
    b1 = b / 10 ** int(n/2)
    a2 = a % 10 ** int(n / 2)
    b2 = b % 10 ** int(n / 2)

    c = a1 * b1
    d = a2 * b2
    e = (a1 + a2) * (b1 + b2) - c - d

    return c * 10 ** n + e * 10 ** int(n/2) + d

if __name__ == "__main__":
    # Test case
    n = args.n
    a = args.a
    b = args.b
    print('Test case for ', a, ' * ', b)
    print('Using traditional method: ', multiply_tradi(a, b, n))
    print('Using new method: ', multiply_new(a, b, n))

    # Analysis
    n = 2 ** 10
    for k in range(10, 33):
        a = randint()