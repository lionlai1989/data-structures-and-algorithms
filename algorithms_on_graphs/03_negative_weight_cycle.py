#!/usr/bin/env python3

import sys

class Vertex():
	def __init__(self):
		self.value = None	# value of the vertex.
		self.adj = [] 		# adjacent of the vertex.
		self.group = None 	# 
		self.prev = None 	# previous vertex
		self.dist = 1e9 	# default distance equals to infinitiv, 
							# it should be bigger than 1e8.
		self.weight = None 	# weight of edges.
		
def negative_cycle(adj, cost):
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
	graph[0].dist = 0 # set distance of start point as 0.

	for j in range(size-1): # We do V-1 times since vertex would be possibly updated after every iteration.
                            # If no distance being update during iteration, the iteration can be stopped.
		for i in range(size):
			u = graph[i]
			for v_idx, v in enumerate(u.adj):
				#print("u =", u.value, "v =", v.value)
				alt = u.dist + u.weight[v_idx]
				if alt < v.dist:
					v.dist = alt
					v.prev = u

	for i in range(size):
		u = graph[i]
		for v_idx, v in enumerate(u.adj):
			alt = u.dist + u.weight[v_idx]
			if alt < v.dist:
				return 1
	return 0
''' This block of code is from Bellman–Ford algorithm wiki.
function BellmanFord(list vertices, list edges, vertex source)
	::distance[],predecessor[]

	// This implementation takes in a graph, represented as
	// lists of vertices and edges, and fills two arrays
	// (distance and predecessor) with shortest-path
	// (less cost/distance/metric) information

	// Step 1: initialize graph
	for each vertex v in vertices:
		distance[v] := inf             // At the beginning , all vertices have a weight of infinity
		predecessor[v] := null         // And a null predecessor
	
	distance[source] := 0              // Except for the Source, where the Weight is zero 
	
	// Step 2: relax edges repeatedly
	for i from 1 to size(vertices)-1:
		for each edge (u, v) with weight w in edges:
			if distance[u] + w < distance[v]:
				distance[v] := distance[u] + w
				predecessor[v] := u

	// Step 3: check for negative-weight cycles
	for each edge (u, v) with weight w in edges:
		if distance[u] + w < distance[v]:
			error "Graph contains a negative-weight cycle"
	return distance[], predecessor[]
'''
if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	#data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1] # ans = 1
	#data = [4, 3, 1, 2, -1, 2, 3, -2, 3, 4, -3] # and = 0
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
	data = data[3 * m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((a, b), w) in edges:
		adj[a - 1].append(b - 1)
		cost[a - 1].append(w)
	#print(adj, cost)
	print(negative_cycle(adj, cost))
