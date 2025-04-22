#include <cassert>  // assert
#include <iostream> // cin, cout

using namespace std;

int fibonacci_naive(int n) {
    if (n <= 1)
        return n;
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
}

int fibonacci(int n) {
    // n = 0, 1, 2, 3, 4
    //     0, 1, 1, 2, 3
    //    n0 n1
    if (n <= 1) {
        return n;
    }
    int n0 = 0;
    int n1 = 1;
    for (int i = 2; i <= n; ++i) {
        int tmp = n0 + n1;
        n0 = n1;
        n1 = tmp;
    }
    return n1;
}

// g++ 1_fibonacci.cpp -std=c++17 -Wall && ./a.out < 1_fibonacci.txt
int main() {
    int n;
    while (cin >> n) {
        cout << fibonacci(n) << '\n';
        assert(fibonacci(n) == fibonacci_naive(n));
    }
    return 0;
}
