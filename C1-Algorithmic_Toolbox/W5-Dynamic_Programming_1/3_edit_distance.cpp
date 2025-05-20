#include <algorithm> // min
#include <iostream>  // cin, cout
#include <string>    // string
#include <vector>    // vector

using namespace std;

int edit_distance(const string &str1, const string &str2) {
    int m = str1.size();
    int n = str2.size();

    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0)); // (i: m+1, j: n+1)
    for (int i = 0; i <= m; ++i) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= n; ++j) {
        dp[0][j] = j;
    }

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {

            if (str1[i - 1] == str2[j - 1]) { // match
                dp[i][j] = dp[i - 1][j - 1];
            } else { // mismatch
                dp[i][j] = min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]}) + 1;
            }
        }
    }
    return dp[m][n];
}

// g++ 3_edit_distance.cpp -std=c++17 -Wall && ./a.out < 3_edit_distance.txt
int main() {
    string str1;
    string str2;
    while (cin >> str1 >> str2) {
        cout << edit_distance(str1, str2) << endl;
    }
    return 0;
}
