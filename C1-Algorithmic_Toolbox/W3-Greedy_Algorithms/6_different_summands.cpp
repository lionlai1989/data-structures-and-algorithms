#include <iostream> // cin, cout
#include <vector>   // vector

using namespace std;

// space: O( sqrt(n) )
// time: O( sqrt(n) )
vector<int> optimal_summands(int n) {
    vector<int> summands;

    int i = 1; // positive integer
    while (n != 0) {
        if (n - i >= i + 1) {
            summands.push_back(i);
            n -= i;
        } else {
            summands.push_back(n);
            break;
        }
        i += 1;
    }
    return summands;
}

// g++ 6_different_summands.cpp -std=c++17 -Wall && ./a.out < 6_different_summands.txt
int main() {
    int n;
    while (cin >> n) {
        vector<int> summands = optimal_summands(n);
        cout << summands.size() << '\n';
        for (int i = 0; i < summands.size(); ++i) {
            cout << summands[i] << ' ';
        }
        cout << endl;
    }
    return 0;
}
