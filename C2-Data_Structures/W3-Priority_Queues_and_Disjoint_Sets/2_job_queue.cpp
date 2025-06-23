#include <iostream> // cout
#include <queue>    // priority_queue
#include <vector>   // vector

using namespace std;

struct Thread {
    int tid;
    long long next_free_time;

    Thread(int tid, long long time) : tid(tid), next_free_time(time) {}
};

struct Compare {
    bool operator()(const Thread &a, const Thread &b) {
        if (a.next_free_time == b.next_free_time) {
            return a.tid > b.tid; // smaller tid first
        }
        return a.next_free_time > b.next_free_time; // smaller time first
    }
};

void job_queue(int n, vector<int> &jobs) {

    priority_queue<Thread, vector<Thread>, Compare> pq;

    for (int i = 0; i < n; ++i) {
        pq.push(Thread(i, 0));
    }

    for (int time : jobs) {
        Thread t = pq.top();
        pq.pop();

        cout << t.tid << " " << t.next_free_time << endl;

        pq.push(Thread(t.tid, t.next_free_time + time));
    }
}

// g++ 2_job_queue.cpp -std=c++17 -Wall && ./a.out < 2_job_queue.txt
int main() {
    int n, m;
    while (cin >> n >> m) {
        vector<int> jobs(m);
        for (int i = 0; i < m; ++i) {
            cin >> jobs[i];
        }
        job_queue(n, jobs);

        cout << endl;
    }
    return 0;
}
