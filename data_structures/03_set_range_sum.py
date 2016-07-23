#!/usr/bin/env python3

from sys import stdin
import copy

# Splay tree implementation
# I implement insert, erase and search by myself, wateching splay tree 
# visualization helps to solve this problem. 
# https://www.cs.usfca.edu/~galles/visualization/SplayTree.html
# Strange thing is, the logic between online visualization and lecture is not 
# really the same, and online visulization seems more makes sense to me.

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, s, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = \
    (key, s, left, right, parent)

def print_vertex(v):
  print('v =', v)
  if v == None:
    return
  print('key =', v.key, ', sum =', v.sum, \
    ', left =', v.left, ', right =', v.right, ', parent =', v.parent)
  if v.left == None and v.right == None:
    return
  if v.left != None:
    print_vertex(v.left)
  if v.right != None:
    print_vertex(v.right)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)
  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right
 
# Code that uses splay tree to solve the problem
root = None

def insert(x):
  global root
  v = root
  key = x
  if v == None:
    v = Vertex(x, x, None, None, None)
  while v != None:
    if v.key == key:
      break    
    if v.key < key:
      if v.right == None:
        v.right = Vertex(x, x, None, None, v)
        v = v.right
      else:
        v = v.right
    else: 
      if v.left == None:
        v.left = Vertex(x, x, None, None, v)
        v = v.left
      else:
        v = v.left
  root = splay(v)
  update(root)
  return

  '''
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None) #self.key, self.sum, self.left, self.right, self.parent
  root = merge(merge(left, new_vertex), right)
  '''
  
def erase(x):
  global root
  v = root
  key = x
  if v == None:
    return
  while v != None:
    if v.key == key:
      break    
    if v.key < key:
      if v.right == None:
        root = splay(v)
        update(root)
        return
      else:
        v = v.right
    else: 
      if v.left == None:
        root = splay(v)
        update(root)
        return
      else:
        v = v.left
  root = splay(v)
  update(root)
  if root.right != None and root.left != None:
    left = root.left
    root.left = None
    left.parent = None
    while left.right != None:
      left = left.right
    left = splay(left)
    update(left)
    
    right = root.right
    right.parent = None
    update(right)
    right.parent = left
    left.right = right
    root = splay(left)
    if root != None:
      root.parent = None
    update(root)
  elif root.right == None and root.left != None:
    left = root.left
    root.left = None
    left.parent = None
    while left.right != None:
      left = left.right
    root = splay(left)
    if root != None:
      root.parent = None
    update(root)
  elif root.right != None and root.left == None:
    right = root.right
    root.right = None
    right.parent = None
    root = splay(right)
    if root != None:
      root.parent = None
    update(root)
  elif root.right == None and root.left == None:
    root = None
  else:
    raise 'error'
    print('fuuuuuuuuuuuuuuuuuuuuk yooooooooooooooou')
  return
  '''
  global root
  # Implement erase yourself
  # pass
  (left, right) = split(root, x)
  if right == None or right.key != x:
    root = merge(left,right)
    return
  right = right.right
  if right != None:
    right.parent = None
  root = merge(left,right)
  '''

def search(x):
  global root
  v = root
  key = x
  tmp = False
  if v == None:
    return tmp
  while v != None:
    if v.key == key:
      tmp = True
      break    
    if v.key < key:
      if v.right == None:
        tmp = False
        break
      else:
        v = v.right
    else: 
      if v.left == None:
        tmp = False
        break
      else:
        v = v.left
  root = splay(v)
  update(root)
  return tmp
  '''
  global root
  # Implement find yourself
  (result, root) = find(root, x)
  if result != None and result.key == x:
    return True
  return False
  '''

def summ(fr, to):
  '''
  global root
  tmp = copy.deepcopy(root) # copy.deepcopy is useless
  left, middle = split(root, fr)
  middle, right = split(middle, to + 1)
  root = tmp
  if middle != None:
    return middle.sum
  else:
    return 0
  
  global root
  original = copy.deepcopy(root)
  match = 0
  if root == None:
    return 0
  while root != None: 
    if root.key == fr:
      match = 1
      break
    if root.key < fr:
      if root.right == None:
        root.right = Vertex(fr, fr, None, None, root)
        root = root.right
      else:
        root = root.right
    else: 
      if root.left == None:
        root.left = Vertex(fr, fr, None, None, root)
        root = root.left
      else:
        root = root.left
  root = splay(root)
  update(root)
  if match == 1:
    if root.left != None:
      root.sum = root.sum - root.left.sum
      root.left.parent = None
      root.left = None
    #splay(root)
    #update(root)
    match = 0
  else:
    right = root.right
    root.right = None
    right.parent = None
    root = right
    #splay(root)
    #update(root)

  if root == None:
    return 0
  while root != None: 
    if root.key == to:
      match = 1
      break
    if root.key < to:
      if root.right == None:
        root.right = Vertex(to, to, None, None, root)
        root = root.right
      else:
        root = root.right
    else: 
      if root.left == None:
        root.left = Vertex(to, to, None, None, root)
        root = root.left
      else:
        root = root.left
  root = splay(root)
  update(root)
  if match == 1:
    if root.right != None:
      root.sum = root.sum - root.right.sum
      root.right.parent = None
      root.right = None
    #splay(root)
    #update(root)
    match = 0
  else:
    left = root.left
    root.left = None
    left.parent = None
    root = left
    #splay(root)
    #update(root)
  tmp1 = root.sum
  root = original
  return tmp1 
  '''
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  ans = 0

  if middle != None:
    ans = middle.sum
  root = merge(merge(left,middle),right)
  return ans

t = []
MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)

  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)

  elif line[0] == '?':
    x = int(line[1])
    #print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    t.append('Found' if search((x + last_sum_result) % MODULO) else 'Not found')

  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = summ((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    t.append(res)
    last_sum_result = (res) % MODULO

for i in range(len(t)):
  print(t[i])
