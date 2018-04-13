# Q1
import random
import argparse
import numpy as np
from math import floor, log
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--test_n", type=int, default=42, nargs='?')
parser.add_argument("-k", "--test_k", type=int, default=200, nargs='?')
parser.add_argument("-a", "--test_a", type=int, default=10, nargs='?')
parser.add_argument("-b", "--test_b", type=int, default=40, nargs='?')
args = parser.parse_args()


def analyse(k, n, a, b, verbose=False):
	A = [random.randrange(k) for _ in range(n)]
	if verbose:
	   print 'k, n, a, b = ',k, n, a, b
	   print A
	count = 0
	for e in A:
	   if a <= e and e <= b:
		   count += 1
	return count


def num_assignments(k, n, a, b, verbose=False):
	count = analyse(k, n, a, b, verbose)

	if verbose:
		print 'Tao mang A: ', n
		print 'count = 0: ', 1
		print 'So vong lap for: ', n
		print 'Trong moi vong lap for: count = ', count
		print 'Tong cong: ', n + 1 + count

	return n + 1 + count



def num_comparisons(k, n, a, b, verbose=False):
	if verbose:
		print 'So vong lap for: ', n
		print 'Trong moi vong lap for: count = ', 2
		print 'Tong cong: ', n * 2
	return n * 2


def plot(data, name=''):
	x = list(range(len(data)))

	asgm = [t[0] for t in data]
	compa = [t[1] for t in data]
	sum = [t[2] for t in data]

	fig, ax = plt.subplots()
	l1, = ax.plot(x, sum, label='n+k')
	l2, = ax.plot(x, asgm, label='assignments')
	l3, = ax.plot(x, compa, label='comparisons')
	ax.legend((l1, l2, l3), ('n+k', 'assignments', 'comparisons'))

	ax.set_xlabel('n', color='0.5')
	ax.set_ylabel('values', color='0.5')  # grayscale color
	ax.set_title(name)
	plt.show()

def run():

	num_assignments(args.test_k, args.test_n, args.test_a, args.test_b, True)
	num_comparisons(args.test_k, args.test_n, args.test_a, args.test_b, True)

	# Co dinh k = 100
	data_k = []
	k = 100
	a = args.test_a
	b = args.test_b
	for n in range(10, 10000, 10):

	   data_k.append([num_assignments(k, n, a, b),\
					num_comparisons(k, n, a, b),\
					n + k])

	plot(data_k, 'Variable n')

	# Co dinh n = 20000
	data_n = []
	n = 20000
	for k in range(10, 10000, 10):
	   data_n.append([num_assignments(k, n, a, b),\
					num_comparisons(k, n, a, b),\
					n + k])

	plot(data_n, 'Variable k')

if __name__ == '__main__':
	run()
