# Algorithms on Graphs

## Description

This section provides a brief overview of the course content for each week. The notation
used here designates V as the set of all vertices and E as the set of all edges.

-   Week 1: Decomposition of Graphs 1

    This section covers the fundamentals of undirected graphs. First, it explores three
    common graph representations. For instance, consider the graph below:

    ```
          B   C
           \ /|
            A |
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

    Later, it discusses checking the reachability of all vertices and finding connected
    components in a graph, both with a time complexity of $O(|V|+|E|)$.

    Finally, adding preorder and postorder attributes to vertices can track the
    execution of a DFS. One important feature of this is that for any vertices, u and v,
    the intervals `(pre(u), post(u))` and `(pre(v), post(v))` are either nested or disjoint.

-   Week 2: Decomposition of Graphs 2

-   Week 3: Paths in Graphs 1

-   Week 4: Paths in Graphs 2

-   Week 5: Minimum Spanning Trees

-   Week 6: Advanced Shortest Paths Algorithms: 1000 to 25000 times faster than the
    classical Dijkstra's algorithm in practice

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
