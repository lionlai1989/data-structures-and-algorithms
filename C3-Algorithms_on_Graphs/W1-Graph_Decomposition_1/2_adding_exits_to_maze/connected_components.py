# Uses python3

import sys


class Graph:
    def __init__(self) -> None:
        self.clock = 0  # Count the time of entering and leaving a vertex.


class Vertex:
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


def depth_first_search(vertices, idx_vertex, graph, group):
    previsit(vertices[idx_vertex], graph)
    vertices[idx_vertex].group = group

    for adj_key in vertices[idx_vertex].adjacent_key:
        if vertices[adj_key].previsit == 0:
            depth_first_search(vertices, adj_key, graph, group)

    postvisit(vertices[idx_vertex], graph)


def number_of_components(adj):
    # Now `adj` is 0-based indexing.
    # print("adj:", adj)
    # print("x:", x)
    # print("y:", y)

    graph = Graph()
    previsit = 0
    postvisit = 0
    group = 0
    vertices = []
    for idx, adjacent_key in enumerate(adj):
        # `adjacent_key` has adjacent keys to `idx`.
        vertices.append(Vertex(idx, adjacent_key, previsit, postvisit, group))

    for idx, vertex in enumerate(vertices):
        if vertex.previsit == 0:
            # `vertex` has not been visited.
            group += 1
            depth_first_search(vertices, idx, graph, group)

    return group


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
