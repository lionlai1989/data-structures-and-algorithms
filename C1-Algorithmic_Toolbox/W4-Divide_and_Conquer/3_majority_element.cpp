#include <iostream> // cin, cout
#include <vector>   // vector

using namespace std;

// Time: O(n), Space: O(1)
bool majority_element(const vector<int> &nums) {
    int count = 0;
    int candidate = 0;

    // First pass: find candidate
    for (int num : nums) {
        if (count == 0) {
            candidate = num;
            count = 1;
        } else if (num == candidate) {
            count += 1;
        } else {
            count -= 1;
        }
    }

    // Second pass: verify
    count = 0;
    for (int num : nums) {
        if (num == candidate) {
            count += 1;
        }
    }

    return count > nums.size() / 2;
}

// g++ 3_majority_element.cpp -std=c++17 -Wall && ./a.out < 3_majority_element.txt
int main() {
    int n;
    while (cin >> n) {
        vector<int> a(n);
        for (size_t i = 0; i < a.size(); ++i) {
            cin >> a[i];
        }
        cout << majority_element(a) << '\n';
    }
}
