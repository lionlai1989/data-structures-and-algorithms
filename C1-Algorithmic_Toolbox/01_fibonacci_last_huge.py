#!/usr/bin/env python3
import sys

def get_fibonacci_last_digit(n):
	l = list([])
	l.append(0)
	l.append(1)
	for i in range(2, n+1):
		l.insert(i, ((l[i-1]%10) + (l[i-2]%10)) % 10)
	#print(l)
	return (l[n])

if __name__ == '__main__':
	input = sys.stdin.readline()
	n = int(input)
	print(get_fibonacci_last_digit(n))
