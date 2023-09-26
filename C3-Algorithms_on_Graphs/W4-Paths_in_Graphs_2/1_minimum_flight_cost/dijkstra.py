#Uses python3

import sys
import heapq
import copy

# This block of pseudo code of Dijkstra's algorithm is from wikipedia.
# 
#  1  function Dijkstra(Graph, source):
#  2      
#  3      for each vertex v in Graph.Vertices:
#  4          dist[v] ← INFINITY
#  5          prev[v] ← UNDEFINED
#  6          add v to Q
#  7      dist[source] ← 0
#  8      
#  9      while Q is not empty:
# 10          u ← vertex in Q with min dist[u]
# 11          remove u from Q
# 12          
# 13          for each neighbor v of u still in Q:
# 14              alt ← dist[u] + Graph.Edges(u, v)
# 15              if alt < dist[v]:
# 16                  dist[v] ← alt
# 17                  prev[v] ← u
# 18
# 19      return dist[], prev[]

class Vertex():

    def __init__(self, key, adjacent_keys, weights, distance=float("inf"), previous_vertex=None):

        self.key = key # key of the vertex.
        self.adjacent_keys = adjacent_keys # keys of adjacent vertices.
        self.weights = weights # weights of edges to adjacent vertices.
        self.distance = distance
        self.previous_vertex = previous_vertex

    # Define a custom comparison method based on 'distance'. The binary heap will
    # use this rule to determine which element will be pop out.
    def __lt__(self, other):
        return self.distance < other.distance


def update_vertex_distance(graph, key, distance):
    # Update the vertex's distance to new distance.
    for node in graph:
        if node.key == key:
            node.distance = distance
            break


def print_heap(graph):
    print("graph")
    for node in graph:
        print("key: ", node.key, "dist:", node.distance)


def dijkstra_slow(original_graph, start_key):
    num_nodes = len(original_graph)

    # Initialize the distance of the starting node to 0.
    original_graph[start_key].distance = 0

    # Create a temporary graph as a binary heap which will be used to extract
    # the node with minimum distance.
    tmp_graph = copy.deepcopy(original_graph)
    assert num_nodes == len(tmp_graph)

    while len(tmp_graph) != 0:
        # Convert a normal list `tmp_graph` to a list with binary heap properties.
        # NOTE: `tmp_graph` is still a list. heapq.heapify() needs to be called
        # before pop every time.
        heapq.heapify(tmp_graph)

        # Pop the Vertex with minimum distance
        node = heapq.heappop(tmp_graph)

        for adj_idx, adj_key in enumerate(node.adjacent_keys):
            
            new_distance = node.distance + node.weights[adj_idx]

            if new_distance < original_graph[adj_key].distance:
                original_graph[adj_key].distance = new_distance
                original_graph[adj_key].previous_vertex = node.key

                # This function is super slow.
                update_vertex_distance(tmp_graph, adj_key, new_distance)

def find_key_of_min_value(dictionary):

    # Use min() with a generator expression to find the minimum value
    min_value = min(dictionary.values())
    # Use a list comprehension to get the keys with the minimum value
    for key, value in dictionary.items():
        if value == min_value:
            return key
    assert False

def dijkstra(original_graph, start_key):
    num_nodes = len(original_graph)

    previous = [None for _ in range(num_nodes)]

    # `distance` stores the distance of each node.
    distance = {}
    for i in range(num_nodes):
        distance[i] = float("inf")

    # `tmp_distance` stores the distance of each node, and 
    # nodes in `tmp_distance` will be pop out one by one.
    tmp_distance = {}
    for i in range(num_nodes):
        tmp_distance[i] = float("inf")

    distance[start_key] = 0
    tmp_distance[start_key] = 0

    while len(tmp_distance) != 0:
        keys_with_min_value = find_key_of_min_value(tmp_distance)

        # Pop the (key, value) out of `tmp_distance`.
        tmp_distance.pop(keys_with_min_value)

        # Get the node going to be processed.
        node = original_graph[keys_with_min_value]

        # Iterate the neighbors of `node`.
        for adj_idx, adj_key in enumerate(node.adjacent_keys):

            # It's possible that `tmp_distance` doesn't have `adj_key` because
            # `adj_key` is already pop out of `tmp_distance`, which means that
            # the distance of the node with `adj_key` is final. It doesn't need
            # to be updated anymore.
            if adj_key not in tmp_distance:
                # NOTE: Do not use break because it just wants to skip this `adj_key`.
                continue
            
            new_distance = distance[keys_with_min_value] + node.weights[adj_idx]

            if new_distance < distance[adj_key]:
                # Update the distance.
                tmp_distance[adj_key] = new_distance
                distance[adj_key] = new_distance

                # Store the previous key.
                previous[adj_key] = keys_with_min_value

    return distance, previous

def distance(adj, cost, start, terminal):
    # print(f"adj: {adj}, cost: {cost}, start: {start}, terminal: {terminal}")

    num_nodes = len(adj)
    assert num_nodes == len(cost)

    # Initialize the `graph`.
    graph = []
    for i in range(num_nodes):
        graph.append(Vertex(i, adj[i], cost[i]))

    distance, previous_key = dijkstra(graph, start)

    if distance[terminal] == float("inf"):
        return -1
    else:
        return distance[terminal]

def stress_test():
	''' This block of code is for stress-testing of distance(). 
	Generating testing input is very important, in this case, I found out some
	loop-hole about copy.deepcopy that makes my program fail. I couldn't find 
	out this loop-hole without large number of testing input. 
	copy.deepcopy has some issues when sys.setrecursionlimit is under 1000.
	I have to raise the limit manually (sys.setrecursionlimit(100000)).
	
	data = []
	n = randint(1, 1000) # 1 <= n <= 1000
	data.append(n)
	m = randint(0, 100000) # 0 <= m <=100000
	data.append(m)
	for i in range(m):
		edge_start = randint(1, n)
		data.append(edge_start)
		edge_end = randint(1, n)
		data.append(edge_end)
		weight = randint(0, 1000) # 0 <= weight <= 1000
		data.append(weight)
	u, v = randint(1, n), randint(1, n) # u != v, 1 <= u, v <= n
	data.append(u)
	data.append(v)
	print(data)

	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
	data = data[3 * m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((a, b), w) in edges:
		adj[a - 1].append(b - 1)
		cost[a - 1].append(w)
	s, t = data[0] - 1, data[1] - 1
	#print(data)
	print(distance(adj, cost, s, t))
	'''

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # Uncomment the following for testing.
    # data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 5] # ans = 6
    # data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3] # ans = 3
    # data = [10, 9, 1, 2, 1, 6, 7, 1, 8, 9, 1, 9, 10, 1, 3, 4, 1, 7, 8, 1, 4, 5, 1, 5, 6, 1, 2, 3, 1, 1, 10] # ans = 9
    # data = [5, 9, 1, 2, 1, 1, 3, 1, 1, 5, 1, 2, 3, 2, 2, 4, 5, 3, 5, 1, 3, 4, 3, 5, 4, 4, 5, 2, 1, 1, 4] # ans = 4
    # data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2] # ans = -1
    # data = [4, 6, 2, 1, 1, 1, 4, 1, 2, 4, 1, 4, 3, 1, 3, 1, 1, 1, 3, 1, 1, 2] # ans = -1
    # data = [3, 0, 1, 2] # ans = -1
    # data = [3, 0, 1, 3] # ans = -1
    # data = [1, 0, 1, 1] # ans = 0

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
