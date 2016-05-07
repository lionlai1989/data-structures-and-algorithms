#!/usr/bin/env python3
import sys
import _edit_distance
#import numpy as np

def optimal_sequence(n):
    # Make a list of minimum number of operantion of 1 to 10e6
    l = [0]
    #l = np.zeros(n)
    for i in range(2, n+1): # i = 2 to 1000000
        #j =  i - 1
        #print('i=', i)
        if i % 3 == 0:
            # i = a > b ? a : b in programming language C
            i = (i // 3) if l[(i//3)-1] < l[(i-1)-1] else i-1 
        elif i % 2 == 0:
            i = (i // 2) if l[(i//2)-1] < l[(i-1)-1] else i-1
        else:
            i = i - 1
        l.append(l[i-1]+1)
        #l[j] = int(l[i-1] + 1)

        #print(i)
        #print(l)
        
    #print(len(l))
    #print((l[96233]))
    #print('done')
   
    sequence = []
    i = None # n % 3
    j = None # n % 2
    k = None # n - 1
    while n >= 1:
        sequence.append(n)
        if n == 1: 
            break
        i = [l[(n//3)-1], (n//3)] if (n % 3 == 0) else [None, None]
        j = [l[(n//2)-1], (n//2)] if (n % 2 == 0) else [None, None]
        k = [l[(n-1-1)], (n-1)]
        #print(i, j, k)
        if i == [None, None] and j != [None, None]:
            #print('1st', min(j, k))
            n = min(j, k)[1]
        elif i != [None, None] and j == [None, None]:
            #print('2nd', min(i, k))
            n = min(i, k)[1]
        elif i != [None, None] and j != [None, None]:
            #print('3th', min(i, j, k))
            n = min(i, j, k)[1]
        else:
            #print('4th', k)
            n = k[1]
        #print(n)
    #print(sequence)    
    return reversed(sequence)

if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
