#Decomposition of Graphs
runtimes of vertices: |V|<br>
runtimes of edges: |E|<br>
Density: how many of edges you have in terms of the number of vertices.<br>
Dense Grapsh: a large fraction of pairs of vertices are connected by edges |E| ~ |V|^2.<br>
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
We want to explore every edge leaving vertex we have found. In Depth First Order(DFS)

make DFS useful by storing data:<br>
clock: store the number of visits, clock ticks at every pre/post visit.<br>
![Alt text](http://g.gravizo.com/g?
  digraph G {
    edge [dir=none];
    "1/8"->v;
    A -> C;
    A -> D;
    C -> D;
  }
)<br>
lemma:<br>
[pre(u), post(u)], [pre(v), post(v)] are either nested or disjoint.<br>







![Alt text](http://g.gravizo.com/g?
  digraph G {
    aize ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf};
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
)
