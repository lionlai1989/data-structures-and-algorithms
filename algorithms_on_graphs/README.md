#Decomposition of Graphs
runtimes of vertices: |V|<br>
runtimes of edges: |E|<br>
Density: how many of edges you have in terms of the number of vertices.<br>
Dense Grapsh: a large fraction of pairs of vertices are connected by edges |E| ~ |V|<sup>2</sup>.<br>
Sparse Grapsh: each vertex has only a few edges.<br>

![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    A -> B;
    A -> C;
    A -> D;
    C -> D;
  }
)<br>

edge list:<br>
edges (A, B), (A, C), (A, D), (C, D)<br>

adjacency matrix:<br>

|   | A |  B  | C | D |
|---|---|:---:|---|---|
| A |   |  1  | 1 | 1 |
| B | 1 |  0  | 0 | 0 |
| C | 1 |  0  | 0 | 1 |
| D | 1 |  0  | 1 | 0 |

adjacent list:<br>
A: [B, C, D]<br>
B: []<br>
C: [D]<br>
D: []<br>

clock: store the number of visits, clock ticks at every pre/post visit.<br>
pre(x) : entrance time of x<br>
post(x): exit time of x<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    "1/4" -> "2/3";
    "5/12" -> "6/11";
    "6/11" -> "7/8";
    "6/11" -> "9/10";
  }
)<br>
**lemma:** [pre(u), post(u)], [pre(v), post(v)] are either nested or disjoint.<br>
#DFS stack vs. BFS queue
**note**: Using iteration to implement DFS is not bad, but it can not record pre(vertex) and post(vertex). I choose to use **recursion** to implement DFS. For BFS, using **iteration** is a better choice because it makes more sense and is easy to understand.<br>
```c++
bfs(G)
{
  list L = empty
  shortest_path_tree T = empty
  choose a starting vertex x
  search(x)
  while(L nonempty)
    remove edge (v,w) from start of L
    if w not yet visited
    {
      add (v,w) to T
      T[w] = v
      search(w)
    }
}

dfs(G)
{
list L = empty
tree T = empty
choose a starting vertex x
search(x)
while(L nonempty)
  remove edge (v,w) from end of L
  if w not yet visited
  {
    add (v,w) to T
    search(w)
  }
}

search(vertex v)
{
  visit(v);
  for each edge (v,w)
    add edge (v,w) to end of L
}
```
##Linearing Ordering
A cycle in a Graph G is a sequence of vertices v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>n-1</sub>, v<sub>n</sub> so that (v<sub>1</sub>, v<sub>2</sub>), (v<sub>2</sub>, v<sub>3</sub>), ..., (v<sub>n-1</sub>, v<sub>n</sub>), (v<sub>n</sub>, v<sub>1</sub>) are all edges.<br>
If G contains a cycle, it cannot be linearly ordered.<br>
A directed graph G is a Directed Acyclic Graph(**DAG**) if it has no cycle.<br>
Any **DAG** can be linearly ordered.<br>
A **source** is a vertex with no incoming edges.<br>
A **sink** is a vertex with no outgoing edges.<br>
**Theorem:** If G is DAG, with an edge u to v, post(u) > post(v).<br>

##Connectivity in Digraphs
**Strongly Connected Components(SCC)**<br>
Two vertices v, w in a directed graph are connected if you can reach v from w and can reach w from v.<br>
A directed graph can be connected into SCC where two vertices are connected if and only if they are in the same component.<br>
Metagraph describes how SSC connected to each other and it's always a DFG.<br>
##Paths and Lengths<br>
Lengths of the path L(P) is the number of edges in the path.<br>
L(D - E - S - A -B) = 4<br>
L(D - S - C - B) = 3<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    D -> E;
    S -> D;
    E -> S;
    S -> A;
    A -> B;
    S -> C;
    C -> B;
  }
)<br>
##Distance
The distance between two vertices is the length of the **shortest** path between them.<br>
d(D, B) = 3<br>
### Distance Layers<br>
Starting point is layer 0.<br>
##Breadth First Search(BFS)
Properties: The running time of breadth-first search is O(|E| + |V|).<br>
##Reachability
Node u is reachable from node S if there is a path from S to u.<br>
##Shortest Path Tree<br>
Consider the shortest path tree(bottom) built by breadth first search from vertex S on the graph(top).<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    D -> E;
    S -> D;
    S -> A;
    A -> B;
    S -> C;
    C -> B;
    D -> F;
    F -> G;
    B -> G;
    G -> H;
    S -> E;
    B -> H;
  }
)<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    G -> B;
    H -> B;
    B -> A;
    F -> D;
    A -> S;
    C -> S;
    D -> S;
    E -> S;
  }
)<br>
**Lemma:**Shortest path tree is indeed a tree.(There is no cycle in tree)<br>
**node:** remove clock, pre and post from class Node. They seem to be useless in BFS.
##Shortest path with **non-negative** edge weights.
###Dijkstra's algorithm
```python
 1  function Dijkstra(Graph, source):
 2
 3      create vertex set Q
 4
 5      for each vertex v in Graph:             // Initialization
 6          dist[v] ← INFINITY                  // Unknown distance from source to v
 7          prev[v] ← UNDEFINED                 // Previous node in optimal path from source
 8          add v to Q                          // All nodes initially in Q (unvisited nodes)
 9
10      dist[source] ← 0                        // Distance from source to source
11      
12      while Q is not empty:
13          u ← vertex in Q with min dist[u]    // Source node will be selected first
14          remove u from Q 
15          
16          for each neighbor v of u:           // where v is still in Q.
17              alt ← dist[u] + length(u, v)
18              if alt < dist[v]:               // A shorter path to v has been found
19                  dist[v] ← alt 
20                  prev[v] ← u 
21
22      return dist[], prev[]
```
**Running time:** O(|V|<sup>2</sup>) or O((|V|+|E|)log(|V|)) depending on the implementation.<br>

##Shortest path with negative and positive edge weights.
**Triangular arbitrage** insert photo
xy --> max <=> log<sub>2</sub.(x) + log<sub>2</sub.(y)<br>
j = 1 to k, &sum; log(r<sub>e<sub>j</sub></sub>) --> max<br>
j = 1 to k, &sum; -log(r<sub>e<sub>j</sub></sub>) --> min<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    RUBLE -> EURO [label="0.013"];
    RUBLE -> USDOLLAR [label="0.015"];
    EURO -> USDOLLAR [label="1.16"];
  }
)<br>
0.013 * 1.16 = 0.01508 > 0.015<br>
-logarithmize<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    RUBLE -> EURO [label="6.2653"];
    RUBLE -> USDOLLAR [label="6.0589"];
    EURO -> USDOLLAR [label="-0.214"];
  }
)<br>
6.2653 - 0.214 = 6.0513 < 6.0589<br>
Negative Weight Cycle:<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    S -> A [label="4"];
    S -> B [label="3"];
    A -> B [label="-2"];
    B -> C [label="-3"];
    C -> A [label="4"];
    B -> D [label="1"];
    C -> D [label="2"];
  }
)<br>
d(S, A) = d(S, B) = d(S, C) = d(S, D) = -&infin;<br>
###Bellman–Ford algorithm
```python
function BellmanFord(list vertices, list edges, vertex source)
   ::distance[],predecessor[]

   // This implementation takes in a graph, represented as
   // lists of vertices and edges, and fills two arrays
   // (distance and predecessor) with shortest-path
   // (less cost/distance/metric) information

   // Step 1: initialize graph
   for each vertex v in vertices:
       distance[v] := inf             // At the beginning , all vertices have a weight of infinity
       predecessor[v] := null         // And a null predecessor
   
   distance[source] := 0              // Except for the Source, where the Weight is zero 
   
   // Step 2: relax edges repeatedly
   for i from 1 to size(vertices)-1: # We do V-1 times since vertex would be possibly updated after every iteration.
                                     # If no distance being update during iteration, the iteration can be stopped.
       for each edge (u, v) with weight w in edges:
           if distance[u] + w < distance[v]:
               distance[v] := distance[u] + w
               predecessor[v] := u
        

   // Step 3: check for negative-weight cycles
   for each edge (u, v) with weight w in edges:
       if distance[u] + w < distance[v]:
           error "Graph contains a negative-weight cycle"
   return distance[], predecessor[]
```
**Running time:** O(|V||E|).<br>
Corollary1: In a graph without negative weight cycles, Bellman-Ford algorithm correctly finds all distances from the starting node S.<br>
Corollary2: If there is no negative weight cycle reachable from S such that u is reachable from this negative weight cycle, Bellman-Ford algorithm correctly finds dist[u] = d(S, U)<br>
###Detect Infinite Arbitrage
Note that there is an advanced problem "Exchanging Money Optimally" in the Programming Assignment 4, and to solve that problem you will need to implement a criterion to determine whether the shortest path from one node to another node in the graph can be made arbitrarily short. The correct criterion for testing that there exist arbitrarily short paths from node S to node u (or, equivalently, that **the shortest path from S to u is −∞**; or that infinite arbitrage is possible for exchanging US dollars into Russian rubles) is the following:<br>
1. Run Bellman-Ford's algorithm to find shortest paths from node S for exactly |V|-1 iterations, where |V| is the number of nodes in the graph.<br>
2. Save all the nodes for which the distance estimate was decreased on the V-th iteration - denote the set of these nodes by A.<br>
3. Find all nodes reachable from any node in A, use breadth-first search to do that (put all the nodes from A in the queue initially, then run the regular breadth-first search with that queue). Denote the set of these nodes by B.<br>
4. There exist arbitrarily short paths from S to u if and only if u is in the set B.<br>
