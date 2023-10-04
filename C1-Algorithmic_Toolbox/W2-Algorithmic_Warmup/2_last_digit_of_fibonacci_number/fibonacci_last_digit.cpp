#include <iostream>

using namespace std;

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1) return n;

    int previous = 0;
    int current = 1;
    int res = 0;

    for (int i = 2; i <= n; ++i) {
        res = previous + current;
        previous = current;
        current = res;
    }

    return current % 10;
}

int get_fibonacci_last_digit_fast(int n) {
    if (n <= 1) return n;

    int previous = 0;
    int current = 1;
    int res = 0;

    for (int i = 2; i <= n; ++i) {
        res = (previous + current) % 10;
        previous = current;
        current = res;
    }

    return current % 10;
}

// g++ -pipe -O2 -std=c++14 fibonacci_last_digit.cpp -lm && ./a.out
int main() {
    int n;
    cin >> n;
    int c = get_fibonacci_last_digit_fast(n);
    cout << c << '\n';
}
