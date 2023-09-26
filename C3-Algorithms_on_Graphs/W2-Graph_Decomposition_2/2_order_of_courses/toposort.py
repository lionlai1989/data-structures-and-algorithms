#Uses python3

import sys

class Graph():
    def __init__(self) -> None:
        self.clock = 0 # Count the time of entering and leaving a vertex.
        self.cycle_detected = False # True if a cycle exists in Graph.

class Vertex():
    """Vertex represents a vertex in the graph. It contains its `key` value and
    `adjacent_key` to whom it connects. E.g., if `key` is 2 and `adjacent_key` is [0, 1],
    it means there are edges (2, 0) and (2, 1).
    """
    def __init__(self, key, adjacent_key, previsit=0, postvisit=0, group=None):
        self.key = key
        self.adjacent_key = adjacent_key
        self.previsit = previsit
        self.postvisit = postvisit
        self.group = group

def previsit(v, graph):
    graph.clock += 1
    v.previsit = graph.clock

def postvisit(v, graph):
    graph.clock += 1
    v.postvisit = graph.clock

def depth_first_search(vertices, idx_vertex, graph, group, topological_order):
    previsit(vertices[idx_vertex], graph)
    vertices[idx_vertex].group = group

    for adj_key in vertices[idx_vertex].adjacent_key:
        if vertices[adj_key].previsit == 0:
            depth_first_search(vertices, adj_key, graph, group, topological_order)

        elif vertices[adj_key].previsit != 0 and vertices[adj_key].postvisit == 0:
            graph.cycle_detected = True

    postvisit(vertices[idx_vertex], graph)
    topological_order.append(vertices[idx_vertex].key)

def toposort(adj):
    # Now `adj` is 0-based indexing.
    # print("adj:", adj)
    
    graph = Graph()
    previsit = 0
    postvisit = 0
    group = 0
    vertices = []

    for idx , adjacent_key in enumerate(adj):
        # `adjacent_key` has adjacent keys to `idx`.
        vertices.append(Vertex(idx, adjacent_key, previsit, postvisit, group))

    # `topological_order` is a reference to a list. Thus, it's OK to send a
    # reference into recursive function calls such that `topological_order`
    # will be updated correctly.
    topological_order = []

    for idx, vertex in enumerate(vertices):
        if vertex.previsit == 0:
            # `vertex` has not been visited.
            group += 1
            depth_first_search(vertices, idx, graph, group, topological_order)

    topological_order.reverse()

    return topological_order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

