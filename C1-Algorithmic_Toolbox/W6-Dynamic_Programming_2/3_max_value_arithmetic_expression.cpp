#include <cassert>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

long long eval(long long a, long long b, char op) {
    if (op == '*') {
        return a * b;
    } else if (op == '+') {
        return a + b;
    } else if (op == '-') {
        return a - b;
    } else {
        assert(0);
    }
}

long long get_maximum_value(const string &exp) {
    // write your code here
    return 0;
}

// g++ 3_max_value_arithmetic_expression.cpp -std=c++17 -Wall && ./a.out < 3_max_value_arithmetic_expression.txt
int main() {
    string s;
    while (cin >> s) {
        cout << get_maximum_value(s) << '\n';
    }
    return 0;
}
