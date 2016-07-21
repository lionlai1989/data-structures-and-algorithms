#!/usr/bin/env python3

import numpy as np
import cProfile
import random

class JobQueue:
    def __init__(self):
        pass

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        #self.num_workers, m = 2, 5
        #self.jobs = [1, 2, 3, 4, 5]
        #self.num_workers, m = 4, 20
        #self.jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #self.num_workers, m = 4, 13
        #self.jobs = [1, 5, 4, 4, 2, 5, 3, 2, 1, 1, 3, 1, 2]
        '''
        self.num_workers, m = 1000, 100000
        self.jobs = [] 
        for i in range(m):
            self.jobs.append(random.randint(0, 1000000000))
        '''
        #print(len(self.jobs))
        self.assigned_workers = np.array([None] * len(self.jobs))
        self.start_times = np.array([None] * len(self.jobs))
        self.heap = np.array([[value, 0] for value in range(self.num_workers)])
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            #print(self.assigned_workers[i], self.start_times[i])
            #print(' '.join(str(self.assigned_workers[i])), ' '.join(str(self.start_times[i])))
            print(self.assigned_workers[i], self.start_times[i])

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

    def assign_jobs(self):
        for i in range(len(self.jobs)):
            self.index_find_min(i)
            
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
'''
if __name__ == "__main__":
    job_queue = JobQueue()
    cProfile.run("job_queue.solve()")
    cProfile.run("job_queue.solve()", filename="a.out")
    cProfile.run("job_queue.solve()", filename="a.out", sort="cumulative")

    import pstats 
    p = pstats.Stats("a.out")
    p.strip_dirs().sort_stats(-1).print_stats()
    p.strip_dirs().sort_stats("name").print_stats(3)
    p.strip_dirs().sort_stats("cumulative", "name").print_stats(0.5)
    p.print_callers(0.5, "sum_num")
    p.print_callees("job_queue.solve")
'''