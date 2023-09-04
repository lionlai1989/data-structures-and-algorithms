# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
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

    def preOrder(self):
        self.result = []

        def preorder_traversal(tree):
            if tree == -1:
                return

            self.result.append(self.key[tree])
            preorder_traversal(self.left[tree])
            preorder_traversal(self.right[tree])

        # Start from the root
        preorder_traversal(0)
                                
        return self.result

    def postOrder(self):
        self.result = []

        def postorder_traversal(tree):
            if tree == -1:
                return

            postorder_traversal(self.left[tree])
            postorder_traversal(self.right[tree])
            self.result.append(self.key[tree])

        # Start from the root
        postorder_traversal(0)
                                
        return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
