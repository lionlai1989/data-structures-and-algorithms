#include <iostream> // cout, cin

using namespace std;

int sum_of_two_digits(int a, int b) { return a + b; }

// g++ 1_sum_of_two_digits.cpp -std=c++17 -Wall && ./a.out < 1_sum_of_two_digits.txt
int main() {
    int a = 0;
    int b = 0;
    while (cin >> a >> b) {
        cout << sum_of_two_digits(a, b) << endl;
    }
    return 0;
}
