#include <iostream> // cout
#include <vector>   // vector

using namespace std;

struct Vertex {
    int key;
    vector<int> adj_keys;
    int previsit = 0;
    int postvisit = 0;
    int group = 0;

    Vertex(int k, const vector<int> &adj_keys) : key(k), adj_keys(adj_keys) {}
};

class Graph {
  private:
    int clock;
    int n_group;
    vector<Vertex> vertices;
    bool acyclic = true; // A graph without a cycle.

  public:
    Graph(const vector<vector<int>> &adjacency_list) : clock(0), n_group(0) {
        for (size_t i = 0; i < adjacency_list.size(); ++i) {
            vertices.emplace_back(i, adjacency_list[i]);
        }

        for (Vertex &v : vertices) {
            if (v.previsit == 0) {
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
        previsit(v);
        v.group = group;

        for (const int k : v.adj_keys) {
            if (vertices[k].previsit == 0) {
                dfs(vertices[k], group);
            } else if (vertices[k].postvisit == 0) {
                acyclic = false;
            }
        }

        postvisit(v);
    }

    bool is_acyclic() const { return acyclic; }
};

// g++ 1_acyclicity.cpp -std=c++17 -Wall && ./a.out < 1_acyclicity.txt
int main() {
    int n_vertices, m_edges;
    while (cin >> n_vertices >> m_edges) {
        // Use adjacency list to represent an directed graph
        vector<vector<int>> adjacency_list(n_vertices);

        int u, v;
        for (int i = 0; i < m_edges; ++i) {
            cin >> u >> v;
            u -= 1;
            v -= 1;
            adjacency_list[u].push_back(v);
        }

        Graph g(adjacency_list);
        cout << !g.is_acyclic() << endl;
    }
}
