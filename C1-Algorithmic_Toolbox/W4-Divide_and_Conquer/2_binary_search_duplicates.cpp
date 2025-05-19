#include <iostream> // cin, cout
#include <vector>   // vector

using namespace std;

int binary_search_duplicates(const vector<int> &a, int x) {
    int left = 0;
    int right = a.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (a[mid] < x) {
            left = mid + 1;
        } else if (a[mid] > x) {
            right = mid - 1;
        } else if (a[mid] == x) {
            if (a[mid - 1] != x) {
                return mid;
            } else { // mid is NOT the first occurence of x
                right = mid - 1;
            }
        }
    }
    return -1;
}

// g++ 2_binary_search_duplicates.cpp -std=c++17 -Wall && ./a.out < 2_binary_search_duplicates.txt
int main() {
    int n, m;

    while (cin >> n) {
        vector<int> a(n, 0);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        cin >> m;
        for (int i = 0; i < m; ++i) {
            int b;
            cin >> b;
            cout << binary_search_duplicates(a, b) << " ";
        }
        cout << endl;
    }

    return 0;
}
