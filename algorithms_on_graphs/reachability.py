#Uses python3

import sys

visited = None

def explore(adj, v):
    global  visited
    visited[v] = 1
    for w in adj[v]:
        if visited[w] == 0:
            explore(adj, w)

def reach(adj, x, y):
    global  visited
    '''
    print('adj =', adj)
    print('x =', x)
    print('y =', y)
    '''
    explore(adj, x)
    if visited[y] == 1:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
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
    visited = [0] * n
    print(reach(adj, x, y))
