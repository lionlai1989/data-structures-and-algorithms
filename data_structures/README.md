#Binary Search Tree
We need binary search trees to solve RangeSearch and NearestNeighbors problems.<br>
a's key is larger than the key of any descendant of its left child, and smaller than the key of any descendant of its right child.<br>
Properties:<br>
  * 1. time: O(depth), if it's a balanced tree, its runtime O(log(n))<br>

![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    a -> b;
    a -> c;
    b -> d;
    b -> e;
  }
)<br>

```python
def search(key, node):
  if node is None or node.key == key:
    return node
  elif key < node.key:
    return search_recursively(key, node.left)
  else:  # key > node.key
    return search_recursively(key, node.right)
```
```python
def insert(key, node):
  if node is None:
    node = Node(key)
  elif key < node.key:
    insert(key, node.left);
  else:  # key > node.key
    insert(key, node.right);
```

![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    "*80*" -> 70;
    "*80*" -> 88;
    88 -> 86;
    88 -> 90;
    86 -> "*83*";
    86 -> 87;
  }
)<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    "*88*" -> 83;
    "*88*" -> 90;
    83 -> 78;
    83 -> 86;
    86 -> 80;
    86 -> "*87*";
  }
)<br>
```python
# find the node in the tree with the next largest key. if given node is largest number of the tree, it fails.
def next(node): 
  if node.right is not None:
    return leftDescendant(node.right)
  else
    return rightAncestor(node)
    
def leftDescendant(node):
  if node.left is None:
    return node
  else:
    return leftDescendant(node.left)
    
def rightAncestor(node):
  if node.key < node.parent.key:
    return node.parent
  else:
    return rightAncestor(node.parent)
```
```python
def delete(node):
  if node.right is None:
    remove node, promote node.left.
  else:
    x <- next(node)
    replace node by x, and promote x.right.
```
##rangeSearch
```python
def rangeSearch(left, right, root):
  l = []
  node = search(left, root)
  while node.key <= right:
    if node.key >= left
      l.append(node)
    node = next(node)
  return l
```
##AVL Tree(self-balancing binary search tree)

#Hash Tables<br>
##Direct Addressing<br>
Input: 0 <= n <= 999<br>
create an array[1000]<br>

|array|
|:---:|
|0|
|1|
|...|
|998|
|999|
##Hash Function<br>
For any set of objects S and any integer m > 0, a function h: S-->{0, 1, ..., m-1} is called a hash function.<br>
m is called the cardinality of hash function h.<br>
Properties:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. direct addressing with O(m) memory.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. we want small cardinality m.<br>
Collision: h(O<sub>1</sub>) == h(O<sub>2</sub>), O<sub>1</sub> != O<sub>2</sub><br>
###Chaining<br>
	
![Alt text](http://g.gravizo.com/g?
  digraph g {
    graph [
		  rankdir = "LR"
	  ];
	  node [
		  fontsize = "16"
		  shape = "ellipse"
	  ];
	  edge [
	  ];
	  	"node0" [
		label = "<f0> array| <f1> 0| <f2> 1| <f3> 2| <f4> 3| <f5> 4"
		shape = "record"
	];
	"node1" [
		label = "<f0> c"
		shape = "record"
	];
	"node2" [
		label = "<f0> d"
		shape = "record"
	];
	  "node3" [
		  label = "<f0> a"
		  shape = "record"
	  ];
	  "node4" [
		  label = "<f0> b"
		  shape = "record"
	  ];
	  "node0":f1 -> "node1":f0 [
	id = 0
	];
	"node0":f4 -> "node3":f0 [
	id = 1
	];
	"node3":f0 -> "node4":f0 [
	id = 2
	];
	"node1":f1 -> "node2":f0 [
	id = 3
	];
	}
)
Properties:<br>
  * 1. memory: O(m+n).<br>
  * 2. time: O(c+1), c is the length of the longest chain.<br>

###Note<br>
Python dictionaries are implemented using hash tables. It is an array whose indexes are obtained using a hash function on the keys. The goal of a hash function is to distribute the keys evenly in the array. 



I finished most of exams except<br>
'00_process_packages.py'<br>
'01_merging_tables.py'<br>
'02_hash_substring.py'<br>
'03_rope.py'<br>
<br>
#**Important Note:**<br>
In 01_job_queue.py, time exceeds limit when using my heap function, so I turned to using python module heapq. But heapq module looks no better than my code. It also uses sift_down and sift_up function.<br> 
In 03_set_range_sum.py, I implement insert, erase and search by myself. Wateching splay tree visualization helps to solve this problem.<br>
https://www.cs.usfca.edu/~galles/visualization/SplayTree.html<br>
Strange thing is that the logic between online visualization and lecture is not really the same, and online visulization seems to more makes sense to me.
