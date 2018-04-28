from random import randint
import argparse
import time
import math

import matplotlib.pyplot as plt
from sympy import *
from numpy import log


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fn", type=str, default='n^3 + n^2 + n + 1', nargs='?', help="For one case testing")
parser.add_argument("-a", "--a", type=int, default=10, nargs='?')
parser.add_argument("-b", "--b", type=int, default=1000, nargs='?')
args = parser.parse_args()

n = Symbol('n')
fn = sympify(args.fn)
a = args.a
b = args.b

# Get the (n - f(n)) pairs
pairs = [(n, fn.subs('n', n)) for n in range(a, b + 1)]
# Estimate alpha
alphas = [log(float(pair[1])) / log(float(pair[0])) for pair in pairs if pair[0] != 1 and pair[1] > 0]
alpha = int(sum(alphas)/ len(alphas))
print 'Alpha ~', alpha
# Find the function a0 + a1*x + ... + a_alpha x^alpha
Fn = 0
for i in range(alpha + 1):
    ai = Symbol('a'+str(i))
    Fn += ai * Symbol('n') ** i

print(Fn)
# Solve equations for a_k
equations = []
test_case = None
for j, pair in enumerate(pairs):
    equations.append(Fn.subs('n', pair[0]) - pair[1])
    if j >= alpha:
        test_case = pairs[j + 1]
        break
# If there are fewer instance of (n, f(n)) than the amount needed to solve for a_k, get more pairs
if test_case is None:
    more_data = alpha + 1 - len(pairs)
    more_pairs = []
    while len(more_pairs) < more_data:
        b += 1
        if fn.subs('n', b) > 0:
            more_pairs.append((b, fn.subs('n', b)))
    for j, pair in enumerate(more_pairs[:-1]):
        equations.append(Fn.subs('n', pair[0]) - pair[1])

    test_case = more_pairs[-1]

results = solve(equations)
Fn = Fn.subs(results)
if Fn.subs('n', test_case[0]) == test_case[1]:
    print(results)
else:
    print('fn doesn\'t have the form of O(n^alpha)')
