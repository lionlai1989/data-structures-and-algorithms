#!/usr/bin/env python3
import sys

def gcd(a, b):
	#print(a, b)
	if b == 0:
		return a
	else:
		a_prime = a % b
	return gcd(b, a_prime)

def lcm(a, b):
	#print(a, b)
	return int(a * int(b / gcd(a, b)))

if __name__ == '__main__':
	input = sys.stdin.readline()
	a, b = map(int, input.split())
	print(lcm(a, b))