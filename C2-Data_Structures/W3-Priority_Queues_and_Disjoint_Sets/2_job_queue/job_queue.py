# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(n_workers, jobs):
    # Naive solution:
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def parent(i):
    return int(i / 2)

def left_child(i):
    return 2 * i

def right_child(i):
    return 2 * i + 1

class BinaryMinHeap:
    def __init__(self, data):
        """BinaryMinHeap is 1-based array which is easier to implement because the lecturer
        also uses it.
        """
        self.size = len(data)
        data.insert(0, 0)
        self.data = data

    def sift_down(self, i):
        min_index = i
        left = left_child(i)
        if left <= self.size and self.data[left] < self.data[min_index]:
            min_index = left
        right = right_child(i)
        if right <= self.size and self.data[right] < self.data[min_index]:
            min_index = right
        if i != min_index:
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            
            self.sift_down(min_index)

    def sift_up(self, i):
        while i > 1 and self.data[parent(i)] > self.data[i]:
            self.data[i], self.data[parent(i)] = self.data[parent(i)], self.data[i]
            i = parent(i)

    def insert(self, p):
        self.size += 1
        self.data[self.size] = p
        self.sift_up(self.size)

    def extract_min(self):
        result = self.data[1]
        self.data[1] = self.data[self.size]
        self.size -= 1
        self.sift_down(1)
        return result

    def build_min_heap(self):
        start = int(self.size / 2)
        for i in range(start, 0, -1): # start, start-1, ..., 1
            self.sift_down(i)

class Worker:
    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time

def assign_jobs_faster(n_workers, jobs):
    # Faster solution:
    result = []
    
    # Build a binary min-heap which has minimum value on the top of the tree.
    # This heap consists of Worker(), which has `thread_id` and `release_time`.
    bin_min_heap = BinaryMinHeap([Worker(i) for i in range(n_workers)])
    bin_min_heap.build_min_heap()

    # The idea is always pop the elements on top of this binary min-heap because
    # it has minimum `release_time`.

    for job in jobs:
        # The `worker` with minimum release_time is pop out and takes the `job`.
        worker = bin_min_heap.extract_min()

        result.append(AssignedJob(worker.thread_id, worker.release_time))

        # The release time is updated.
        worker.release_time += job

        # Push `worker` back with updated released time.
        bin_min_heap.insert(worker)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs_faster(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    # Use the following as input:
    # 2 5
    # 1 2 3 4 5
    #
    # Output:
    # 0 0
    # 1 0
    # 0 1
    # 1 2
    # 0 4
    main()
