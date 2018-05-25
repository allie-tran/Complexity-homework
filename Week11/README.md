## Knapsack problem

*Command-line example*:
> python main.py

```python
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
```


Let subset\[i,j\] indicates that there is a subset from A\[0:j-1\] forming the sum of i.
Then we have: if subset\[i, j-1\] is True, subset\[i,j\] is also True. In this case, the subset doesn't include A\[j-1\]. In the other hand, if subset\[i - A\[j-1\], j-1\] is True, A\[i,j\] is also true. In this case, A\[i, j\] is included in the subset.

In the case of i=0, an empty set will satisfy the condition. Thus, A\[0,i\] = True.
In the case of j=0, an empty set will not satisfy any condition with i != 0. Thus, A\[i, 0\] = False for all i!=0.

The complexity of this algorithm is O(n*k).

