#include <algorithm> // sort
#include <iostream>  // cin, cout
#include <vector>    // vector

using namespace std;

struct Item {
    int value;
    int weight;
    double value_per_weight() const { return static_cast<double>(value) / weight; }
};

double get_optimal_value(int capacity, vector<Item> &items) {
    // items cannot be const because it will be sorted.
    // Sort items in descending order
    // Take items with the highest value-to-weight ratio first.
    sort(items.begin(), items.end(),
         [&](const Item &a, const Item &b) { return a.value_per_weight() > b.value_per_weight(); });

    double total = 0.0;

    for (auto item : items) {
        if (capacity == 0) {
            break;
        }

        // Greedy strategy: if you can take a whole item, do so; otherwise, take
        // a fraction.
        int w = min({item.weight, capacity});
        capacity -= w;
        total += w * item.value_per_weight();
    }
    return total;
}

// g++ 2_maximum_value_of_the_loot.cpp -std=c++17 -Wall && ./a.out < 2_maximum_value_of_the_loot.txt
int main() {
    int n;
    int capacity;
    cout.precision(10);

    while (cin >> n >> capacity) {
        vector<Item> items(n);
        for (int i = 0; i < n; i++) {
            cin >> items[i].value >> items[i].weight;
        }
        double optimal_value = get_optimal_value(capacity, items);
        cout << optimal_value << endl;
    }

    return 0;
}
