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
equations = []
for j, pair in enumerate(pairs):
    equations.append(Fn.subs('n', pair[0]) - pair[1])
    if j >= alpha :
        test_case = pairs[j + 1]
        break
results = solve(equations)
Fn = Fn.subs(results)
print(results)
assert Fn.subs('n', test_case[0]) == test_case[1], 'fn doesn\'t have the form of O(n^alpha)'
