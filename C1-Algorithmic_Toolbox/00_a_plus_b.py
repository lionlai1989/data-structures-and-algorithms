#!/usr/bin/env python3
import sys

input = sys.stdin.readline()
tokens = input.split()
a = int(tokens[0])
if a < 0:
	sys.exit(0)
b = int(tokens[1])
if b > 9:
	sys.exit(0)
print(a + b)
