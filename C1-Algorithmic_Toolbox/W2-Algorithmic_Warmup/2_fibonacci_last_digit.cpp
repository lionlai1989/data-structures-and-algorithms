#include <iostream> // cin, cout

using namespace std;

int fibonacci_last_digit(int n) {
    if (n <= 1) {
        return n;
    }
    int n0 = 0;
    int n1 = 1;

    for (int i = 2; i <= n; ++i) {
        int tmp = (n0 + n1) % 10;
        n0 = n1;
        n1 = tmp;
    }

    return n1;
}

// g++ 2_fibonacci_last_digit.cpp -std=c++17 -Wall && ./a.out < 2_fibonacci_last_digit.txt
int main() {
    int n;
    while (cin >> n) {
        cout << fibonacci_last_digit(n) << '\n';
    }
    return 0;
}
