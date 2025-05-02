#include <iostream> // cin, cout
#include <vector>   // vector

using namespace std;

int binary_search(const vector<int> &a, int x) {
    // a is sorted
    int left = 0;
    int right = a.size() - 1;

    // use "<" or "<="?
    while (left < right) {
        // The infamous integer-overflow bug undetected for 20 years in C++.
        int mid = left + (right - left) / 2;

        if (a[mid] > x) {
            right = mid - 1;
        } else if (a[mid] < x) {
            left = mid + 1;
        } else { // found
            return mid;
        }
    }
    return -1;
}

// g++ 1_binary_search.cpp -std=c++17 -Wall && ./a.out < 1_binary_search.txt
int main() {
    int n, m;
    while (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        cin >> m;
        vector<int> b(m);
        for (int i = 0; i < m; ++i) {
            cin >> b[i];
        }
        for (int i = 0; i < m; ++i) {
            std::cout << binary_search(a, b[i]) << ' ';
        }
        cout << endl;
    }

    return 0;
}
