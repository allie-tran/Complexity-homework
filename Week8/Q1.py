import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-A", "--sorted_array", type=int, required=True, nargs='+', help="Input array")
parser.add_argument("-x", "--x", type=int, required=True, help="Element to find")
args = parser.parse_args()


def find(A, x):
	left = 0
	right = len(A) - 1
	while left <= right:
		mid = (left + right) // 2
		if A[mid] == x:
			return mid
		if A[mid] > x:
			right = mid - 1
		else:
			left = mid + 1
	return None


if __name__ == "__main__":
	print "Finding ", args.x, " in the array ", args.sorted_array
	print "Result: ", find(args.sorted_array, args.x)
