#include <algorithm> // max
#include <iostream>  // cin, cout
#include <vector>    // vector

using namespace std;

struct TreeNode {
  public:
    vector<TreeNode *> children;

    TreeNode() = default;
};

int tree_height(TreeNode *root) {
    int max_height = 0;

    for (auto &child : root->children) {
        max_height = max(tree_height(child), max_height);
    }

    return max_height + 1; // count the current node
}

// g++ 2_tree_height.cpp -std=c++17 -Wall && ./a.out < 2_tree_height.txt
int main() {
    int n;
    while (cin >> n) {
        TreeNode *root = nullptr;

        vector<TreeNode> tree(n);

        int idx;
        for (int i = 0; i < n; ++i) {
            cin >> idx;
            if (idx == -1) {
                root = &tree[i];
            } else {
                // i: child, idx: parent
                tree[idx].children.push_back(&tree[i]);
            }
        }
        cout << tree_height(root) << endl;
    }

    return 0;
}
