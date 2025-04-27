#include <algorithm> // sort
#include <iostream>  // cin, cout
#include <vector>    // vector

using namespace std;

// space: O(1)
// time: O( n*log(n) )
long long max_dot_product(vector<int> &a, vector<int> &b) {
    sort(a.begin(), a.end(), [&](int i, int j) { return i > j; });
    sort(b.begin(), b.end(), [&](int i, int j) { return i > j; });

    long long val = 0;

    for (int i = 0; i < a.size(); ++i) {
        val += (a[i] * b[i]);
    }
    return val;
}

// g++ 4_maximum_dot_product.cpp -std=c++17 -Wall && ./a.out < 4_maximum_dot_product.txt
int main() {
    int n;
    while (cin >> n) {
        vector<int> a(n), b(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> b[i];
        }
        cout << max_dot_product(a, b) << endl;
    }
}
