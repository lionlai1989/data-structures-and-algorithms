#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
    def __init__(self, tree):
        self.n = len(tree)
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = tree[i]
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
    
    def inOrder(self):
        self.result = []

        def inorder_traversal(tree):
            if tree == -1:
                return

            inorder_traversal(self.left[tree])
            self.result.append(self.key[tree])
            inorder_traversal(self.right[tree])

        # Start from the root
        inorder_traversal(0)
                        
        return self.result

def IsBinarySearchTree(tree):
    # Use inorder traversal to travel through the tree. The result must be
    # in ascending order. If the result is not in ascending order, then
    # it is not a binary search tree.

    if len(tree) == 0:
        return True

    t = Tree(tree)
    inorder_traversal = t.inOrder()

    # Traverse the result. Start from the 2nd element (index=1).
    for i in range(1, len(inorder_traversal)):
        # If the current element is smaller than the previous element,
        # then it is not in ascending order.
        if inorder_traversal[i] < inorder_traversal[i-1]:
            return False
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
