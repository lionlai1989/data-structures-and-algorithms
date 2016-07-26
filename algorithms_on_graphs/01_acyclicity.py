#!/usr/bin/env python3
import sys


class Node():
	def __init__(self, adj):
		# color = None, not has been visited
		# color = 0, has been visited
		# color = 1, has been backtracked
		self.color = [None] * len(adj)
		self.visited = [None] * len(adj) 
		self.tmp = 0

	
def dfs(adj, v, node):
	#print('===')
	if node.color[v] == 0:
		node.tmp = 1
		return 1

	#print(node.color)
	#print(node.visited)
	
	node.visited[v] = 0
	node.color[v] = 0
	for w in adj[v]:
		#print(w)
		
		if node.visited[w] is None:
			#print('aaa')
			dfs(adj, w, node)
		elif node.color[w] == 0:
			node.tmp = 1
			return 1
	node.color[v] = 1
	return 

def acyclic(adj):
	node = Node(adj)
	for index, item in enumerate(node.visited):
		if item is None:
			if dfs(adj, index, node) == 1:
				return 1
	return node.tmp

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	#n, m = [4, 3] # ans = 0
	#data = [1, 2, 3, 2, 4, 3]
	#n, m = [4, 4] # ans = 1
	#data = [1, 2, 2, 3, 3, 1, 4, 1]
	#n, m = [5, 7] # ans = 0
	#data = [1, 2, 2, 3, 1, 3, 3, 4, 1, 4, 2, 5, 3, 5]
	#n, m = [6, 7] # ans = 1
	#data = [3, 2, 1, 3, 2, 4, 4, 3, 4, 6, 6, 5, 4, 5]
	#n, m = [6, 6] # ans = 1
	#data = [1, 2, 2, 5, 5, 4, 4, 3, 4, 6, 3, 5]
	#n, m = [5, 8] # ans = 1
	#data = [1, 2, 1, 3, 2, 3, 2, 4, 3, 4, 3, 5, 1, 5, 3, 1]
	#n, m = [5, 7] # ans = 0
	#data = [1, 2, 1, 3, 2, 3, 2, 4, 3, 4, 3, 5, 1, 5]


	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)

	print(acyclic(adj))
