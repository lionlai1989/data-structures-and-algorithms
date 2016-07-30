#!/usr/bin/env python3
import sys
# Using recursive call to implement DFS

class Node():
	def __init__(self): 
		self.key = None
		self.pre = 0
		self.post = 0
		self.count = 0
		self.adj = None

def dfs(node, v, group):
	dfs.clock += 1
	v.pre = dfs.clock
	v.group = group
	for w in v.adj:
		if node[w].pre == 0:
			dfs(node, node[w], group)
		elif node[w].pre != 0 and node[w].post == 0:
			dfs.detect_cycle = 1
			
	dfs.clock += 1
	v.post = dfs.clock


def number_of_components(adj):
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

	return group

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	# sys.stdin.read() will read from standard input till EOF.
	# (which is usually Ctrl+D)
	n, m = data[0:2]
	data = data[2:]
	# print(n, m)
	# print(data)
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
		adj[b - 1].append(a - 1)
	#print(adj)
	print(number_of_components(adj))
