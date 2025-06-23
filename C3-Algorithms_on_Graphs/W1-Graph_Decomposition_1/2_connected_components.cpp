#include <iostream> // cout
#include <queue>    // queue
#include <vector>   // vector

using namespace std;

struct Vertex {
    int key;
    vector<int> adj_keys;
    int previsit = 0;
    int group = 0;

    Vertex(int k, const vector<int> &adj) : key(k), adj_keys(adj) {}
};

class Graph {
  public:
    Graph(const vector<vector<int>> &adj) : clock(0), n_group(0) {
        for (size_t i = 0; i < adj.size(); ++i) {
            vertices.emplace_back(i, adj[i]);
        }

        for (Vertex &v : vertices) {
            if (v.previsit == 0) {
                n_group += 1;
                bfs(v, n_group);
            }
        }
    }

    int connected_components() const { return n_group; }

  private:
    int clock;
    int n_group;
    vector<Vertex> vertices;

    void previsit(Vertex &v) {
        clock += 1;
        v.previsit = clock;
    }

    void bfs(Vertex &start, int group) {
        queue<Vertex *> q;
        previsit(start);
        start.group = group;
        q.push(&start);

        while (!q.empty()) {
            Vertex &current = *q.front();
            q.pop();

            for (int nbr_key : current.adj_keys) {
                Vertex &neighbor = vertices[nbr_key];
                if (neighbor.previsit == 0) {
                    previsit(neighbor);
                    neighbor.group = group;
                    q.push(&neighbor);
                }
            }
        }
    }
};

// g++ 2_connected_components.cpp -std=c++17 -Wall && ./a.out < 2_connected_components.txt
int main() {
    int n_vertices, m_edges;
    while (cin >> n_vertices >> m_edges) {
        vector<vector<int>> adjacency_list(n_vertices);

        for (int i = 0, u, v; i < m_edges; ++i) {
            cin >> u >> v;
            // Convert to 0-based index
            u -= 1;
            v -= 1;
            adjacency_list[u].push_back(v);
            adjacency_list[v].push_back(u);
        }

        Graph g(adjacency_list);
        cout << g.connected_components() << endl;
    }
}
