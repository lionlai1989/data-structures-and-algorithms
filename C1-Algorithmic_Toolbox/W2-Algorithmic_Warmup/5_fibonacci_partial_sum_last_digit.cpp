#include <iostream> // cin, cout

using namespace std;

int pisano_period(int n) {
    int f0 = 0;
    int f1 = 1;
    for (int i = 2; i <= n * n; ++i) {
        int tmp = f1;
        f1 = (f1 + f0) % n;
        f0 = tmp;

        if (f0 == 0 && f1 == 1) {
            return i - 1;
        }
    }
    return -1; // code should not reach here.
}

int fibonacci_sum_last_digit(long long n) {
    if (n <= 1)
        return n;

    int period = pisano_period(10);

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

    return (f1 + 10 - 1) % 10;
}

long long fibonacci_partial_sum_last_digit(long long from, long long to) {
    int sum_to = fibonacci_sum_last_digit(to);
    int sum_from = from > 0 ? fibonacci_sum_last_digit(from - 1) : 0;

    if (sum_from <= sum_to) {
        return (sum_to - sum_from) % 10;
    } else {
        return (sum_to + 10 - sum_from) % 10;
    }
}

// g++ 5_fibonacci_partial_sum_last_digit.cpp -std=c++17 -Wall && ./a.out < 5_fibonacci_partial_sum_last_digit.txt
int main() {
    long long from, to;
    while (cin >> from >> to) {
        cout << fibonacci_partial_sum_last_digit(from, to) << '\n';
    }
}
