#Uses python3

import sys

visited = None
count = 1

def explore(adj, v):
    global visited
    global count
    visited[v] = count
    for w in adj[v]:
        if visited[w] == 0:
            explore(adj, w)

def number_of_components(adj):
    global visited
    global count
    result = 0
    for index, item in enumerate(visited):
        if item == 0:
            explore(adj, index)
            count = count + 1
            result = result + 1
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # sys.stdin.read() will read from standard input till EOF.
    # (which is usually Ctrl+D)
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = [0] * n
    print(number_of_components(adj))
