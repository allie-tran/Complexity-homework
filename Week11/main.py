import numpy as np
import time
import matplotlib.pyplot as plt


def possible(A, k):
	subset = np.zeros((k + 1, len(A) + 1))
	for i in range(len(A) + 1):
		subset[0, i] = True
	for i in range(1, k + 1):
		subset[i, 0] = False
	for i in range(1, k+1):
		for j in range(1, len(A) + 1):
			subset[i, j] = subset[i, j-1]
			if i >= A[j-1]:
				subset[i, j] = subset[i, j] or subset[i-A[j-1], j-1]

	return subset[k, len(A)]

def plot(data, name=''):

	n = [t[0] * 200 for t in data]
	time = [t[1] * 2e4 for t in data]

	fig, ax = plt.subplots()
	l1, = ax.plot(n, n, label='n')
	l2, = ax.plot(n, time, label='time')
	ax.legend((l1, l2), ('n', 'time'))

	ax.set_xlabel('n', color='0.5')
	ax.set_ylabel('values', color='0.5')  # grayscale color
	ax.set_title(name)
	plt.show()


if __name__ == "__main__":
	# A = [3, 3, 4, 9]
	# print(possible(A, 6))
	data = []

	#Analysis
	for n in range(50, 1001, 50):
		total_time = 0
		for i in range(100):
			A = np.random.randint(501, size=n)
			S = 200
			start = time.time()
			possible(A, S)
			end = time.time()
			total_time += end-start

		data.append((n, total_time))

	plot(data)





