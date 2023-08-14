#!/usr/bin/env python3

from collections import defaultdict
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
#n, m = 5, 5
#lines = [1, 1, 1, 1, 1]
#n, m = 6, 4
#lines = [10, 0, 5, 0, 3, 3]
#n, m = 10, 6
#lines = [2, 3, 0, 1, 4, 5, 8, 3, 4, 2]

lines.insert(0, 0)
rank = [1] * (n+1)
parent = defaultdict(list)
root = defaultdict(list)

def make_set(i):
    parent[i] = i
    rank[i] = 0

    root[i] = 0

def find(i):
    #while i != parent[i]:
    #    i = parent[i]
    #return i
    if i != parent[i]:
        #print(i)
        parent[i] = find(parent[i])

    return parent[i]

def getParent(i):
    # find parent and compress path
    i = find(i)
    return i

def union(i, j):
    if i == j:
        return
    '''
    if rank[i] > rank[j]:
        lines[i] = lines[i] + lines[j]
        lines[j] = 0
        parent[j] = i
        root.pop(j)
        
    else:
        parent[i] = j
        lines[j] = lines[j] + lines[i]
        lines[i] = 0
        root.pop(i)
        if rank[i] == rank[j]:
            rank[j] += 1
    '''
    lines[i] = lines[i] + lines[j]
    lines[j] = 0
    parent[j] = i
    root.pop(j)

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    union(realDestination, realSource)
    
    return True



#if __name__ == '__main__':
def main():
    for i in range(1, n+1):
        make_set(i)
    #print(parent)
    #print(rank)
    #print(lines)
    #print(root)
    tmp = []
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        merge(destination, source)
        #print(parent)
        #print(lines)
        a = list(root.keys())

        tmp.append(max([lines[j] for j in a]))
    #print(root)
    for i in tmp:
        print(i)

threading.Thread(target=main).start()