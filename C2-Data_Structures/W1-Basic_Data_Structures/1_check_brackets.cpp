#include <iostream> // cin, cout
#include <stack>    // stack
#include <string>   // string
#include <tuple>    // tuple

using namespace std;

bool left_bracket(char c) {
    if (c == '[' || c == '(' || c == '{') {
        return true;
    }
    return false;
}

bool right_bracket(char c) {
    if (c == ']' || c == ')' || c == '}') {
        return true;
    }
    return false;
}

bool is_pair(char c1, char c2) {
    if ((c1 == '[' && c2 == ']') || (c1 == '(' && c2 == ')') || (c1 == '{' && c2 == '}')) {
        return true;
    }
    return false;
}

int check_brackets(const string &text) {
    stack<tuple<char, int>> st;

    for (size_t i = 0; i < text.size(); ++i) {
        char c = text[i];

        if (left_bracket(c)) {
            st.push(make_tuple(c, i));
        } else if (right_bracket(c)) {
            auto [top_c, top_i] = st.top();

            if (is_pair(top_c, c)) {
                st.pop();
            } else {
                return i + 1; // 1-based index
            }
        }
    }

    if (!st.empty()) {
        auto [top_c, top_i] = st.top();
        return top_i + 1;
    }

    return 0;
}

// g++ 1_check_brackets.cpp -std=c++17 -Wall && ./a.out < 1_check_brackets.txt
int main() {
    string s;
    while (cin >> s) {
        int ret = check_brackets(s);
        if (ret == 0) {
            cout << "Success" << endl;
        } else {
            cout << ret << endl;
        }
    }

    return 0;
}
