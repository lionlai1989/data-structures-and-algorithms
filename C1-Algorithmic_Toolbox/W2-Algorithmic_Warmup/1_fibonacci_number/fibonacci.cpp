#include <cassert>
#include <iostream>

using namespace std;

int fibonacci_naive(int n) {
    if (n <= 1) return n;
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
}

int fibonacci_fast(int n) {
    if (n <= 1) return n;

    int prev1 = 1, prev2 = 0, curr = 0;
    for (int i = 2; i < n + 1; ++i) {
        curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }

    return curr;
}

void test_solution() {
    assert(fibonacci_fast(3) == 2);
    assert(fibonacci_fast(10) == 55);
    for (int n = 0; n < 20; ++n) {
        assert(fibonacci_fast(n) == fibonacci_naive(n));
    }
}

// g++ -pipe -O2 -std=c++14 fibonacci.cpp -lm && ./a.out
int main() {
    int n = 0;
    cin >> n;
    // cout << fibonacci_naive(n) << '\n';
    // test_solution();
    cout << fibonacci_fast(n) << '\n';
    return 0;
}
