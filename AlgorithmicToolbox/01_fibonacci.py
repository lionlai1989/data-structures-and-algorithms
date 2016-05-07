#!/usr/bin/env python3
import sys

def calc_fib(n):
	l = list([])
	l.append(0)
	l.append(1)
	for i in range(2, n+1):
		l.insert(i, l[i-1] + l[i-2])
	#print(l)
	return l[n]
	
n = int(input())
print(calc_fib(n))
