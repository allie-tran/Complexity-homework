import random
import time
import matplotlib.pyplot as plt
from math import log

# Using quicksort
def find_kth_smallest_value(S, k, left, right):
	# If k is smaller than the number of elements in S
	if 0 < k < len(S):
		S, pos = partition(S, left, right)
		# Partition the array around last element and get position of pivot element in sorted array

		# If position is the same as k
		if pos - left == k - 1:
			return S[pos]
		# If position is more, recur for left subarray
		if pos - left > k - 1:
			return find_kth_smallest_value(S, k, left, pos - 1)
		else:
			return find_kth_smallest_value(S, k - (pos - left + 1), pos + 1, right)

	return None


def partition(S, left, right):
	x = S[right]
	i = left
	for j in range(left, right):
		if S[j] < x:
			S[i], S[j] = S[j], S[i]
			i += 1
	S[i], S[right] = S[right], S[i]
	return S, i

def plot(data, name=''):
	x = list(range(10, 100, 10))

	time = [t[0] for t in data]
	n = [t[1] for t in data]
	nlogn = [t[2] for t in data]
	fig, ax = plt.subplots()
	l1, = ax.plot(x, time, label='time')
	l2, = ax.plot(x, n, label='n')
	l3, = ax.plot(x, nlogn, label='nlogn')
	ax.legend((l1, l2, l3), ('time', 'n', 'nlogn'))

	ax.set_xlabel('n', color='0.5')
	ax.set_ylabel('values', color='0.5')  # grayscale color
	ax.set_title(name)
	plt.show()


if __name__ == "__main__":

	k = 5
	data = []
	for N in range(10, 100, 10):
		t = 0
		for repeat in range(100):
			S = random.sample(set(range(1, 1001)), N)
			start = time.time()
			find_kth_smallest_value(S, k, 0, len(S)-1)
			end = time.time()
			t += end - start
		data.append((t * 1e4, N, N*log(N)))

	plot(data, 'Comparison between real times and different estimations')
	print "The time complexity is estimated to be O(n) on average."

