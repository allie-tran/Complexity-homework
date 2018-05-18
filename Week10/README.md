## `Q1.py`
*Command-line example*:
>python `Q1.py`

This will show the result of the test case for `n = 4` and run the code for the analysis of cases from `2^10` to `2^32`, expecting **long** running time.

The following is the proof for the complexity of two methods:
#### Traditional method

```python
def naive_multiply(A, B, n):
	C = np.zeros((n, n))
	for i in range(n): # Loop1
		for j in range(n): # Loop2
			for k in range(n): # Loop3
				C[i, j] += A[i, k] * B[k, j]
	return C
```
The first command for creating `C` contains $$n^2$$ assignments.
For each loop in loop3, 1 addition is made. There are $$n$$ loop3s in each loop2, and there are $$n$$ loop2s in each loop1. Thus the total number of additions is $$n^3$$. Thus the complexity of this method is $$O(n^3)$$.

#### Strass method
Let $$T(n)$$ be the total calculations made for the case of matrices of size $$n * n$$.
If $$n = 1$$, there is 1 calculation to be made, thus $$T(1) = 1$$.
For case $$n$$, we have:
$$T(n)= 7T(n/2) + Cn^2$$,
with $$Cn^2$$ is the time for making matrix additions.
With $$n = 2^k$$, we have
$$T(n) = T(2^k) = 7T(2^{k-1}) + C.2^{2k}) = 7T(2^{k-1}) + C.4^{k})
= 7^2T(2^{k-2}) + C.7.4^{k-1} + C.4^2k
= ... = 7^k + C\sum_{i=0}^{k-1}7^i.4^{k-i} = O(7^k) = O(7^{logn}) = O(n^{log7})







