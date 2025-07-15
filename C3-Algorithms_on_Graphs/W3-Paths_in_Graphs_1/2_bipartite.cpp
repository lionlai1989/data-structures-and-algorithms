#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int bipartite(vector<vector<int>> &adjacency_list) {
    int n_vertices = adjacency_list.size();

    // +1: white
    // -1: black
    //  0: uncolored
    vector<int> colors(n_vertices, 0);
    vector<bool> visited(n_vertices, false);

    for (int start = 0; start < n_vertices; ++start) {
        // There could be different connected componenets.
        if (visited[start]) {
            continue;
        }

        queue<int> q;

        colors[start] = 1; // set to white
        visited[start] = true;
        q.push(start);

        while (!q.empty()) {
            int n_ele = q.size();

            for (int i = 0; i < n_ele; ++i) {
                int node = q.front();
                q.pop();

                int curr_color = colors[node];

                for (auto nbr : adjacency_list[node]) {
                    if (!visited[nbr]) { // not visited
                        colors[nbr] = curr_color * -1;
                        visited[nbr] = true;
                        q.push(nbr);
                    } else { // already visited
                        if (curr_color == colors[nbr]) {
                            return 0;
                        }
                    }
                }
            }
        }
    }

    return 1;
}

// g++ 2_bipartite.cpp -std=c++17 -Wall && ./a.out < 2_bipartite.txt
int main() {
    int n_vertices, m_edges;

    while (cin >> n_vertices >> m_edges) {
        vector<vector<int>> adjacency_list(n_vertices);
        int u, v;

        for (int i = 0; i < m_edges; ++i) {
            cin >> u >> v;
            u -= 1;
            v -= 1;
            adjacency_list[u].push_back(v);
            adjacency_list[v].push_back(u);
        }
        cout << bipartite(adjacency_list) << endl;
    }

    return 0;
}
