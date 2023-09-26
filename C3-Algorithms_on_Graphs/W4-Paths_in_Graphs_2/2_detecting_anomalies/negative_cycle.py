#Uses python3

import sys
from random import randint

""" This block of pseudo code of Bellman-Ford algorithm is from wikipedia.

function BellmanFord(list vertices, list edges, vertex source) is

    // This implementation takes in a graph, represented as
    // lists of vertices (represented as integers [0..n-1]) and edges,
    // and fills two arrays (distance and predecessor) holding
    // the shortest path from the source to each vertex

    distance := list of size n
    predecessor := list of size n

    // Step 1: initialize graph
    for each vertex v in vertices do
        // Initialize the distance to all vertices to infinity
        distance[v] := inf
        // And having a null predecessor
        predecessor[v] := null
    
    // The distance from the source to itself is, of course, zero
    distance[source] := 0

    // Step 2: relax edges repeatedly
    repeat |V|-1 times:
        for each edge (u, v) with weight w in edges do
            if distance[u] + w < distance[v] then
                distance[v] := distance[u] + w
                predecessor[v] := u

    // Step 3: check for negative-weight cycles
    for each edge (u, v) with weight w in edges do
        if distance[u] + w < distance[v] then
            predecessor[v] := u
            // A negative cycle exist; find a vertex on the cycle 
            visited := list of size n initialized with false
            visited[v] := true
            while not visited[u] do
                visited[u] := true
                u := predecessor[u]
            // u is a vertex in a negative cycle, find the cycle itself
            ncycle := [u]
            v := predecessor[u]
            while v != u do
                ncycle := concatenate([v], ncycle)
                v := predecessor[v]
            error "Graph contains a negative-weight cycle", ncycle
    return distance, predecessor
"""

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

    """
    def __init__(self, key, adjacent_keys, weights, distance=1e9, previous_vertex=None):

        self.key = key # key of the vertex.
        self.adjacent_keys = adjacent_keys # keys of adjacent vertices.
        self.weights = weights # weights of edges to adjacent vertices.
        self.distance = distance
        self.previous_vertex = previous_vertex

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

def negative_cycle(adj, cost):
    # print(f"adj: {adj}, cost: {cost}")

    num_nodes = len(adj)
    assert num_nodes == len(cost)

    # Initialize the `graph`.
    graph = []
    for i in range(num_nodes):
        graph.append(Vertex(i, adj[i], cost[i]))

    # `start_key` is not necessarily 0.
    start_key = randint(0, num_nodes-1) # Return a random integer N such that a <= N <= b

    # Pass `graph` by reference. `graph` will be updated in-place.
    bellman_ford(graph, start_key)

    # print_graph(graph)

    for i in range(num_nodes):
        u = graph[i]
        for v_idx, v in enumerate(u.adjacent_keys):
            alt = u.distance + u.weights[v_idx]

            if alt < graph[v].distance:
                # negative-weight cycles can reduce the distance to minus infinity.
                return 1
    return 0

def print_graph(graph):
    print("graph")
    for node in graph:
        print("key: ", node.key, "dist:", node.distance)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    # data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1] # ans = 1
    # data = [4, 3, 1, 2, -1, 2, 3, -2, 3, 4, -3] # and = 0

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
