#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Heap {
  private:
    vector<int> data;

  public:
    Heap(const vector<int> &data) : data(std::move(data)) {}
};

// g++ 1_build_heap.cpp -std=c++17 -Wall && ./a.out < 1_build_heap.txt
int main() {
    int n;
    while (cin >> n) {
        vector<int> v(n);
        for (int i = 0; i < n; ++i) {
            cin >> v[i];
        }
        Heap h(v);
    }
    return 0;
}
