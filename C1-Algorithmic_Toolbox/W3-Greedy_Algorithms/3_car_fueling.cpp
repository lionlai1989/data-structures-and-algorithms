#include <iostream> // cin, cout
#include <vector>   // vector

using namespace std;

int compute_min_refills(int dist, int tank, vector<int> &stops) {
    // The end line is the last stops.
    stops.push_back(dist);

    int n_refill = 0;
    int curr_pos = 0;
    int curr_fuel = tank;

    for (int i = 0; i < stops.size(); ++i) {
        // Next stop is too far away.
        if (curr_pos + tank < stops[i]) {
            return -1;
        }

        // Refill the tank to reach the next stop.
        if (curr_pos + curr_fuel < stops[i]) {
            n_refill += 1;
            curr_fuel = tank;
        }

        // Consume fuel to reach the next stop
        curr_fuel -= (stops[i] - curr_pos);
        // move to the next stop.
        curr_pos = stops[i];
    }

    return n_refill;
}

// g++ 3_car_fueling.cpp -std=c++17 -Wall && ./a.out < 3_car_fueling.txt
int main() {
    int d, m, n;
    while (cin >> d >> m >> n) {
        vector<int> stops(n);
        for (int i = 0; i < n; ++i) {
            cin >> stops[i];
        }
        cout << compute_min_refills(d, m, stops) << "\n";
    }

    return 0;
}
