#include <iostream>
#include <vector>

using namespace std;

struct Vertex {
    int key;
    vector<int> adj_keys;
    int previsit = 0;
    int postvisit = 0;
    int group = 0;

    Vertex(int k, const vector<int> &adj) : key(k), adj_keys(adj) {}
};

struct Graph {
    int clock;
    int n_group;
    vector<Vertex> vertices;

    Graph(const vector<vector<int>> &adj) : clock(0), n_group(0) {
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

        for (Vertex &v : vertices) {
            if (v.previsit == 0) {
                // Update group ID only when starting a new DFS.
                n_group += 1;
                dfs(v, n_group);
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

        for (int nbr_key : v.adj_keys) {
            dfs(vertices[nbr_key], group);
        }

        postvisit(v);
    }

    bool reach(int start, int end) const { return vertices[start].group == vertices[end].group; }
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
