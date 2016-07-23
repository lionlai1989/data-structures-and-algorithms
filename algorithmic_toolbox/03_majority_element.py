#!/usr/bin/env python3
import sys

class elem:
    def __init__(self):
        self.value = None
        self.count = 0

def get_majority_element(a, number):
    maj_element = None
    count = 1
    for i in a:
        if maj_element == i:
            count = count + 1
        else: 
            count = count - 1
        if count == 0:
            maj_element = i
            count = 1
    if a.count(maj_element) > (number/2):
        return 0
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n = 11
    #a = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]
    #n = 6
    #a = [2, 3, 9, 2, 2, 9]
    #n = 4
    #a = [1, 2, 3, 1]
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
