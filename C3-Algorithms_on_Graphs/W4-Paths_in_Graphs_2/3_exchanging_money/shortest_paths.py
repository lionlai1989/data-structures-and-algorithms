#!/usr/bin/env python3

import sys
from collections import deque

class Vertex():
    """ BUG: One BIG issue of using `float("inf")` as the default value of `distance` is the following:
    
    >>> ditance = float("inf")
    >>> assert ditance + 10 < ditance + 100
    >>> Traceback (most recent call last):
    >>> File "<stdin>", line 1, in <module>
    >>> AssertionError

    But if `ditance` is set to a very big number instead of `inf`.
    >>> ditance = 1e9
    >>> assert ditance + 10 < ditance + 100
    Then everything works as expected.

    Ok, it seems I need to use `float("inf")` to represent infinity here because the distance
    in this task is already very large value.
    """
    def __init__(self, key, adjacent_keys, weights, distance=float("inf"), previous_vertex=None, layer=None):

        self.key = key # key of the vertex.
        self.adjacent_keys = adjacent_keys # keys of adjacent vertices.
        self.weights = weights # weights of edges to adjacent vertices.
        self.distance = distance
        self.previous_vertex = previous_vertex
        self.layer = layer

    # Define a custom comparison method based on 'distance'. The binary heap will
    # use this rule to determine which element will be pop out.
    def __lt__(self, other):
        return self.distance < other.distance

def bellman_ford(original_graph, start_key):
    num_vertices = len(original_graph)

    # previous = [None for _ in range(num_vertices)]

    original_graph[start_key].distance = 0 # set distance of start point as 0.

    # We do V-1 times since vertex would be possibly updated after every iteration.
    # If no distance being update during iteration, the iteration can be stopped.
    for j in range(num_vertices - 1): 
        for i in range(num_vertices):

            u = original_graph[i]
            for v_idx, v_key in enumerate(u.adjacent_keys):
                new_distance = u.distance + u.weights[v_idx]

                if new_distance < original_graph[v_key].distance:
                    original_graph[v_key].distance = new_distance
                    original_graph[v_key].previous_vertex = u.key


def explore(graph, node_key, queue):
    # Loop all adjacent keys of `node_key`.
    for adj_key in graph[node_key].adjacent_keys:

        if graph[adj_key].layer == None:
        
            graph[adj_key].layer = graph[node_key].layer + 1

            queue.append(adj_key)

def breadth_first_search(graph, start_key, inf_v):
    queue = deque()

    queue.append(start_key)
    inf_v.append(start_key) # Appending the starting point.

    while len(queue) != 0:
        node_key = queue.popleft()
        inf_v.append(node_key)

        explore(graph, node_key, queue)


def shortet_paths(adj, cost, start_key, distance, reachable, shortest):

    # print(f"adj: {adj}, cost: {cost}, s: {s}, distance:, {distance}, reachable: {reachable}, shortest: {shortest}")

    num_nodes = len(adj)
    assert num_nodes == len(cost)

    # Initialize the `graph`.
    graph = []
    for i in range(num_nodes):
        graph.append(Vertex(i, adj[i], cost[i]))

    distance[start_key] = 0

    ''' Run Bellman-Ford's algorithm to find shortest paths from node S for 
    exactly |V|-1 iterations, where |V| is the number of nodes in the graph.
    '''
    bellman_ford(graph, start_key=start_key)

    # Write distance to `distance` variable.
    for i in range(num_nodes):
        distance[i] = graph[i].distance


    ''' Save all the nodes for which the distance estimate was decreased on the
    V-th iteration - denote the set of these nodes by A. Nodes in A represent
    the node that has infinite distance to the start node.
    '''
    A = [] 
    for i in range(num_nodes):

        u = graph[i]

        for v_idx, v in enumerate(u.adjacent_keys):

            alt = u.distance + u.weights[v_idx]
            if alt < graph[v].distance:
                graph[v].distance = alt
                graph[v].previous_vertex = u.key

                A.append(u)

    ''' Find all nodes reachable from any node in A, use breadth-first search 
    to do that (put all the nodes from A in the queue initially, then run the 
    regular breadth-first search with that queue). Denote the set of these 
    nodes by B. There exist arbitrarily short paths from S to u if and only if
    u is in the set B. Nodes in B are reachable by the nodes in A. In other words,
    nodes in B has infinite distance from the starting point.
    '''
    B = []
    for node in A:
        if node.layer == None:
            node.layer = 0

            # start from the vertex `node`
            breadth_first_search(graph, node.key, B)

    for i in B:
        shortest[i] = 0

    for i in range(num_nodes):
        if graph[i].distance == float('inf'):
            reachable[i] = 0
        else:  
            reachable[i] = 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    # data = [6, 7, 1, 2, 10, 2, 3, 5, 1, 3, 100, 3, 5, 7, 5, 4, 10, 4, 3, -18, 6, 1, -1, 1] # ans = 0 10 - - - *
    # data = [5, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 3, 1, -5, 4] # ans = - - - 0 *
    # data = [6, 6, 4, 3, 2, 3, 1, -4, 1, 2, 1, 2, 3, 2, 2, 5, 10, 5, 6, 3, 4] # ans = - - - 0 - -
    # data = [6, 6, 1, 2, -4, 2, 3, 1, 3, 1, 2, 6, 3, 100, 4, 6, 1, 2, 4, 1, 1] # ans = - - - - * -
    # data = [7, 7, 1, 2, -4, 2, 3, 1, 3, 1, 2, 6, 3, 100, 4, 6, 1, 2, 4, 1, 7, 1, 3, 1] # ans = - - - - * - *
    # data = [7, 8, 4, 7, 2, 1, 2, -4, 2, 3, 1, 3, 1, 2, 6, 3, 100, 4, 6, 1, 2, 4, 1, 7, 1, 3, 7] # ans = - - - - * - -
    # data = [5, 7, 1, 2, 10, 2, 3, 5, 1, 3, 100, 3, 5, 7, 5, 4, 10, 4, 3, -18, 5, 1, -1, 1] # ans = - - - - - 
    # data = [3, 2, 2, 3, -1, 3, 2, -1, 1] # ans = 0 * *

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
    distance = [10**19] * n
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

