#include <iostream> // cin, cout
#include <limits>   // numeric_limits
#include <vector>   // vector

using namespace std;

// space: O(1)
// time: O(n)
long long MaxPairwiseProduct(const vector<int> &numbers) {
    int largest = numbers[0];
    int second = numeric_limits<int>::min();

    for (int i = 1; i < numbers.size(); i++) {
        if (numbers[i] >= largest) {
            second = largest;
            largest = numbers[i];
        } else if (numbers[i] < largest && numbers[i] > second) {
            second = numbers[i];
        }
    }
    return (long long)largest * second;
}

// g++ 2_maximum_pairwise_product.cpp -std=c++17 -Wall && ./a.out < 2_maximum_pairwise_product.txt
int main() {
    int n;
    // Read test cases until end of file
    while (cin >> n) {
        vector<int> numbers(n);
        for (int i = 0; i < n; ++i) {
            cin >> numbers[i];
        }
        cout << MaxPairwiseProduct(numbers) << "\n";
    }
    return 0;
}
