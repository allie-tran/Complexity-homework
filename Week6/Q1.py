from random import randint
import argparse
import time
import math

import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n", type=int, default=20, nargs='?', help="For one case testing")
parser.add_argument("-x", "--x", type=int, default=50, nargs='?')
args = parser.parse_args()


def binary_search(array, target):
	if target < 0:
		return -1
	l = 0
	r = len(array) - 1
	# print(array)
	while l <= r:
		mid = int((l+r)/2)
		if array[mid] < target:
			l = mid + 1
		elif array[mid] > target:
			r = mid - 1
		else:
			return mid
	return -1


def find_pairs(A, x):
	sorted_A, indices = (list(t) for t in zip(*sorted(zip(A, range(len(A))))))
	for l in range(len(A) - 1):
		r = len(A)
		need = x - sorted_A[l]
		j = binary_search(sorted_A[l:r], need)
		if j == -1:
			continue
		else:
			return indices[l], indices[l+j]

	return -1, -1


def plot(data, name=''):
	x = list(range(10, 1000, 10))

	time = [t[0] for t in data]
	nlogn = [t[1] for t in data]

	fig, ax = plt.subplots()
	l1, = ax.plot(x, nlogn, label='nlogn')
	l2, = ax.plot(x, time, label='time')
	ax.legend((l1, l2), ('nlogn', 'time'))

	ax.set_xlabel('n', color='0.5')
	ax.set_ylabel('values', color='0.5')  # grayscale color
	ax.set_title(name)
	plt.show()



if __name__=='__main__':
	# for testing
	print "-" * 80
	print "For one-case testing"
	A = [randint(1, 100) for _ in range(args.n)]
	print "A = ", A
	pos = find_pairs(A, args.x)
	if pos == (-1, -1):
		print "Not found"
	else:
		print "Found a pair at position", pos[0], "and", pos[1], "which is", A[pos[0]], "and", A[pos[1]]

	# for time analysis
	print "-" * 80
	print "Complexity analysing..."
	print "-" * 80
	print "Proving the correctness"
	print "First we use a sorting algorithm to sort the array."
	print "For example, I choose Merge Sort for the complexity of O(nlog(n))"
	print "Using the sorted array, for each 'for' loop, we perform a Binary Search " \
	      "for the complementry element or element l (left)" \
	      " in the remaining array."
	print "If the x - A[l] is found at position j in Binary Search, then A[l] + A[l+j] = A[l] + x - A[l] = x"
	print "-" * 80
	print "Empirical results (the running time is scaled up) is shown in the plot."
	data = []
	for n in range(10, 1000, 10):
		times = []
		for i in range(100):
			A = [randint(1, 10000) for _ in range(n)]
			start = time.time()
			find_pairs(A, args.x)
			end = time.time()
			times.append(float(end - start))

		data.append((sum(times)/len(times), n * math.log(n)))
	scale = data[-1][1] / data[-1][0]
	scaled_data = [(x * scale, y) for (x,y) in data]
	plot(data, 'Scaled running time VS. nlog(n)')