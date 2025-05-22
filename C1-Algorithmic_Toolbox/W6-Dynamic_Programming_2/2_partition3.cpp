#include <iostream> // cin, cout
#include <numeric>  // accumulate
#include <vector>   // vector

using namespace std;

int partition3(const vector<int> &values) {
    int n = values.size();
    int sum = accumulate(values.begin(), values.end(), 0);

    // If total sum is not divisible by 3, can't partition
    if (sum % 3 != 0)
        return 0;

    int target = sum / 3;
}

int main() {
    int n;
    while (cin >> n) {
        vector<int> v(n);
        for (size_t i = 0; i < v.size(); ++i) {
            cin >> v[i];
        }
        cout << partition3(v) << '\n';
    }
}
