#include <iostream>

using namespace std;

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1) return n;

    long long previous = 0;
    long long current = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}

long long find_Pisano_period(long long m) {
    long long prev = 0, curr = 1, temp = 0;
    long long result = 0;
    for (int i = 0; i < m * m; ++i) {
        temp = curr;
        curr = (prev + curr) % m;
        prev = temp;
        if (prev == 0 && curr == 1) {
            result = i + 1;
        }
    }

    return result;
}

long long get_fibonacci_huge_fast(long long n, long long m) {
    long long pisano_period = find_Pisano_period(m);
    long long remainder = n % pisano_period;
    // cout << "pisano_period: " << pisano_period << endl;
    // cout << "remainder: " << remainder << endl;

    if (remainder <= 1) return remainder;

    long long prev = 0, curr = 1, temp = 0;
    for (long long i = 2; i < remainder + 1; ++i) {
        temp = curr;
        curr = (prev + curr) % m;
        prev = temp;
    }

    return curr % m;
}

// g++ -pipe -O2 -std=c++14 fibonacci_huge.cpp -lm && ./a.out
int main() {
    long long n, m;
    cin >> n >> m;
    cout << get_fibonacci_huge_fast(n, m) << '\n';
}
