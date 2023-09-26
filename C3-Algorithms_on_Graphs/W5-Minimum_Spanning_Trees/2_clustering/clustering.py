#!/usr/bin/env python3

import sys
import math


class Vertex():
    def __init__(self, key, x, y):
        self.key = key      # value of the vertex.
        self.x_coord = x # x coordinate
        self.y_coord = y # y coordinate

class Edge():
    def __init__(self, vertex_1, vertex_2, distance):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.distance = distance
          
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def Kruskal_min_spanning_tree(graph):
    """ Given a set of 2D points scattering over a 2D plane, it first constructs the
    minimum spanning tree connecting all 2D points and calculates the distance of the
    tree.

    Wiki: the following code is implemented with a disjoint-set data structure.

    algorithm Kruskal(G) is
    F:= ∅
    for each v ∈ G.V do
        MAKE-SET(v)
    for each (u, v) in G.E ordered by weight(u, v), increasing do
        if FIND-SET(u) ≠ FIND-SET(v) then
            F:= F ∪ {(u, v)} ∪ {(v, u)}
            UNION(FIND-SET(u), FIND-SET(v))
    return F
    """

    # Create a list of sets. Each set contains a vertex.
    vertices_sets = []
    for v in graph:
        vertices_sets.append(set([v]))

    # Every vertex can possibly connect to every other vertices. Thus, I
    # need to calculate distances for all edges and sort them in non-decreasing
    # order.
    def calculate_edges(graph):
        # Using numpy is cheating. Thus, use 2D list.
        # already_processed = [[False for _ in range(size)] for _ in range(size)] 

        edges = []
        size = len(graph)

        """ The two for loops calculate distances between two vertices:
            size == 4 (0, 1, 2, 3)

              0 1 2 3 (i)
            0   v v v
            1     v v
            2       v
           (j)
        
            There is no self-loops (edges going from a vertex to itself) and parallel edges.
        """
        for i in range(1, size):
            for j in range(size - 1):
                if j == i:
                    break
                edges.append(Edge(graph[i], graph[j], euclidean_distance(graph[i].x_coord, graph[i].y_coord, graph[j].x_coord, graph[j].y_coord)))

        return edges
            
    sorted_edges = sorted(calculate_edges(graph), key=lambda tmp: tmp.distance)
    # for edge in sorted_edges:
    #     print(f"{edge.distance} ", end="")

    min_distance = 0
    mininum_spanning_tree = []

    # Iterate edges with distances from small to big.
    for edge in sorted_edges:
        # Check if an edge's two terminal u and v are in the same set.
        # FIND-SET(u)
        for idx, s in enumerate(vertices_sets):
            if edge.vertex_1 in s:
                 u_idx = idx
                 break
        # FIND-SET(u)
        for idx, s in enumerate(vertices_sets):
            if edge.vertex_2 in s:
                 v_idx = idx
                 break

        # if FIND-SET(u) ≠ FIND-SET(v) then
        if u_idx != v_idx:

            # UNION(u, v) to a set which u is already in, and delete original v's set.
            vertices_sets[u_idx] = vertices_sets[u_idx].union(vertices_sets[v_idx])
            vertices_sets.pop(v_idx)

			# store the new edge to result.
            min_distance += edge.distance
            mininum_spanning_tree.append(edge)

    return mininum_spanning_tree, min_distance

def Prim_min_spanning_tree():
    """ Given a set of 2D points scattering over a 2D plane, it first constructs the
    minimum spanning tree connecting all 2D points and calculates the distance of the
    tree.
    """
    pass

def clustering(x, y, k):
    num_points = len(x)
    assert num_points == len(y)

    graph = []

    for i in range(num_points):
        graph.append(Vertex(i, x[i], y[i]))

    mininum_spanning_tree, _ = Kruskal_min_spanning_tree(graph)

    edges_counter = 0
    for edge in mininum_spanning_tree:
        edges_counter += 1
        # x vertices need x-1 edges to connect them.
        # k clusters need k-1 edges to connect them.
        # vertix of size, k clusters, need size-k edges to divide into k clusters.
        # size-k+1's edge is the min distance between any two points from different
        # clusters.
        if edges_counter == num_points-k+1:
            return edge.distance

    assert False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    # data = [12, 7, 6, 4, 3, 5, 1, 1, 7, 2, 7, 5, 7, 3, 3, 7, 8, 2, 8, 4, 4, 6, 7, 2, 6, 3] # ans = 2.828427124746
    # data = [8, 3, 1, 1, 2, 4, 6, 9, 8, 9, 9, 8, 9, 3, 11, 4, 12, 4] # ans = 5.000000000

    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
