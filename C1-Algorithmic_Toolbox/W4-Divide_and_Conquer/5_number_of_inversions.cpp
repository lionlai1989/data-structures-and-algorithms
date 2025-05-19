#include <iostream> // cin, cout
#include <vector>   // vector

using namespace std;

long long number_of_inversions(const vector<int> &a) { return 0; }

// g++ 5_number_of_inversions.cpp -std=c++17 -Wall && ./a.out < 5_number_of_inversions.txt
int main() {
    int n;
    while (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < a.size(); ++i) {
            cin >> a[i];
        }
        cout << number_of_inversions(a) << '\n';
    }
}
