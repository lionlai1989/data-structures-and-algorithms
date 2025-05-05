#include <cassert>  // assert
#include <iostream> // cin, cout

using namespace std;

// space: O(1)
// time: O(min(a, b))
int gcd_brute_force(int a, int b) {
    int gcd = 1;

    for (int i = 1; i <= a && i <= b; ++i) {
        if (a % i == 0 && b % i == 0) {
            gcd = i;
        }
    }
    return gcd;
}

// space: O(log(max(a, b)))
// time: O(log(max(a, b)))
int gcd_recursive(int a, int b) {
    // It doesn't matter whether a or b is larger.
    if (b == 0) {
        return a;
    } else {
        return gcd_recursive(b, a % b);
    }
}

// space: O(1)
// time: O(log(max(a, b)))
int gcd_iterative(int a, int b) {
    while (a % b != 0) {
        int tmp = a;
        a = b;
        b = tmp % b;
    }
    return b;
}

// g++ 3_greatest_common_divisor.cpp -std=c++17 -Wall && ./a.out < 3_greatest_common_divisor.txt
int main() {
    int a, b;
    while (cin >> a >> b) {
        int i = gcd_iterative(a, b);
        int j = gcd_recursive(a, b);
        int k = gcd_brute_force(a, b);
        cout << i << " " << j << " " << k << endl;
        assert(i == j && j == k);
    }
    return 0;
}
