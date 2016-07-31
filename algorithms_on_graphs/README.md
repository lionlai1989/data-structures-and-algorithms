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
**note**: Using iteration is not bad, but it can not record pre(vertex) and post(vertex). I choose to use recursion.
```c++
bfs(G)
{
  list L = empty
  tree T = empty
  choose a starting vertex x
  search(x)
  while(L nonempty)
    remove edge (v,w) from start of L
    if w not yet visited
    {
      add (v,w) to T
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
![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    D -> E;
    S -> D;
    E -> S;
    S -> A;
    A -> B;
    S -> C;
    C -> B,
  }
)<br>
##Distance
The distance between two vertices is the length of the shortest path between.<br>
