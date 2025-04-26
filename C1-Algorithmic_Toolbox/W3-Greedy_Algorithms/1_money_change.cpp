#include <iostream> // cin, cout

using namespace std;

int get_change(int m) {
    int n_tens = 0;
    int n_fives = 0;
    int n_ones = 0;
    // dividend / divisor = quotient
    // numerator / denominator = remainder
    n_tens = m / 10;
    n_fives = m % 10 / 5;
    n_ones = m % 10 % 5;
    return n_tens + n_fives + n_ones;
}

// g++ 1_money_change.cpp -std=c++17 -Wall && ./a.out < 1_money_change.txt
int main() {
    int m;
    while (cin >> m) {
        std::cout << get_change(m) << '\n';
    }
    return 0;
}
