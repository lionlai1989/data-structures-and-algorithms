#include <algorithm> // sort, reverse
#include <iostream>  // cin, cout
#include <numeric>   // accumulate
#include <string>    // string
#include <vector>    // vector

using namespace std;

bool cmp(const string &a, const string &b) {
    // 2, 21
    // 221 > 212
    return a + b > b + a;
}

string largest_concatenate(vector<string> &a) {
    sort(a.begin(), a.end(), cmp);
    string result = accumulate(a.begin(), a.end(), string{});

    return result;
}

// g++ 7_largest_concatenate.cpp -std=c++17 -Wall && ./a.out < 7_largest_concatenate.txt
int main() {
    int n;
    while (cin >> n) {
        vector<string> a(n);
        for (int i = 0; i < a.size(); ++i) {
            cin >> a[i];
        }
        cout << largest_concatenate(a) << endl;
    }
}
