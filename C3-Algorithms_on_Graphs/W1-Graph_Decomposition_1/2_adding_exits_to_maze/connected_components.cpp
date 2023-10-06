#include <iostream>
#include <vector>

using namespace std;

struct Graph {
    int clock;

    Graph() : clock(0) {}
};

class Vertex {
  public:
    int key;
    vector<int> adj_keys;
    int previsit;
    int postvisit;
    int group;

    Vertex(int _key, const vector<int>& _adj_keys, int _previsit = 0,
           int _postvisit = 0, int _group = 0)
        : key(_key),
          adj_keys(_adj_keys),
          previsit(_previsit),
          postvisit(_postvisit),
          group(_group) {}
};

void previsit(Vertex& v, Graph& g) {
    g.clock += 1;
    v.previsit = g.clock;
}

void postvisit(Vertex& v, Graph& g) {
    g.clock += 1;
    v.postvisit = g.clock;
}

void depth_first_search(vector<Vertex>& vertices, size_t idx, Graph& graph, int group) {
    previsit(vertices[idx], graph);
    vertices[idx].group = group;

    for (size_t i = 0; i < vertices[idx].adj_keys.size(); ++i) {
        auto adj_key = vertices[idx].adj_keys[i];
        if (vertices[adj_key].previsit == 0) {
            depth_first_search(vertices, adj_key, graph, group);
        }
    }
    postvisit(vertices[idx], graph);
}

int number_of_components(vector<vector<int> >& adj) {
    Graph graph;
    int previsit = 0;
    int postvisit = 0;
    int group = 0;  // group == 1 means there is 1 connected components.
    vector<Vertex> vertices;

    for (size_t i = 0; i < adj.size(); ++i) {
        vertices.push_back(Vertex(i, adj[i]));
    }

    for (size_t i = 0; i < vertices.size(); ++i) {
        if (vertices[i].previsit == 0) {
            group += 1;
            depth_first_search(vertices, i, graph, group);
        }
    }

    return group;
}

// g++ -pipe -O2 -std=c++14 connected_components.cpp -lm && ./a.out
int main() {
    size_t n, m;
    cin >> n >> m;
    vector<vector<int> > adj(n, vector<int>());
    for (size_t i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        adj[x - 1].push_back(y - 1);
        adj[y - 1].push_back(x - 1);
    }
    cout << number_of_components(adj);
}
