#!/usr/bin/env python3
import sys

def explore(adj, v, visited, count):
    visited[v] = count
    for w in adj[v]:
        if visited[w] is None:
            explore(adj, w, visited, count)

def number_of_components(adj):
    visited = [None] * len(adj)
    count = 0
    for index, item in enumerate(visited):
        if item is None:
            explore(adj, index, visited, count)
            count = count + 1
    
    return count

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
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
