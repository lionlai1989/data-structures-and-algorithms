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


def breadth_first_search(graph, start_key):
    queue = deque()

    queue.append(start_key)

    while len(queue) != 0:
        node_key = queue.popleft()

        explore(graph, node_key, queue)

def distance(adj, start, terminal):
    # print(f"adj: {adj}")
    # print(f"start: {start}. terminal: {terminal}")

    graph = []

    for idx , adjacent_key in enumerate(adj):
        # Key is also the index in the graph.
        graph.append(Node(idx, adjacent_key))

    # Initialize the starting node's distance.
    graph[start].distance = 0

    breadth_first_search(graph, start)

    return graph[terminal].distance

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
