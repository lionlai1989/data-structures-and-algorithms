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

detect_bipartite = 1

def search(node, v, queue):
    global detect_bipartite
    for w in v.adj:
        if node[w].layer == None:
            node[w].layer = v.layer + 1
            queue.append(w)
        if node[w].layer !=  None and abs(v.layer - node[w].layer) % 2 == 0:
            detect_bipartite = 0

def bfs(node, v):
    queue = []
    v.group = bfs.group
    #shortest_path_tree T = empty
    search(node, v, queue)
    while len(queue) != 0:
        w = queue.pop(0)
        search(node, node[w], queue)

def bipartite(adj):
    bfs.group = 0
    node = []
    for i in range(len(adj)):
        node.append(Node())
    for i in range(len(adj)):
        node[i].key = i
    for i in range(len(adj)):
        node[i].adj = adj[i]

    for n in node:
        if n.layer == None:
            bfs.group += 1
            n.layer = 0
            bfs(node, n) # start point from node[u]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    #n, m = 5, 4
    #data = [5, 2, 4, 2, 3, 4, 1, 4]
    #n, m = 4, 4
    #data = [1, 2, 4, 1, 2, 3, 3, 1]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    bipartite(adj)
    print(detect_bipartite)
