#!/usr/bin/env python3

import sys
import math
import numpy as np
import copy
from random import randint
#sys.setrecursionlimit(100000) 	# when using copy.deepcopy, this function
								# has to be called manually.

class Vertex():
	def __init__(self):
		self.value = None	# value of the vertex.
		self.adj = [] 		# adjacent of the vertex.
		self.group = None 	# 
		self.prev = None 	# previous vertex
		self.dist = 1e9 	# default distance equals to infinitiv, 
							# it should be bigger than 1e8.
		self.weight = None 	# weight of edges.

def distance(adj, cost, s, t):
	size = len(adj)
	graph = []
	for i in range(size):
		graph.append(Vertex())
	graph[s].dist = 0 # set distance of start point as 0.
	for i in range(size):
		graph[i].value = i
	for i in range(size):
		graph[i].weight = cost[i]
	for i in range(size):
		for j in adj[i]:
			graph[i].adj.append(graph[j])

	dist_que = []
	for i in range(size):
		dist_que.append(graph[i].dist)

	#tmp_g = copy.deepcopy(h) 	I prefer not to use this function since it has 
	# 							a issue about recursion limit.
	tmp_g = []
	for i in range(size):
		tmp_g.append(graph[i])

	while len(graph) != 0:
		index_u = np.argmin(dist_que)
		#index_u = min(range(len(dist_que)), key=dist_que.__getitem__)
		u = graph[index_u]
		#print("u_val =", u.value)
		graph.pop(index_u)
		dist_que.pop(index_u)

		for v_idx, v in enumerate(u.adj):
			#print("v_val =", v.value)
			alt = u.dist + u.weight[v_idx]
			#print("alt =", alt, "dist =", v.dist)

			if alt < v.dist:
				v.dist = alt
				v.prev = u
				tmp_g[v.value] = v
				#print("v_new_dist = ", tmp_g[v.value].dist)
				
				# when updating vertex, dist list should be updated too. 
				# It's a list of integer, not list of objects(mutable). 
				dist_que = []
				for i in range(len(graph)):
					dist_que.append(graph[i].dist)
			
	if tmp_g[t].dist < 1e9:
		return tmp_g[t].dist
	else:
		return -1	

''' This block of pseudo code is from Dijkstra wiki. 
function Dijkstra(Graph, source):

     create vertex set Q

     for each vertex v in Graph:         // Initialization
         dist[v] ← INFINITY              // Unknown distance from source to v
         prev[v] ← UNDEFINED             // Previous node in optimal path from source
         add v to Q                      // All nodes initially in Q (unvisited nodes)

     dist[source] ← 0                    // Distance from source to source
     
     while Q is not empty:
         u ← vertex in Q with min dist[u]// Source node will be selected first
         remove u from Q 
         
         for each neighbor v of u:       // where v is still in Q.
             alt ← dist[u] + length(u, v)
             if alt < dist[v]:           // A shorter path to v has been found
                 dist[v] ← alt 
                 prev[v] ← u 

     return dist[], prev[]
'''
if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	#data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 5] # ans = 6
	#data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3] # ans = 3
	#data = [10, 9, 1, 2, 1, 6, 7, 1, 8, 9, 1, 9, 10, 1, 3, 4, 1, 7, 8, 1, 4, 5, 1, 5, 6, 1, 2, 3, 1, 1, 10] # ans = 9
	#data = [5, 9, 1, 2, 1, 1, 3, 1, 1, 5, 1, 2, 3, 2, 2, 4, 5, 3, 5, 1, 3, 4, 3, 5, 4, 4, 5, 2, 1, 1, 4] # ans = 4
	#data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2] # ans = -1
	#data = [4, 6, 2, 1, 1, 1, 4, 1, 2, 4, 1, 4, 3, 1, 3, 1, 1, 1, 3, 1, 1, 2] # ans = -1
	#data = [3, 0, 1, 2] # ans = -1
	#data = [3, 0, 1, 3] # ans = -1
	#data = [1, 0, 1, 1] # ans = 0
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
	#print(adj, cost)
	print(distance(adj, cost, s, t))
	
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