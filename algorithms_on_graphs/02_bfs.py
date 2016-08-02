#!/usr/bin/env python3

import sys
import queue

class Node():
    def __init__(self):
        self.key = None
        self.adj = None
        self.layer = None
        self.group = None
        self.prev = None

def search(node, v, queue):
    for w in v.adj:
        if node[w].layer == None:
            node[w].layer = v.layer + 1
            queue.append(w)

def bfs(node, v):
    queue = []
    v.group = bfs.group
    #shortest_path_tree T = empty
    search(node, v, queue)
    while len(queue) != 0:
        w = queue.pop(0)
        search(node, node[w], queue)

def distance(adj, start, end):
    bfs.group = 0
    node = []
    for i in range(len(adj)):
        node.append(Node())
    for i in range(len(adj)):
        node[i].key = i
    for i in range(len(adj)):
        node[i].adj = adj[i]

    node[start].layer = 0
    bfs(node, node[start]) # start point from node[u]

    if node[end].layer == None: # It means start can not connect to end.
        return -1
    else:
        return node[end].layer - node[start].layer # start in on layer 0.

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    '''
    n, m = 4, 4 # ans = 2
    data = [1, 2, 4, 1, 2, 3, 3, 1]
    #n, m = 7, 7 
    #data = [1, 5, 2, 5, 5, 7, 2, 7, 3, 4, 3, 6, 1, 3]
    '''
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    u, v = data[2 * m] - 1, data[2 * m + 1] - 1
    #u, v = 1, 3
    #u, v = 1, 3
    print(distance(adj, u, v))
