#include <algorithm> // sort
#include <iostream>  // cin, cout
#include <vector>    // vector

using namespace std;

struct Segment {
    int start;
    int end;
};

// space: O(n)
// time: O(n)
vector<int> optimal_points(vector<Segment> &segments) {
    sort(segments.begin(), segments.end(), [&](const Segment &a, const Segment &b) { return a.end < b.end; });

    vector<int> bars;

    int bar = segments[0].end; // init
    bars.push_back(bar);
    for (int i = 1; i < segments.size(); ++i) {
        if (bar >= segments[i].start) {
            // Intersect. Do nothing.
        } else { // update bar
            bar = segments[i].end;
            bars.push_back(bar);
        }
    }
    return bars;
}

// g++ 5_covering_segments.cpp -std=c++17 -Wall && ./a.out < 5_covering_segments.txt
int main() {
    int n;
    while (cin >> n) {
        vector<Segment> segments(n);
        for (int i = 0; i < segments.size(); ++i) {
            cin >> segments[i].start >> segments[i].end;
        }
        vector<int> points = optimal_points(segments);
        cout << points.size() << "\n";
        for (int i = 0; i < points.size(); ++i) {
            cout << points[i] << " ";
        }
        cout << endl;
    }
}
