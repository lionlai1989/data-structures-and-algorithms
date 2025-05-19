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

int fibonacci_sum_squares_last_digit(long long n) {
    if (n <= 1) {
        return n;
    }
    /**
     * Hint:
     * f(1)^2 + f(2)^2 + f(3)^2 + f(4)^2 + f(5)^2 = f(5) * f(6)
     */
    int f_n = fibonacci_huge_fast(n, 10);
    int f_n1 = fibonacci_huge_fast(n + 1, 10);
    return f_n * f_n1 % 10;
}

// g++ 6_fibonacci_sum_squares_last_digit.cpp -std=c++17 -Wall && ./a.out < 6_fibonacci_sum_squares_last_digit.txt
int main() {
    long long n = 0;
    while (cin >> n) {
        std::cout << fibonacci_sum_squares_last_digit(n) << std::endl;
    }
    return 0;
}
