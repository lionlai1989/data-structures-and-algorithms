# python3

from sys import stdin
import copy
# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, summ, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = \
    (key, summ, left, right, parent)

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
    smallRotation(v);
    smallRotation(v);

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

def inOrder(v):
  print('haha')
  if v == None:
    #print('xxx')
    return
  if v.left != None:
    inOrder(v.left)
  print(v.key, '===')
  if v.left == None and v.right == None:
    return
  if v.right != None:
    inOrder(v.right)

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
  #update(root)
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
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
  root = merge(merge(left, new_vertex), right)

def erase(x): 
  global root
  (left, right) = split(root, x)
  if right == None:
    return
  else:
    if left == None and right.key == x:
      right = right.right
      #right.parent == None
      update(right)
      root = right
      return 
    elif left == None and right.key != x:
      update(right)
      root = right
      return
    elif left != None and right.key == x:
      right = right.right
      update(right)
      # find max value of left tree
      while left.right != None:
        left = left.right
      left = splay(left)
      update(left)
      left.right = right
      #right.parent = left
      update(left)
      root = left
      root = merge(left, right)
      return
    elif left != None and right.key != x:
      root = merge(left, right)
      update(root)
      return 
    else:
      raise 'error'
      print('fuuuuuuuuuuuuuuuuuuuuk yooooooooooooooou')
  
def search(x): 
  global root
  result, tmp = find(root, x)
  
  if result != None and result.key == x:
    root = splay(tmp)
    return True
  elif result != None and result.key != x:
    root = splay(tmp)
    return False
  else:
    root = splay(tmp)
    return False

def summ(fr, to): 
  global root
  left, middle = split(root, fr)
  middle, right = split(middle, to + 1)

  if middle != None:
    tmp = middle.sum

  inOrder(middle)
  #update(middle)
  root = merge(left, middle)
  update(root)
  root = merge(root, right)
  update(root)
  '''
  print('left =')
  inOrder(left)
  print('middle =')
  inOrder(middle)
  print('right =')
  inOrder(right)
  print('root =')
  inOrder(root)
  '''
  ans = 0

  if middle == None:
    return ans
  else:
    #inOrder(middle)
    
    return tmp

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
    #inOrder(root)
    
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    t.append('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
        
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = summ((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    '''
    t.append('===')
    t.append('s')
    t.append(l)
    t.append(r)
    t.append(res)
    t.append('===')
    '''
    t.append(res)
    print('res = ', res)
    last_sum_result = (res) % MODULO
    print('last sum result =', last_sum_result)
  inOrder(root)
  print()
for i in range(len(t)):
  print(t[i])
