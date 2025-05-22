#include <iostream> // cin, cout
#include <vector>   // vector

using namespace std;

// space:
// time:
int max_gold(int capacity, const vector<int> &weights) {}

// g++ 1_knapsack_max_gold.cpp -std=c++17 -Wall && ./a.out < 1_knapsack_max_gold.txt
int main() {
    int n_bars, capacity;
    while (cin >> capacity >> n_bars) {
        vector<int> weights(n_bars);
        for (int i = 0; i < n_bars; ++i) {
            cin >> weights[i];
        }
        cout << max_gold(capacity, weights) << '\n';
    }
}
