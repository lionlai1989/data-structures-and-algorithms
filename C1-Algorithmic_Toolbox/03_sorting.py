#!/usr/bin/env python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pass

def partition2(a, l, r):
    #print(a)
    print(l, r)
    tmp = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        print(a, i, j)
        if a[i] <= tmp:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return None
    k = random.randint(l, r)
    print(k, a[l], a[k], a[r])
    a[l], a[k] = a[k], a[l] #swap a[l], a[k]
    print(k, a[l], a[k], a[r])
    #use partition3
    m = partition2(a, l, r)
    print(a)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    n = 7
    a = [7, 6, 5, 4, 3, 2, 1]
    """
    Important NOTE:
    Lists and dicts are mutable objects in python, where as tuples and strings 
    are immutable objects. int is immutable also.
    When passing a mutable objects to func, a reference of it is copied to 
    function. The function change the contents of the objects being passed.
    When passing an immutable objects to func, you pass the object.
    """
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
