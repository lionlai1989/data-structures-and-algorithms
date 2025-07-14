#include <iostream> // cin, cout
#include <queue>    // queue
#include <vector>   // vector

using namespace std;

int distance(const vector<vector<int>> &adjacency_list, int u, int v) {
    vector<bool> visited(adjacency_list.size(), false);

    queue<int> q;

    visited[u] = true;
    q.push(u);

    int dist = 0;

    while (!q.empty()) {
        int n_elem = q.size();

        for (int i = 0; i < n_elem; ++i) {
            int front = q.front();
            q.pop();

            if (front == v) {
                return dist;
            }

            for (auto nbr : adjacency_list[front]) {
                if (!visited[nbr]) {
                    visited[nbr] = true;
                    q.push(nbr);
                }
            }
        }

        dist += 1;
    }

    return -1;
}

// g++ 1_bfs.cpp -std=c++17 -Wall && ./a.out < 1_bfs.txt
int main() {
    int n_vertices, m_edges;

    while (cin >> n_vertices >> m_edges) {
        // Use default ctor for all elements.
        vector<vector<int>> adjacency_list(n_vertices);
        int u, v;

        // Contruct adjacency list
        for (int i = 0; i < m_edges; i++) {
            cin >> u >> v;
            u -= 1;
            v -= 1;
            adjacency_list[u].push_back(v);
            adjacency_list[v].push_back(u);
        }

        // Given two cities
        cin >> u >> v;
        u -= 1;
        v -= 1;

        cout << distance(adjacency_list, u, v) << endl;
    }

    return 0;
}
