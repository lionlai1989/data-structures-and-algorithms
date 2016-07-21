#!/usr/bin/env python3
import sys

n = int(input())
input = sys.stdin.readline()
tmp = input.split()
a = [int(x) for x in tmp]
assert(len(a) == n)

result = 0
tmp1st = max(a)
a.remove(tmp1st)
tmp2nd = max(a)
'''
for i in range(0, n):
    if a[i]*tmp > result:
        result = a[i]*tmp
'''
result = tmp1st * tmp2nd
print(result)
