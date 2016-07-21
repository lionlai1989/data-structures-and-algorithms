# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size



class TreeOrders:
    def __init__(self):
        self.inList = []
        self.preList = []
        self.postList = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        #print(self.n)
        #print(self.key)
        #print(self.left)
        #print(self.right)

    def inOrder(self, node):
        if self.left[node] != -1:
            self.inOrder(self.left[node])
        #print(self.key[node])
        self.inList.append(self.key[node])
        if self.left[node] == -1 and self.right[node] == -1:
            return
        if self.right[node] != -1:
            self.inOrder(self.right[node])
        return self.inList

    def preOrder(self, node):
        #print(self.key[node])
        self.preList.append(self.key[node])
        if self.left[node] == -1 and self.right[node] == -1:
            return
        if self.left[node] != -1:
            self.preOrder(self.left[node])
        if self.right[node] != -1:
            self.preOrder(self.right[node])
        return self.preList
       
    def postOrder(self, node):
        if self.left[node] != -1:
            self.postOrder(self.left[node])
        if self.right[node] != -1:
            self.postOrder(self.right[node]) 
        #print(self.key[node])
        self.postList.append(self.key[node])
        if self.left[node] == -1 and self.right[node] == -1:
            return
        return self.postList

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder(0)))
    print(" ".join(str(x) for x in tree.preOrder(0)))
    print(" ".join(str(x) for x in tree.postOrder(0)))

threading.Thread(target=main).start()
