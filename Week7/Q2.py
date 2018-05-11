from random import randint
import argparse
import time
import math

import matplotlib.pyplot as plt
from sympy import *
from numpy import zeros, random


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n", type=int, default=4, nargs='?')
parser.add_argument("-a", "--a", type=str, default='1234', nargs='?')
parser.add_argument("-b", "--b", type=str, default='4321', nargs='?')
args = parser.parse_args()

# a.
def multiply_tradi(a, b, n):
    results = zeros(2*n)
    i_a = 0
    # From right to left in a
    while i_a < len(a):
        n1 = int(a[-i_a -1])

        # From right to left in b:
        carry = 0
        i_b = 0
        while i_b < len(b):
            n2 = int(b[-i_b - 1])

            sum = results[i_a + i_b] + n1 * n2 + carry
            print ''.join(str(int(digit)) for digit in results[::-1])
            carry = sum // 10
            results[i_a + i_b] += sum % 10

            i_b += 1

        results[i_a + i_b - 1] += carry
        i_a += 1

    # Remove '0's from the front
    start = 0
    results = results[::-1]
    while results[start] == 0.0:
        start += 1
        if start >= len(results):
            return '0'
    return ''.join([str(int(digit)) for digit in results[start:]])

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
    print 'Test case for ', a, ' * ', b
    print 'Using traditional method: ', multiply_tradi(a, b, n)
    print 'Using new method: ', multiply_new(1234, 4321, n)

    # # Analysis
    # time_tradi = []
    # time_new = []
    # for k in range(10, 33):
    #     a = random.randint(0, 9, 2 ** k)
    #     b = random.randint(0, 9, 2 ** k)
    #     start = time.time()
    #     multiply_tradi(a, b, k)
    #     end1 = time.time()
    #     multiply_new(a, b, k)
    #     end2 = time.time()
    #     time_tradi.append(end1 - start)
    #     time_new.append(end2 - end1)
    #
    # print 'Average time for traditional method: ', sum(time_tradi)/len(time_tradi)
    # print 'Average time for new method: ', sum(time_new)/len(time_new)
    #
    # print '=' * 80
    # print 'Proving the first method has a complexity of O(n^2)'
    # print """def multiply_tradi(a, b, n):
    # result = 0                       --> 1 assignment
    # place = 1                        --> 1 assignment
    # while b > 0:                     --> n + 1 comparisons, n loops
    #     last_digit = b % 10               --> 1 assignment
    #     result  += last_digit * a * place --> 1 assignment
    #     place *= 10                       --> 1 assignment
    #     b /= 10                           --> 1 assignment
    #
    # return result"""
    #
    # print '-' * 80
    # print 'Total: 2 + 4(n + 1) = 4n + 4 assignments, n+1 comparisons'
