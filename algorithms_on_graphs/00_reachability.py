#!/usr/bin/env python3
import sys

def explore(adj, v, visited, count):
    visited[v] = count
    for w in adj[v]:
        if visited[w] is None:
            explore(adj, w, visited, count)

def reach(adj, x, y):
    visited = [None] * len(adj)
    count = 0
    for index, item in enumerate(visited):
        if item is None:
            explore(adj, index, visited, count)
            count = count + 1
    
    if visited[x] == visited[y]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # sys.stdin.read() will read from standard input till EOF.
    # (which is usually Ctrl+D)
    n, m = data[0:2]
    data = data[2:]
    # print(n, m)
    # print(data)
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # previous code transfers start index from 0
    # 4 4       4 4
    # 1 2       0 1
    # 3 2  -->  2 1
    # 4 3  -->  3 2
    # 1 4       0 3
    # 1 4       0 3
    # I think using 0 as start index is better than using 1.
    print(reach(adj, x, y))
