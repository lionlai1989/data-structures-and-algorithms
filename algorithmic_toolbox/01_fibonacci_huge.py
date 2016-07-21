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

def get_fibonaccihuge(n, m):
	l = list([])
	remainder = list([])
	l.append(0)
	remainder.append(0)
	l.append(1)
	remainder.append(1)
	
	for i in range(2, n+1):
		l.insert(i, ((l[i-1]%m) + (l[i-2]%m)) % m)
		remainder.append(l[i] % m)
		#print(l)
		#print(remainder[0:i])
		#print(i)
		if((remainder[i-1] == 0) and (remainder[i] == 1) and ((i-1) % 2 == 0) \
			and (remainder[0:(int((i-1)/2))] == remainder[int((i-1)/2):(i-1)])):# and (remainder[0:i/2] == remainder[i/2+1:i])
			#print(int((i-1)/2))
			#print(remainder[0:(int((i-1)/2))])#(int((i-1)/2))
			#print(remainder[3:6])
			#print(remainder[int((i-1)/2):(i-1)])
			period = int((i-1)/2)
			break
		elif i == n:
			return(calc_fib(n) % m)

	#print(period)
	return(remainder[n % period])
	

if __name__ == '__main__':
	input = sys.stdin.readline()
	n, m = map(int, input.split())
	#n = 281621358815590
	#m = 30524
	#n = 20
	#m = 3
	#n = 99999999999999999
	#m = 100000
	print(get_fibonaccihuge(n, m))
