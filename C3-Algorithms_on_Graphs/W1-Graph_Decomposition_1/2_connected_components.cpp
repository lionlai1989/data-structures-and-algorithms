#include <iostream>
#include <vector>

using namespace std;

int number_of_components(vector<vector<int>> &adj) {}

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
    }
}
