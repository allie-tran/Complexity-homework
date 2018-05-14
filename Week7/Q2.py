from random import randint
import argparse
import time
import math

import matplotlib.pyplot as plt
from sympy import *
from numpy import zeros, random, append


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n", type=int, default=4, nargs='?')
parser.add_argument("-a", "--a", type=str, default='123', nargs='?')
parser.add_argument("-b", "--b", type=str, default='123', nargs='?')
args = parser.parse_args()


# a.
def padding(a, b):
    n = max(len(a), len(b))
    if n == 0:
        return 0, a, b
    while len(a) < n:
        a = "0" + a
    while len(b) < n:
        b = "0" + b
    return n, a, b


def multiply_tradi(a, b):
    n, a, b = padding(a, b)
    result = zeros(2*n)
    i_a = 0
    # From right to left in a
    while i_a < len(a):
        n1 = int(a[-i_a - 1])

        # From right to left in b:
        carry = 0
        i_b = 0
        while i_b < len(b):
            n2 = int(b[-i_b - 1])

            sum = result[i_a + i_b] + n1 * n2 + carry
            carry = sum // 10
            result[i_a + i_b] = sum % 10

            i_b += 1

        result[i_a + i_b - 1] += carry
        i_a += 1

    # Remove '0's from the front
    start = 0
    result = result[::-1]
    while result[start] == 0.0:
        start += 1
        if start >= len(result):
            return '0'
    return ''.join([str(int(digit)) for digit in result[start:]])

# b
def add(a, b):

    n, a, b = padding(a, b)
    result = zeros(n)
    i = 0
    carry = 0
    while i < n:
        n1 = int(a[-i - 1])
        n2 = int(b[-i - 1])
        sum = n1 + n2 + carry
        result[i] = sum % 10
        carry = sum // 10
        i += 1
    if carry > 0:
        result = append(result, [carry])

    # Remove '0's from the front
    start = 0
    result = result[::-1]

    while result[start] == 0.0:
        start += 1
        if start >= len(result):
            return '0'
    # print a, '+', b, '=', ''.join([str(int(digit)) for digit in result[start:]])
    return ''.join([str(int(digit)) for digit in result[start:]])


def subtract(a, b):
    n, a, b = padding(a, b)
    # print a, '-', b
    result = zeros(n)
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    i = 0
    while i < n:
        n1 = a[-i - 1]
        n2 = b[-i - 1]
        diff = n1 - n2
        if diff >= 0:
            result[i] = diff
        else:
            j = i + 2
            while j <= len(a):
                a[-j] = a[-j] - 1
                if a[-j] != 9:
                        break
                else:
                    j += 1
            result[i] = diff + 10
        i += 1

    # Remove '0's from the front
    start = 0
    result = result[::-1]

    while result[start] == 0.0:
        start += 1
        if start >= len(result):
            return '0'
    # print ' = ', ''.join([str(int(digit)) for digit in result[start:]])
    return ''.join([str(int(digit)) for digit in result[start:]])


def multiply_new(a, b):
    if a == '0' or b == '0' or a == '' or b == '':
        return '0'

    n, a, b = padding(a, b)
    if n == 1:
        # print a, '*', b, '=', str(int(a) * int(b))
        return str(int(a) * int(b))

    a1 = a[:-int(n/2)]
    a2 = a[-int(n/2):]
    b1 = b[:-int(n/2)]
    b2 = b[-int(n/2):]

    c = multiply_new(a1, b1)
    d = multiply_new(a2, b2)
    e = multiply_new(add(a1, a2), add(b1, b2))
    e = subtract(e, c)
    e = subtract(e, d)

    result = add(add(c + ''.join(['0'] * (2 * int(n/2))), e + ''.join(['0'] * int(n/2))), d)
    # print a, '*', b, '=', result
    return result


def plot(data, name=''):

	n = [t[0] for t in data]
	time2 = [t[1] for t in data]
	time1 = [t[2] for t in data]
	fig, ax = plt.subplots()
	l1, = ax.plot(n, n, label='n')
	l2, = ax.plot(n, time2, label='time1')
	l3, = ax.plot(n, time1, label='time2')
	ax.legend((l1, l2, l3), ('n', 'time1', 'time2'))

	ax.set_xlabel('n', color='0.5')
	ax.set_ylabel('values', color='0.5')  # grayscale color
	ax.set_title(name)
	plt.show()


if __name__ == "__main__":
    # Test case
    n = args.n
    a = args.a
    b = args.b
    print 'Test case for ', a, ' * ', b
    print 'Using traditional method: ', multiply_tradi(a, b)
    print 'Using new method: ', multiply_new(a, b)
    #
    # Analysis
    time_tradi = []
    time_new = []
    data = []
    for k in range(10, 1000):
        a = ''.join([str(x) for x in random.randint(0, 9, 2**k)])
        b = ''.join([str(x) for x in random.randint(0, 9, 2**k)])
        # print a
        # print b
        start = time.time()
        multiply_tradi(a, b)
        end1 = time.time()
        multiply_new(a, b)
        end2 = time.time()
        data.append((k, (end1 - start) * 1e5, (end2 - end1) * 1e4))

    plot(data)

