#include <iostream>
#include <vector>

using namespace std;

struct Vertex {
    int key;
    vector<int> adj_keys;
    int previsit;
    int postvisit;
    int group;

    Vertex(int k, const vector<int> &ak, int pre = 0, int post = 0, int g = 0)
        : key(k), adj_keys(ak), previsit(pre), postvisit(post), group(g) {}
};

struct Graph {
    int clock;
    vector<Vertex> vertices;

    Graph(const vector<vector<int>> &adj) {
        clock = 0;
        for (size_t i = 0; i < adj.size(); ++i) {
            /**
             * push_back(Vertex(...)) first constructs a temporary Vertex object, then invokes either the copy- or
             * move-constructor to place it into the vector’s storage. That’s two constructor calls (one for the
             * temporary, one for the in-vector object), plus the move (or copy) itself. With push_back, even if the
             * compiler can elide some copies, you’re still conceptually creating an extra object and then moving it.
             */
            // vertices.push_back(Vertex(i, adj[i]));

            /**
             * emplace_back(...) forwards your constructor arguments directly into the vector’s uninitialized memory,
             * running just one constructor call “in-place.” With emplace_back, there’s no move or copy at all—your
             * Vertex(int, const vector<int>&) runs exactly where it needs to.
             */
            vertices.emplace_back(i, adj[i]);
        }

        int group = 1; // goup idx starting from 1.

        for (Vertex &v : vertices) {
            if (v.previsit == 0) {
                dfs(v, group);

                // Update group ID only when starting a new DFS.
                group += 1;
            }
        }
    }

    ~Graph() = default;

    void previsit(Vertex &v) {
        clock += 1;
        v.previsit = clock;
    }

    void postvisit(Vertex &v) {
        clock += 1;
        v.postvisit = clock;
    }

    void dfs(Vertex &v, int group) {
        if (v.previsit != 0) { // already visited?
            return;
        }

        previsit(v);
        v.group = group;

        for (size_t nbr : v.adj_keys) {
            dfs(vertices[nbr], group);
        }

        postvisit(v);
    }

    bool reach(int start, int end) { return vertices[start].group == vertices[end].group; }
};

// g++ 1_reachability.cpp -std=c++17 -Wall && ./a.out < 1_reachability.txt
int main() {
    int n_vertices, m_edges;
    while (cin >> n_vertices >> m_edges) {
        // Use adjacency list to represent an undirected graph
        vector<vector<int>> adjacency_list(n_vertices);

        int u, v;
        for (int i = 0; i < m_edges; ++i) {
            cin >> u >> v;
            // zero-based indexing
            adjacency_list[u - 1].push_back(v - 1);
            adjacency_list[v - 1].push_back(u - 1);
        }

        // Construct graph. The advantage of constructing a graph first is that the DFS only run once and we can use
        // the constructed graph to check reachability in O(1).
        Graph g(adjacency_list);

        int start, end;
        cin >> start >> end;

        cout << g.reach(start - 1, end - 1) << endl; // O(1)
    }
}
