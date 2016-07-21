#!/usr/bin/env python3
import numpy as np

def recursive_edit_distance(x, y, memo=None):
	# it's code from internet, do not use, just a reminder.
	'''
    if len(x) == 0:
    	return len(y)
    if len(y) == 0:
    	return len(x)
    delt = 1 if x[-1] != y[-1] else 0
    diag = edit_distance(x[:-1], y[:-1]) + delt
    vert = edit_distance(x[:-1], y) + 1
    horz = edit_distance(x, y[:-1]) + 1
    return min(diag, vert, horz)
    
	if memo == None:
		memo = {}
	if len(x) == 0:
		return len(y)
	if len(y) == 0:
		return len(x)
	if (len(x), len(y)) in memo:
		return memo[(len(x), len(y))]
	delt = 1 if x[-1] != y[-1] else 0
	diag = edit_distance(x[:-1], y[:-1], memo) + delt
	vert = edit_distance(x[:-1], y, memo) + 1
	horz = edit_distance(x, y[:-1], memo) + 1
	ans = min(diag, vert, horz)
	memo[(len(x), len(y))] = ans
	return ans
	'''
	pass

def edit_distance(x, y):
	m = len(x)
	n = len(y)
	arr = np.zeros(shape=(m+1, n+1))
	#print(arr.shape)
	for i in range(m+1):
		arr[i, 0] = i
	for i in range(n+1):
		arr[0, i] = i
	for i in range(1, m+1):
		for j in range(1, n+1):
			insertion = arr[i, j-1] + 1
			deletion = arr[i-1, j] + 1
			match = arr[i-1, j-1]
			mismatch = arr[i-1, j-1] + 1
			#print(i, j)
			if x[i-1] == y[j-1]:
				arr[i, j] = min(insertion, deletion, match)
			else:
				arr[i, j] = min(insertion, deletion, mismatch)
			#print(i, j)
	return int(arr[m, n])
	

if __name__ == "__main__":
	print(edit_distance(input(), input()))
