#!/usr/bin/env python3

import sys
import numpy as np

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def size(self):
        return(len(self.items))


if __name__ == "__main__":
    text = sys.stdin.read()
    s = Stack()
    status = True
    #opening_brackets_stack = []
    for i, next in enumerate(text, start=1): # start=1 demanded by the task
        if next == '(' or next == '[' or next == '{':
            s.push([i, next])
        if next == ')' or next == ']' or next == '}':
            if s.isEmpty() == True:
                status = False
                break
            tmp = s.pop()
            #print(tmp)
            if tmp[1] == '(' and next == ')':
                pass
            elif tmp[1] == '[' and next == ']':
                pass
            elif tmp[1] == '{' and next == '}':
                pass
            else:
                status = False
                break
    
    if status == False:
        print(i)
    elif s.isEmpty() == False:
        print(s.pop()[0])
    else:
        print("Success")
            
   
   