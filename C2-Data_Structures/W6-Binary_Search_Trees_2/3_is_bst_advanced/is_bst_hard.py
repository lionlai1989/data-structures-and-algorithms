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
    

def IsBinarySearchTree(tree):

    if len(tree) == 0:
        return True

    t = Tree(tree)
    # print("t.key: ", t.key)
    def is_bst(tree, minimum, maximum):
        if tree == -1:
            return True

        if minimum != -1 and t.key[tree] < minimum:
           return False
        if maximum != -1 and t.key[tree] >= maximum:
           return False

        return is_bst(t.left[tree], minimum, t.key[tree]) and is_bst(t.right[tree], t.key[tree], maximum)
        
    return is_bst(0, -1, -1)

    # def is_bst(tree, minimum, maximum):
    #     if tree == -1:
    #         return True

    #     left_child = t.left[tree]
    #     # print("left_tree: ", left_child)
    #     right_child = t.right[tree]
    #     # print("right_tree: ", right_child)

    #     if left_child != -1 and t.key[left_child] >= t.key[tree]:
    #        # If left_child == -1, it doesn't make sense to compare because
    #        # there is no left child.
    #        return False
    #     if right_child != -1 and t.key[right_child] < t.key[tree]:
    #        # If right_child == -1, it doesn't make sense to compare because
    #        # there is no left child.
    #        return False

    #     if is_bst(t.left[tree], minimum, t.key[tree]) is True and is_bst(t.right[tree], t.key[tree], maximum) is True:
    #        return True
    #     else:
    #        return False

    # return is_bst(0, -1, -1)

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
