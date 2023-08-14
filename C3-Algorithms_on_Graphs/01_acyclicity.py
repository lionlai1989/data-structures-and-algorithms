#!/usr/bin/env python3
import sys

class Node():
	def __init__(self): 
		self.key = None
		self.pre = 0
		self.post = 0
		self.group = None
		self.adj = None

def dfs(node, v, group):
	dfs.clock += 1
	v.pre = dfs.clock
	v.group = group
	for w in v.adj:
		#print(w)
		if node[w].pre == 0:
			dfs(node, node[w], group)
		elif node[w].pre != 0 and node[w].post == 0:
			dfs.detect_cycle = 1

	dfs.clock += 1
	v.post = dfs.clock

def acyclic(adj):
	dfs.detect_cycle = 0
	dfs.clock = 0
	group = 0
	node = []
	for i in range(len(adj)):
		node.append(Node())
	for i in range(len(adj)):
		node[i].key = i
	for i in range(len(adj)):
		node[i].adj = adj[i]

	for n in node:
		if n.pre == 0:
			group += 1
			dfs(node, n, group)

	if dfs.detect_cycle == 1:
		return 1
	else:
		return 0

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
