#include <cassert>  // assert
#include <iostream> // cin, cout

using namespace std;

long long lcm_naive(int a, int b) {
    for (long long i = 1; i <= (long long)a * b; ++i) {
        if (i % a == 0 && i % b == 0) {
            return i;
        }
    }
    assert(false);
}

int gcd_iterative(int a, int b) {
    while (a % b != 0) {
        int tmp = a;
        a = b;
        b = tmp % b;
    }
    return b;
}

long long lcm_fast(int a, int b) {
    int gcd = gcd_iterative(a, b);
    return (long long)a * b / gcd;
}

// g++ 4_least_common_multiple.cpp -std=c++17 -Wall && ./a.out < 4_least_common_multiple.txt
int main() {
    int a, b;
    while (cin >> a >> b) {
        cout << lcm_fast(a, b) << ' ' << lcm_naive(a, b) << endl;
        assert(lcm_fast(a, b) == lcm_naive(a, b));
    }
    return 0;
}
