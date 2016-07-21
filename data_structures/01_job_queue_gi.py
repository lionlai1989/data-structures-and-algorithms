# python3

import heapq


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


class JobQueue:
    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2 
    
    def sift_down(self, i):
        
        min_index = i
        n = self.num_workers
        l = 2*i+1
        r = 2*i+2
        
        if l <= n-1:
            if self.heap[l][1] < self.heap[min_index][1]:
                min_index = l
            elif self.heap[l][1] == self.heap[min_index][1] and self.heap[l][0] < self.heap[min_index][0]:
                min_index = l
        if r <= n-1:
            if self.heap[r][1] < self.heap[min_index][1]:
                min_index = r
            elif self.heap[r][1] == self.heap[min_index][1] and self.heap[r][0] < self.heap[min_index][0]:
                min_index = r
        
        '''
        if l <= n-1 and self.heap[l][1] < self.heap[min_index][1]:
            min_index = l
        elif l <= n-1 and self.heap[l][1] == self.heap[min_index][1] and self.heap[l][0] < self.heap[min_index][0]:
            min_index = l
        if r <= n-1 and self.heap[r][1] < self.heap[min_index][1]:
            min_index = r
        elif r <= n-1 and self.heap[r][1] == self.heap[min_index][1] and self.heap[r][0] < self.heap[min_index][0]:
            min_index = r
        '''
        
        if i != min_index:
            self.heap[i][0], self.heap[min_index][0] = self.heap[min_index][0], self.heap[i][0]
            self.heap[i][1], self.heap[min_index][1] = self.heap[min_index][1], self.heap[i][1]
            # swap two rows of an array, the following line is more efficient.
            #self.heap[i, :], self.heap[min_index, :] = self.heap[min_index, :], self.heap[i, :].copy() 
            self.sift_down(min_index)
        else:
            return
        
    def index_find_min(self, i):
        self.assigned_workers[i], self.start_times[i] = self.heap[0][0], self.heap[0][1]
        #print('before = ', self.heap)
        self.heap[0][1] += self.jobs[i]
        #print('update = ', self.heap)
        self.sift_down(0)
        #print('after= ', self.heap)
        return

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.size = len(self.jobs)
        assert m == self.size

    def write_response(self):
        for worker_id, start_time in self.result:
            print(worker_id, start_time)

    def assign_jobs(self):
        self.result = []
        self.q = [Worker(i) for i in range(self.num_workers)]

        for job in self.jobs:
            w = heapq.heappop(self.q)

            self.result.append((w.thread_id, w.release_time))

            w.release_time += job
            heapq.heappush(self.q, w)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == "__main__":
    job_queue = JobQueue()
    job_queue.solve()