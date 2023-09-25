# Algorithms on Graphs

## Description

This section provides a brief overview of the course content for each week. The notation
used here designates $G$ as a graph, $V$ as the set of all vertices and $E$ as the set
of all edges.

### Week 1: Decomposition of Graphs 1

This section covers the fundamentals of undirected graphs. First, it explores three
common graph representations. For instance, consider the graph below:

```
      B     C
       \   /|
        \ / |
         A  |
          \ |
           \|
            D
```

The representations are as follows:

**Edge list:**

```
(A, B), (A, C), (A, D), (C, D)
```

**Adjacency Matrix:**

```
  A B C D
A 0 1 1 1
B 1 0 0 0
C 1 0 0 1
D 1 0 1 0
```

**Adjacency List:**

```
A.adj: [B, C, D]
B.adj: [A]
C.adj: [A, D]
D.adj: [A, c]
```

Later, it discusses checking the reachability of all vertices and finding **connected
components** in a graph, both with a time complexity of $O(|V|+|E|)$.

Finally, adding preorder and postorder attributes to vertices can track the execution of
a DFS. One important feature of this is that for any vertices, u and v, the intervals
`(pre(u), post(u))` and `(pre(v), post(v))` are either nested or disjoint.

### Week 2: Decomposition of Graphs 2

It introduces directed graphs, specifically **Directed Acyclic Graphs (DAGs)**, known
for their cycle-free nature. It also introduces **Strongly Connected Components
(SCCs)**. It's noteworthy that the metagraph of any graph $G$ is inherently a DAG. It
subsequently details the process of identifying SCCs within a graph $G$, which begins
with the reversal of the graph $G^R$.

### Week 3: Paths in Graphs 1

It introduces **Breadth-First Search (BFS)** for finding minimum distances between any
two vertices and constructing the shortest path between them with a runtime of
$O(|E| + |V|)$.

### Week 4: Paths in Graphs 2

Until this week, graphs were introduced without edge weights. Starting this week and
continuing onward, graphs will be introduced with weighted edges.

### Week 5: Minimum Spanning Trees

### Week 6: Advanced Shortest Paths Algorithms

## Reference:

-   Week 1:

    -   [Depth-First Search (DFS) Visualization](https://www.cs.usfca.edu/~galles/visualization/DFS.html)

-   Week 2:

    -   [Topological sort using Depth-First Search](https://www.cs.usfca.edu/~galles/visualization/TopoSortDFS.html)
    -   [Topological sort using indegree array](https://www.cs.usfca.edu/~galles/visualization/TopoSortIndegree.html)
    -   [Strongly Connected Components](https://www.cs.usfca.edu/~galles/visualization/ConnectedComponent.html)

-   Week 3:

    -   [Breadth-First Search Visualization](https://www.cs.usfca.edu/~galles/visualization/BFS.html)

-   Week 4:

    -   [Dijkstra's Algorithm Visualization](https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html)

-   Week 5:

    -   [Kruskal's Algorithm Visualization](https://www.cs.usfca.edu/~galles/visualization/Kruskal.html)

-   Week 6:
