# Data Structures

## Description

This section provides a brief overview of the course content for each week.

### Week 1: Basic Data Structures

Arrays and linked lists serve as fundamental building blocks for data storage in
computers, and there's no any other option. I explore the advantages and drawbacks of
both arrays and singly/doubly linked lists. Later, I dive into abstract data structures,
stacks (First In, Last Out) and queues (First In, First Out). The choice between
array-based and linked list-based implementations of stacks and queues depends on
specific application needs. Some applications may prefer arrays, while others may opt
for linked lists. Finally, a brief overview of binary trees is introduced.

### Week 2: Dynamic Arrays and Amortized Analysis

As introduced in week 1, primitive arrays have a fixed size. To overcome this
limitation, I can use an abstraction data type called a dynamic array, which allows for
resizable arrays, offering greater convenience. To my surprise, both C++'s `std::vector`
and Python's `list` rely on resizable dynamic arrays as their underlying
implementations, rather than linked lists. Dynamic arrays must periodically resize
themselves, necessitating the copying of $n$ elements to a new array, resulting in a
time complexity of $O(n)$ for this operation. However, the amortized cost for each
insert operation remains constant at $O(1)$.

### Week 3: Priority Queues and Disjoint Sets

Priority queues is an abstract data type where each element is assigned a priority, and
elements are extracted in order based on their priority. In C++, you can use
`priority_queue`, while in Python, `heapq` serves this purpose. Priority queues can be
implemented using arrays, linked lists, but are most commonly implemented with
tree-structured binary min/max heaps, where the insertion and extraction of min/max
values have a time complexity of $O(log(n))$.

Disjoint sets, on the other hand, offer solutions to various practical problems, such as
finding a path from an entrance to an exit in a maze or determining the number of
connected components in a graph, particularly useful for addressing graph-related
challenges. Typically, disjoint sets are implemented using linked list-based tree
structures, providing an amortized constant cost of $O(log^{\ast}(n))$ for a single
operation. It's important to highlight that for any practical value of $n$, even as
large as $2^{65536}$, the value of $log^{\ast}(n)$ remains less than 5.

### Week 4: Hash Tables

An implementation of a **Set** or a **Map** using hashing is commonly referred to as a
hash table. In C++, you can use `unordered_set` for **Set** and `unordered_map` for
**Map**, while in Python, `set` serves as **Set**, and `dict` is used for **Map**. Hash
tables have a memory consumption cost of $O(n + m)$ and an operation cost of $O(c + 1)$,
where:

-   $n$ represents the number of objects,
-   $m$ is the cardinality of the hash function, and
-   $c$ denotes the longest chain length.

### Week 5: Binary Search Trees 1

It covers the fundamentals of binary search trees (BSTs) and AVL trees, which are a type
of balanced binary search tree. In an AVL tree, for every node N, the absolute
difference between the heights of its left and right subtrees is always less than or
equal to 1, $|N.left.height - N.right.height| \le 1$. This balance property allows us to
execute all tree operations in logarithmic time complexity $O(log(n))$.

### Week 6: Binary Search Trees 2

It discusses the utility of BSTs in order statistics, enabling the retrieval of the k-th
largest element, the median, or the 25th percentile element efficiently. Subsequently,
it dives into Splay trees, which aim to optimize tree access patterns. Splay trees
capitalize on prior knowledge of frequently accessed nodes by reorganizing the tree to
position them closer to the root for quicker access.

## Reference:

-   Week 1:

    -   [array-based stack](http://www.cs.usfca.edu/~galles/visualization/StackArray.html)
    -   [list-based stack](http://www.cs.usfca.edu/~galles/visualization/StackLL.html)
    -   [array-based queue](http://www.cs.usfca.edu/~galles/visualization/QueueArray.html)
    -   [list-based queue](http://www.cs.usfca.edu/~galles/visualization/QueueLL.html)
    -   [Python list vs. array – when to use?](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use)

-   Week 2:

    -   [Additional Video on Amortized Analysis](https://www.youtube.com/watch?v=U5XKyIVy2Vc)

-   Week 3:

    -   [min-heap visualization](http://www.cs.usfca.edu/~galles/visualization/Heap.html)

-   Week 4:

-   Week 5:

    -   [AVL tree Wiki](https://en.wikipedia.org/wiki/AVL_tree)
    -   [AVL Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html)

-   Week 6:

    -   [Splay Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/SplayTree.html)
    -   [AVL Tree v.s. Splay Tree](https://stackoverflow.com/questions/7467079/difference-between-avl-trees-and-splay-trees)
    -   [The original paper of Splay Tree](https://www.cs.cmu.edu/~sleator/papers/self-adjusting.pdf)
