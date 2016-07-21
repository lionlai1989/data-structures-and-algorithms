#!/usr/bin/env python3
import sys

def min_dot_product(a, b):
    result = 0
    for i in range(len(a)):
        result = result + max(a) * min(b)
        a.remove(max(a))
        b.remove(min(b))
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
