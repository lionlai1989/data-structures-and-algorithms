#!/usr/bin/env python3
import sys

class Node():
	def __init__(self):
		self.key = None
		self.pre = 0
		self.post = 0
		self.group = None
		self.adj = None

topolist = []
def dfs(node, v, group):
	global topolist
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
	topolist.append(v.key)

def toposort(adj):
	global topolist

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

	return	topolist

'''
class Node():
	def __init__(self, adj):
		# color = None, not has been visited
		# color = 0, has been visited
		# color = 1, has been backtracked
		self.color = [None] * len(adj)
		self.visited = [None] * len(adj) 
		self.tmp = 0
		self.l = []

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
	node.l.append(v)
	return 


def toposort(adj):
	node = Node(adj)
	for index, item in enumerate(node.visited):
		if item is None:
			if dfs(adj, index, node) == 1:
				return 1
	return node.l
'''
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
	#print(order)
	for x in order[::-1]:
		print(x + 1, end=' ')

