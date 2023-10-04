#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

long long MaxPairwiseProduct(const vector<int> &numbers) {
    long long max_product = 0;
    int n = numbers.size();

    // Init
    int idx1 = -1, idx2 = -1;

    for (int i = 0; i < n; ++i) {
        if (idx1 == -1 || numbers[idx1] < numbers[i]) {
            idx1 = i;
        }
    }
    for (int i = 0; i < n; ++i) {
        if (idx1 != i && (idx2 == -1 || numbers[idx2] < numbers[i])) {
            idx2 = i;
        }
    }

    // NOTE: `numbers[idx1] * numbers[idx2]` returns an integer even `max_product` is
    // the type of `long long`. To avoid this, I must explicitly convert one `int` to
    // `long long` before multiplication.
    // https://stackoverflow.com/q/49067649/2641038
    max_product = (long long)numbers[idx1] * numbers[idx2];
    return max_product;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
