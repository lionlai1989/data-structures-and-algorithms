#!/usr/bin/env python3

import sys
import math
import operator

class Vertex():
    def __init__(self):
        self.value = None   # value of the vertex.
        self.pos = None
        self.adj = []       # adjacent of the vertex.
        self.group = None   # 
        self.prev = None    # previous vertex
        # default distance equals to infinitiv, 
        # it should be bigger than 1e8.
        # Don't use 1e19, there would be some problems of stack overflow.
        self.dist = float('inf')   
        self.weight = None  # weight of edges.
        self.layer = None

class Edge():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def clustering(x, y, k):
    size = len(x)
    graph = []
    result = 0.
    # make G graph.
    for i in range(size):
        graph.append(Vertex())
        graph[i].value = i
        graph[i].pos = [x[i], y[i]]
    # foreach v ∈ G.V, make_set(v)
    s = [] 
    for v in graph:
        s.append(set([v]))
    # weight is a array of size * size, it's just a reminder.
    weight = [[0 for x in range(size)] for y in range(size)] 
    # use graph_dict to store weights of every edge weight(u, v)
    graph_dict = {}
    for i in range(1, size):
        for j in range(size):
            if j == i:
                break
            weight[i][j] = math.sqrt((graph[i].pos[0] - graph[j].pos[0])**2
                            +  (graph[i].pos[1] - graph[j].pos[1])**2)
            tmp = math.sqrt((graph[i].pos[0] - graph[j].pos[0])**2
                            +  (graph[i].pos[1] - graph[j].pos[1])**2)
            graph_dict.update({Edge(graph[i], graph[j]): tmp})
    #sorting dict by weights in non-decreasing order, and store it to a list.
    graph_list = sorted(graph_dict.items(), key=operator.itemgetter(1)) 
    #print(graph_list)

    # mininum spanning tree
    mst = []
    edges_counter = 0
    # foreach (u, v) in G.E ordered by weight(u, v), increasing:
    for index, u_v in enumerate(graph_list):
        # FIND-SET(u)
        for index, set_u in enumerate(s):
            if u_v[0].p1 in set_u:
                id1 = index
                break
        # FIND-SET(u)
        for index, set_u in enumerate(s):
            if u_v[0].p2 in set_u:
                id2 = index
                break
        # if FIND-SET(u) ≠ FIND-SET(v):
        if id1 != id2:
            # UNION(u, v) to a set which u is already in, and delete original v's set.
            s[id1] = s[id1].union(s[id2])
            s.pop(id2)

            # store the new edge to result.
            result = result + u_v[1]

            mst.append((u_v[0].p1, u_v[0].p2))

            edges_counter += 1
            # x vertices need x-1 edges to connect them.
            # k clusters need k-1 edges to connect them.
            # vertix of size, k clusters, need size-k edges to divide into k clusters.
            # size-k+1's edge is the min distance between any two points from different
            # clusters.
            if edges_counter == size-k+1:
                return u_v[1]
    return result
'''
KRUSKAL(G):
    A = ∅
    foreach v ∈ G.V:
        MAKE-SET(v)
    foreach (u, v) in G.E ordered by weight(u, v), increasing:
        if FIND-SET(u) ≠ FIND-SET(v):
            A = A ∪ {(u, v)}
            UNION(u, v)
    return A
'''
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [12, 7, 6, 4, 3, 5, 1, 1, 7, 2, 7, 5, 7, 3, 3, 7, 8, 2, 8, 4, 4, 6, 7, 2, 6, 3]
    #data = [8, 3, 1, 1, 2, 4, 6, 9, 8, 9, 9, 8, 9, 3, 11, 4, 12, 4]
    #print(data)
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
