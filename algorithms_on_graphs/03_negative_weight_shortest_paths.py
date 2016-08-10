#!/usr/bin/env python3

import sys
import queue

class Vertex():
    def __init__(self):
        self.value = None   # value of the vertex.
        self.adj = []       # adjacent of the vertex.
        self.group = None   # 
        self.prev = None    # previous vertex
        self.dist = 1e19    # default distance equals to infinitiv, 
                            # it should be bigger than 1e8.
        self.weight = None  # weight of edges.

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    size = len(adj)
    graph = []
    for i in range(size):
        graph.append(Vertex())
    for i in range(size):
        graph[i].value = i
    for i in range(size):
        graph[i].weight = cost[i]
    for i in range(size):
        for j in adj[i]:
            graph[i].adj.append(graph[j])
    graph[s].dist = 0 # set distance of start point as 0.
    distance[s] = 0

    for j in range(2):
        for i in range(size):
            u = graph[i]
            for v_idx, v in enumerate(u.adj):
                #print("u =", u.value, "v =", v.value)
                alt = u.dist + u.weight[v_idx]
                if alt < v.dist:
                    v.dist = alt
                    v.prev = u
                    distance[v.value] = alt

    for i in range(size):
        u = graph[i]
        for v_idx, v in enumerate(u.adj):
            alt = u.dist + u.weight[v_idx]
            if alt < v.dist:
                shortest[u.prev.value] = 0
                tmp = u
                u = u.prev
                while u != tmp:
                    #print("u value =", u.value, "u prev =", u.prev.value, "v prev =", v.prev.value)
                    shortest[u.prev.value] = 0
                    u = u.prev
                
    for i in range(size):
        if graph[i].dist == 1e19:
            reachable[i] = 0
        else:  
            reachable[i] = 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [6, 7, 1, 2, 10, 2, 3, 5, 1, 3, 100, 3, 5, 7, 5, 4, 10, 4, 3, -18, 6, 1, -1, 1] # ans = 0 10 - - - *
    #data = [5, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 3, 1, -5, 4] # ans = - - - 0 *
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [1e19] * n # list is an immutable type in python
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])