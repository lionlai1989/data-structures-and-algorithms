# python3

from sys import stdin
import copy
# Splay tree implementation

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
  
  print('++++')
  print_vertex(root)
  print('++++')
  
  (left, right) = split(root, x)
  
  print('###')
  print_vertex(left)
  print('~~~~~~~')
  print_vertex(right)
  print('###')
  
  if right == None:
    new_vertex = Vertex(x, x, None, None, None)
    new_vertex.right = right
    update(new_vertex)
    root = merge(left, new_vertex)
    return
  elif right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
    right.parent = new_vertex
    new_vertex.right = right
    update(new_vertex)
    root = merge(left, new_vertex)
    return
  elif right.key == x:
    root = merge(left, right)
    return
  else:
    raise 'error'
    print('fuuuuuuuuuuuuuuuuuuuuk yooooooooooooooou')


def erase(x):
  global root
  left, right = split(root, x)
  '''
  print('!!!')
  print_vertex(left)
  print('!!!')
  print_vertex(right)
  print('!!!')
  '''
  if right == None:
    root = merge(left, right)
    return
  else: 
    if left == None and right.key == x:
      right = right.right
      if right != None:
        right.parent = None
      update(right)
      root = merge(left, right)
      return 
    elif left == None and right.key != x:
      #update(right)
      root = merge(left, right)
      return
    elif left != None and right.key != x:
      root = merge(left, right)
      #update(root)
      return 
    elif left != None and right.key == x:
      right = right.right
      if right != None:
        right.parent = None
      update(right)
      # find max value of left tree
      while left.right != None:
        left = left.right
      left = splay(left)
      update(left)
      
      left.right = right
      if right != None:
        right.parent = left
      update(left)
      root = left

      #root = merge(left, right)
      return
    else:
      raise 'error'
      print('fuuuuuuuuuuuuuuuuuuuuk yooooooooooooooou')

def search(x):
  global root
  left, right = split(root, x)
  if right == None:
    root = merge(left, right)
    return False
  else:
    if right.key == x:
      root = merge(left, right)
      return True
    elif right.key != x:
      root = merge(left, right)
      return False
    else:
      raise 'error'
      print('fuuuuuuuuuuuuuuuuuuuuk yooooooooooooooou')
  
def summ(fr, to):
  global root
  tmp = copy.deepcopy(root)
  left, middle = split(root, fr)
  middle, right = split(middle, to + 1)
  root = tmp
  if middle != None:
    return middle.sum
  else:
    return 0

t = []
MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  #print('$$$$$$$$$$$$$$$')
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
    #print('======')
    print_vertex(root)#

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
    last_sum_result = (res) % MODULO
    t.append(res)
    #print(res)
    #print('res = ', res)
    #print('last sum result =', last_sum_result)
  #print('===')
#print_vertex(root)

for i in range(len(t)):
  print(t[i])
