#include <algorithm> // min
#include <iostream>  // cin, cout
#include <vector>    // vector

using namespace std;

// space: O(n)
// time: O(n * coins)
int money_change_dp(int money, const vector<int> &coins, vector<int> &coin_seq) {
    const int UNREACHABLE = money + 1;
    vector<int> minimum_coins(money + 1, UNREACHABLE);
    minimum_coins[0] = 0;

    // Start from 1th element
    for (int i = 1; i <= money; ++i) {
        for (auto c : coins) {
            if (i >= c && minimum_coins[i - c] + 1 < minimum_coins[i]) {
                minimum_coins[i] = minimum_coins[i - c] + 1;
                coin_seq[i] = c;
            }
        }
    }

    if (minimum_coins[money] == UNREACHABLE)
        return -1;
    return minimum_coins[money];
}

// g++ 1_money_change_dp.cpp -std=c++17 -Wall && ./a.out < 1_money_change_dp.txt
int main() {
    vector<int> coins{1, 3, 4};
    int money;

    while (cin >> money) {
        vector<int> coin_seq(money + 1, -1);
        cout << money_change_dp(money, coins, coin_seq) << '\n';
        int idx = money;
        while (idx > 0) {
            cout << coin_seq[idx] << " ";
            idx -= coin_seq[idx];
        }
        cout << endl;
    }
}
