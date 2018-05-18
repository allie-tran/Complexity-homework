import numpy as np
import matplotlib.pyplot as plt
import time
import json
from math import log

def naive_multiply(A, B, n):
	C = np.zeros((n, n))
	for i in range(n):
		for j in range(n):
			for k in range(n):
				C[i, j] += A[i, k] * B[k, j]
	return C

def Strass_multiply(A, B, n):
	if n == 1:
		return np.ones((1, 1)) * A[0, 0] * B[0, 0]
	assert n % 2 == 0, "Only applicable for n = 2^q"
	k = n/2
	A11 = A[:k, :k]
	A12 = A[:k, k:]
	A21 = A[k:, :k]
	A22 = A[k:, k:]

	B11 = B[:k, :k]
	B12 = B[:k, k:]
	B21 = B[k:, :k]
	B22 = B[k:, k:]

	P1 = Strass_multiply(A11 + A22, B11 + B22, k)
	P2 = Strass_multiply(A21 + A22, B11, k)
	P3 = Strass_multiply(A11, B12 - B22, k)
	P4 = Strass_multiply(A22, B21 - B11, k)
	P5= Strass_multiply(A11 + A12, B22, k)
	P6 = Strass_multiply(A21 - A11, B11 + B12, k)
	P7 = Strass_multiply(A12 - A22, B21 + B22, k)

	C = np.zeros((n, n))
	C[:k, :k] = P1 + P4 - P5 + P7
	C[:k, k:] = P3 + P5
	C[k:, :k] = P2 + P4
	C[k:, k:] = P1 + P3 - P2 + P6
	return C

def plot(data, name=''):

	n = [t[0] for t in data]
	n3 = [t[0] ** 3 for t in data]
	nlog7 = [t[0] ** log(7, 2) for t in data]
	time1 = [t[1] for t in data]
	time2 = [t[2] for t in data]
	fig, ax = plt.subplots()
	l1a, = ax.plot(n, n3, label='n3')
	l1b, = ax.plot(n, nlog7, label='nlog7')
	l2, = ax.plot(n, time1, label='traditional')
	l3, = ax.plot(n, time2, label='Strass')
	ax.legend((l1a, l1b, l2, l3), ('n3', 'nlog7', 'traditional', 'Strass'))

	ax.set_xlabel('n', color='0.5')
	ax.set_ylabel('values', color='0.5')  # grayscale color
	ax.set_title(name)
	plt.show()

if __name__ == "__main__":
	# Test case
	print 'Test case for n = 4'
	n = 4
	N = 1000
	A = np.random.randint(N, size=(n, n)) + 1
	B = np.random.randint(N, size=(n, n)) + 1
	print A , '*', B
	print 'Traditional method result: '
	print naive_multiply(A, B, n)
	print 'Strass method result: '
	print Strass_multiply(A, B, n)

	# Analysis
	time_naive = []
	time_Strass = []
	data = []
	for k in range(10, 32):
		n = 2**k
		N = 1000
		A = np.random.randint(N, size=(n, n)) + 1
		B = np.random.randint(N, size=(n, n)) + 1
		# print a
		# print b
		start = time.time()
		naive_multiply(A, B, n)
		end1 = time.time()
		Strass_multiply(A, B, n)
		end2 = time.time()
		data.append([n, (end1 - start), (end2 - end1)])

	# Save data
	with open('real_time_result.txt', 'w') as f:
		json.dump(data, f)

	# Rescaling for plotting
	for i in range(len(data)):
		data[i][1] = data[i][1] * 1e5
		data[i][2] = data[i][2] * 1e5

	# Plot
	plot(data, 'Comparison between two methods')

