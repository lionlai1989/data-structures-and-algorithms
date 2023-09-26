#Uses python3

import sys
from collections import deque

class Node():
    """Node represents a node in the graph. It contains its `key` value and
    `adjacent_key` to whom it connects. E.g., if `key` is 2 and `adjacent_key` is [0, 1],
    it means there are edges (2, 0) and (2, 1).
    `distance`: store the number of edges between the starting node and itself.
    """
    def __init__(self, key, adjacent_key, distance=-1):
        self.key = key
        self.adjacent_key = adjacent_key
        self.distance = distance


def explore(graph, node_key, queue):

    # Loop all adjacent keys of `node_key`.
    for adj_key in graph[node_key].adjacent_key:

        if graph[adj_key].distance == -1:
        
            graph[adj_key].distance = graph[node_key].distance + 1

            queue.append(adj_key)

        if graph[adj_key].distance != -1 and (graph[node_key].distance == graph[adj_key].distance):
            # graph[node_key] and graph[adj_key] are on the same level of Shortest-path tree, and
            # they are connected.
            # Thus, the graph is not a bipartite.
            return 0
    
    # The graph is a bipartite.
    return 1

def breadth_first_search(graph, start_key):
    queue = deque()

    queue.append(start_key)

    while len(queue) != 0:
        node_key = queue.popleft()

        if explore(graph, node_key, queue) == 0:
            # The graph is not a bipartite.
            return 0

    # The graph is a bipartite.   
    return 1

def bipartite(adj):
    # print(f"adj: {adj}")

    graph = []

    for idx , adjacent_key in enumerate(adj):
        # Key is also the index in the graph.
        graph.append(Node(idx, adjacent_key))

    # Iterate every node in graph.
    for idx, node in enumerate(graph):

        # Run BFS on node if it has not been reached.
        if node.distance == -1:
            # `node` is the first node in this run. Thus, initialize the distance to 0.
            node.distance = 0

            if breadth_first_search(graph, idx) == 0:
                # The graph is not a bipartite.
                return 0

    # The graph is a bipartite.
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
