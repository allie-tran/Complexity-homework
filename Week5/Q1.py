# Q1
import argparse
import numpy as np
from math import floor, log
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--num", type=int, default=42, nargs='?')
args = parser.parse_args()

def dec_to_bin(n):
	s = ''
	while n > 0:
		s = str(n % 2) + s
		n = n // 2
	return s


def num_assignments(n, verbose=False):
	if verbose:
		num = 1
		print "  s = '':", 1
		print "  There is floor(log(n)) + 2 while loop"
		print "  In each while loop before the last one (where n = 0): 2 assignments"
		print "  In total: 1 + (floor(log2(n)) + 1) * 2, which is :", int(1 + (floor(log(n, 2)) + 1) * 2)

		while n > 0:
			num += 2
			n = n // 2

		print "  Real result: ", num
		return num

	else:
		return int(1 + (floor(log(n, 2)) + 1) * 2)

def num_comparisons(n, verbose=False):
	if verbose:
		print "  There is floor(log(n)) + 2 while loop"
		print "  In each while loop: 1 comparison"
		print "  In total: floor(log2(n)) + 2, which is :", int(floor(log(n, 2)) + 2)

		num = 0
		while n > 0:
			n = n // 2
			num += 1
		num += 1

		print "  Real result: ", num
		return num
	else:
		return int(floor(log(n, 2)) + 2)


def plot():
	x = np.linspace(10, 1000, 20)
	asgm = [num_assignments(n) for n in x]
	compa = [num_comparisons(n) for n in x]
	log2 = [log(n, 2) for n in x]

	fig, ax = plt.subplots()
	l1, = ax.plot(x, log2, '.', label='log2')
	l2, = ax.plot(x, asgm, '.', label='assignments')
	l3, = ax.plot(x, compa, '.', label='comparisons')
	ax.legend((l1, l2, l3), ('log2', 'assignments', 'comparisons'))

	ax.set_xlabel('n', color='0.5')
	ax.set_ylabel('values', color='0.5')  # grayscale color
	plt.show()


def run(n):
	print("""-------------------------
def dec_to_bin(n):
	s = ''
	while n > 0:
		s = str(n % 2) + s
		n = n // 2
	return s
-------------------------""")

	print 'Binary number ', dec_to_bin(n)
	print 'Number of assignments:'
	num_assignments(n, verbose=True)
	print 'Number of comparisons: '
	num_comparisons(n, verbose=True)

	plot()


if __name__ == '__main__':
	run(args.num)
