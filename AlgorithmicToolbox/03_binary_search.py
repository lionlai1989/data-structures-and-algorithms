#!/usr/bin/env python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    while left <= right:
        mid = left + (right-left)//2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1

def binary_search_index(a, x, first_index):
    if len(a) == 0:
        return -1
    else:
        mid = len(a)//2
        if a[mid] == x:
            return first_index+mid
        elif x < a[mid]:
            return binary_search_index(a[:mid], x, first_index)
        else:
            return binary_search_index(a[mid+1:], x, first_index+mid+1)
    
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [5, 1, 5, 8, 12, 13, \
    #        5, 8, 1, 23, 1, 11]
    #data = [10, 1, 5, 8, 12, 13, 100, 501, 999, 1045, 2000, \
    #        10, 8, 1, 1, 150, 100, 502, 501, 2000, 12, 2001]
    #data = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \
    #        12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #print(n, m, a)
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
        #print(binary_search_index(a, x, 0), end = ' ')
        