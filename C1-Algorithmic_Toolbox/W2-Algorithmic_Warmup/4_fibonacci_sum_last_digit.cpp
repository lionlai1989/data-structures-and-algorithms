#include <cassert>  // assert
#include <iostream> // cin, cout

using namespace std;

int pisano_period(int n) {
    /**
     * The Pisano period is defined as the length of the repeating cycle in the
     * sequence of Fibonacci numbers modulo n. Thus, the possible modulo number
     * is from 0 to n-1. If the Fibonacci sequence modulo n repeats the pattern
     * 0, 1, it indicates the cycle has restarted.
     */
    int f0 = 0;
    int f1 = 1;
    // Explain why n*n.
    // Each mod n could result to 0, 1, 2, ... , n-1
    // If try n^2 + 1 times, it guarantees to generate (0, 1) pair.
    for (int i = 2; i <= n * n; ++i) {
        int tmp = f1;
        f1 = (f1 + f0) % n;
        f0 = tmp;

        if (f0 == 0 && f1 == 1) {
            return i - 1;
        }
    }
    assert(false);
}

int fibonacci_sum_last_digit(long long n) {
    if (n <= 1)
        return n;

    // Use mod 10 to get last digit
    int period = pisano_period(10);
    assert(period == 60);

    // f(0) + f(1) + f(2) + ... + f(n) = f(n+2) - 1
    int remainder = (n + 2) % period;
    if (remainder <= 1) {
        return remainder;
    }

    int f0 = 0;
    int f1 = 1;
    for (long long i = 2; i <= remainder; ++i) {
        int tmp = f0;
        f0 = f1;
        f1 = (tmp + f1) % 10;
    }

    // f1 is the current target
    // To avoid negative result
    return (f1 + 10 - 1) % 10;
}

// g++ 4_fibonacci_sum_last_digit.cpp -std=c++17 -Wall && ./a.out < 4_fibonacci_sum_last_digit.txt
int main() {
    long long n = 0;
    while (cin >> n) {
        cout << fibonacci_sum_last_digit(n) << endl;
    }
    return 0;
}
