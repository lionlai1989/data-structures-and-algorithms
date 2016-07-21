#!/usr/bin/env python3

from collections import defaultdict
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
    '''
    #using list
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        #self.n = 5 # 3
        #self.parent = [4, -1, 4, 1, 1]
        #self.n = 5 # 4
        #self.parent = [-1, 0, 4, 0, 3]
        #self.n = 10 # 6
        #self.parent = [8, 8, 5, 6, 7, 3, 1, 6, -1, 5] 
        #self.n = 10 # 4
        #self.parent = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1] 

        self.leaf = list(set(list(range(self.n))) - set(self.parent)) # find leaves of a tree
        self.parent = [ [i, self.parent[i]] for i in list(range(self.n)) ] 
        self.maxHeight = []
        
    def compute_height(self, index, height):
        if index in self.leaf:
            self.leaf.remove(index)
            self.maxHeight.append(height)
            return 
        #self.parent = [row[0] for row in self.parent if not (row[1] == tree) ]
        height += 1
        # ":" It makes the copy of the slice of self.parent[]. i.e. creation of 
        # the original list.
        # self.parent[:] != self.parent[]
        for row in self.parent[:]: 
            #print(row)
            if (row[1] == index):
                self.compute_height(row[0], height)
                self.parent.remove(row)
            else:
                pass
        return max(self.maxHeight)
    '''
    
    
    # using dict, it's much FASTER than list.
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        #self.n = 5 # 3
        #self.parent = [4, -1, 4, 1, 1]
        #self.n = 5 # 4
        #self.parent = [-1, 0, 4, 0, 3]
        #self.n = 10 # 6
        #self.parent = [8, 8, 5, 6, 7, 3, 1, 6, -1, 5] 
        #self.n = 10 # 4
        #self.parent = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1] 
        self.d = defaultdict(list)
        for index, item in enumerate(self.parent):
            if item in self.d:
                self.d[item].append(index)
            else:
                self.d[item] = [index]      
        #print(self.d)                 
        self.maxHeight = 0


    def compute_height(self, index, height):
            tmp = height
            for i in self.d[index]:
                height = tmp
                height += 1
                #print('i = ', i, 'h = ', height)
                self.compute_height(i, height)
            self.maxHeight = max(self.maxHeight, height)
            #print('return', self.maxHeight)
            return self.maxHeight
    

    '''
    # lecturer's code
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        #self.n = 5 # 3
        #self.parent = [4, -1, 4, 1, 1]
        #self.n = 5 # 4
        #self.parent = [-1, 0, 4, 0, 3]
        #self.n = 10 # 6
        #self.parent = [8, 8, 5, 6, 7, 3, 1, 6, -1, 5] 
        #self.n = 10 # 4
        #self.parent = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1] 

    def compute_height(self, index, height):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        return maxHeight;
    '''



def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height(-1, 0))
    
threading.Thread(target=main).start()
