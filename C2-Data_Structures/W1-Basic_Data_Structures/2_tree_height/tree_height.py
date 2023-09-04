# python3

import sys
import threading
from collections import deque

def compute_height(n, parents):
    # Naive solution:
    max_height = 0

    # key is from 0 to n-1.
    for key in range(n):
        height = 0
        current = key

        # current will trace back to root.
        while current != -1:
            height += 1

            # Trace one level up.
            current = parents[current]

        # Update max_height if height > max_height
        max_height = max(max_height, height)
    return max_height


class Node:
    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_child(self, node):
        self.nodes.append(node)

    def __repr__(self):
        return f"NonBinTree({self.val}): {self.nodes}"


def find_tree_depth_dfs(root):
    if not root:
        return 0

    max_child_depth = 0
    for child in root.nodes:
        child_depth = find_tree_depth_dfs(child)
        max_child_depth = max(max_child_depth, child_depth)

    return max_child_depth + 1

def find_tree_depth_bfs(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    depth = 0

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current = queue.popleft()
            for child in current.nodes:
                queue.append(child)
        depth += 1

    return depth

def compute_height_faster(n, parents):
    # Faster solution:
    nodes = [Node(i) for i in range(n)]
    
    for i in range(n):
        parent_idx = parents[i]
        if parent_idx == -1:
            root = i
        else:
            nodes[parent_idx].add_child(nodes[i])

    depth = find_tree_depth_bfs(nodes[root])
    return depth


def main():
    # Use the following as input:
    # 10
    # 9 7 5 5 2 9 9 9 2 -1
    # Output:
    # 4
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_faster(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
