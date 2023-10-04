#include <iostream>

using namespace std;

long long lcm_naive(int a, int b) {
    for (long l = 1; l <= (long long)a * b; ++l)
        if (l % a == 0 && l % b == 0) return l;

    return (long long)a * b;
}

int greatest_common_divisor(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return greatest_common_divisor(b, a % b);
    }
}

long long lcm_fast(int a, int b) {
    auto gcd = greatest_common_divisor(a, b);
    return (long long)a * b / gcd;
}

// g++ -pipe -O2 -std=c++14 lcm.cpp -lm && ./a.out
int main() {
    int a, b;
    cin >> a >> b;
    cout << lcm_fast(a, b) << endl;
    return 0;
}
