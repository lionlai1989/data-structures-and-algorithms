#include <cassert>  // assert
#include <iostream> // cin, cout

using namespace std;

long long fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long f0 = 0;
    long long f1 = 1;

    for (long long i = 2; i <= n; ++i) {
        long long tmp = f1;
        f1 = f0 + f1;
        f0 = tmp;
    }
    return f1 % m;
}

int pisano_period(int m) {
    /**
     * The Pisano period is defined as the length of the repeating cycle in the
     * sequence of Fibonacci numbers modulo n. Thus, the possible modulo number
     * is from 0 to n-1. If the Fibonacci sequence modulo n repeats the pattern
     * 0, 1, it indicates the cycle has restarted.
     */
    int f0 = 0;
    int f1 = 1;
    for (int i = 2; i <= m * m; ++i) {
        int tmp = f1;
        f1 = (f1 + f0) % m;
        f0 = tmp;

        if (f0 == 0 && f1 == 1) {
            return i - 1;
        }
    }
    assert(false);
}

long long fibonacci_huge_fast(long long n, int m) {
    int period = pisano_period(m);
    int remainder = n % period;
    if (remainder == 0 || remainder == 1) {
        return remainder;
    }

    int f0 = 0;
    int f1 = 1;
    // Calculate f(remainder)
    for (int i = 2; i <= remainder; ++i) {
        int tmp = f1;
        f1 = (f0 + f1) % m;
        f0 = tmp;
    }
    return f1 % m;
}

// g++ 5_fibonacci_huge.cpp -std=c++17 -Wall && ./a.out < 5_fibonacci_huge.txt
int main() {
    long long n;
    int m;
    while (cin >> n >> m) {
        cout << fibonacci_huge_naive(n, m) << '\n';
        assert(fibonacci_huge_fast(n, m) == fibonacci_huge_naive(n, m));
    }
    return 0;
}
