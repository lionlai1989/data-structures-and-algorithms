#!/usr/bin/env python3

import sys

sys.setrecursionlimit(200000)

class Node():
    def __init__(self): 
        self.key = None
        self.pre = 0
        self.post = 0
        self.group = None
        self.adj = None

def dfs(node, v, group):
    dfs.clock += 1
    v.pre = dfs.clock
    v.group = group
    for w in v.adj:
        #print(w)
        if node[w].pre == 0:
            dfs(node, node[w], group)
        elif node[w].pre != 0 and node[w].post == 0:
            dfs.detect_cycle = 1

    dfs.clock += 1
    v.post = dfs.clock

def number_of_strongly_connected_components(adj):
    dfs.number_of_SCC = 0
    dfs.detect_cycle = 0
    dfs.clock = 0
    group = 0
    node = []
    for i in range(len(adj)):
        node.append(Node())
    for i in range(len(adj)):
        node[i].key = i
    for i in range(len(adj)):
        node[i].adj = adj[i]

    for n in node:
        if n.pre == 0:
            group += 1
            dfs(node, n, group)

    result = 0
    return result    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
