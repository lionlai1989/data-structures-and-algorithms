#!/usr/bin/env python3

import sys
import queue

class Vertex():
	def __init__(self):
		self.value = None   # value of the vertex.
		self.adj = []       # adjacent of the vertex.
		self.group = None   # 
		self.prev = None    # previous vertex
		# default distance equals to infinitiv, 
		# it should be bigger than 1e8.
		# Don't use 1e19, there would be some problems of stack overflow.
		self.dist = float('inf')   

		self.weight = None  # weight of edges.
		self.layer = None

def search(node, v, queue):
	for w in v.adj:
		if w.layer == None:
			w.layer = v.layer + 1
			queue.append(w)
			
def bfs(node, v, inf_v):
	queue = []
	v.group = bfs.group
	#shortest_path_tree T = empty
	search(node, v, queue)
	inf_v.append(v.value) # Appending the start point(not in queue).
	while len(queue) != 0:
		w = queue.pop(0)
		inf_v.append(w.value)
		search(node, w, queue)

def shortet_paths(adj, cost, s, distance, reachable, shortest):
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
	graph[s].dist = 0 # set distance of start point as 0.
	distance[s] = 0
	
	''' Run Bellman-Ford's algorithm to find shortest paths from node S for 
	exactly |V|-1 iterations, where |V| is the number of nodes in the graph.
	'''
	for j in range(size-1): 
		for i in range(size):
			u = graph[i]
			for v_idx, v in enumerate(u.adj):
				#print("u =", u.value, "v =", v.value)
				alt = u.dist + u.weight[v_idx]
				if alt < v.dist:
					v.dist = alt
					v.prev = u
					distance[v.value] = alt

	''' Save all the nodes for which the distance estimate was decreased on the
	V-th iteration - denote the set of these nodes by A.
	'''
	a = [] 
	for i in range(size):
		u = graph[i]
		for v_idx, v in enumerate(u.adj):
			#print("u =", u.value, "v =", v.value)
			alt = u.dist + u.weight[v_idx]
			if alt < v.dist:
				v.dist = alt
				v.prev = u
				a.append(u)

	''' Find all nodes reachable from any node in A, use breadth-first search 
	to do that (put all the nodes from A in the queue initially, then run the 
	regular breadth-first search with that queue). Denote the set of these 
	nodes by B. There exist arbitrarily short paths from S to u if and only if
	u is in the set B.
	'''
	inf_v = []
	bfs.group = 0
	for n in a:
		if n.layer == None:
			bfs.group += 1
			n.layer = 0
			# start from vertex node[u]
			# inf_v is an mutable list.
			bfs(a, n, inf_v) 

	for i in inf_v:
		shortest[i] = 0

	for i in range(size):
		if graph[i].dist == float('inf'):
			reachable[i] = 0
		else:  
			reachable[i] = 1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	#data = [6, 7, 1, 2, 10, 2, 3, 5, 1, 3, 100, 3, 5, 7, 5, 4, 10, 4, 3, -18, 6, 1, -1, 1] # ans = 0 10 - - - *
	#data = [5, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 3, 1, -5, 4] # ans = - - - 0 *
	#data = [6, 6, 4, 3, 2, 3, 1, -4, 1, 2, 1, 2, 3, 2, 2, 5, 10, 5, 6, 3, 4] # ans = - - - 0 - -
	#data = [6, 6, 1, 2, -4, 2, 3, 1, 3, 1, 2, 6, 3, 100, 4, 6, 1, 2, 4, 1, 1] # ans = - - - - * -
	#data = [7, 7, 1, 2, -4, 2, 3, 1, 3, 1, 2, 6, 3, 100, 4, 6, 1, 2, 4, 1, 7, 1, 3, 1] # ans = - - - - * - *
	#data = [7, 8, 4, 7, 2, 1, 2, -4, 2, 3, 1, 3, 1, 2, 6, 3, 100, 4, 6, 1, 2, 4, 1, 7, 1, 3, 7] # ans = - - - - * - -
	#data = [5, 7, 1, 2, 10, 2, 3, 5, 1, 3, 100, 3, 5, 7, 5, 4, 10, 4, 3, -18, 5, 1, -1, 1] # ans = - - - - - 
	#data = [3, 2, 2, 3, -1, 3, 2, -1, 1] # ans = 0 * *
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
	distance = [float('inf')] * n # list is an immutable type in python
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