#!/usr/bin/env python3
import numpy as np

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
        #self.num_workers, m = 5, 20
        #self.jobs = [10, 3, 1, 4, 3, 1, 2, 2, 1, 1, 3, 4, 6, 5, 2, 1, 9, 2, 3, 1]  

        self.assigned_workers = np.array([None] * len(self.jobs))
        self.start_times = np.array([None] * len(self.jobs))
        self.heap = np.array([[value, 0] for value in range(self.num_workers)])
        assert m == len(self.jobs)

    def assign_jobs(self):
        for i in range(len(self.jobs)):
            print(self.heap[0][0], self.heap[0][1])
            self.heap[0][1] += self.jobs[i]
            
            min_index = 0
            while True:
                i = min_index
                n = self.num_workers
                l = 2*i+1
                r = 2*i+2
        
                if l <= n-1 and self.heap[l][1] < self.heap[min_index][1]:
                    min_index = l
                elif l <= n-1 and self.heap[l][1] == self.heap[min_index][1]:
                    if self.heap[l][0] < self.heap[min_index][0]:
                        min_index = l
                if r <= n-1 and self.heap[r][1] < self.heap[min_index][1]:
                    min_index = r
                elif r <= n-1 and self.heap[r][1] == self.heap[min_index][1]:
                    if self.heap[r][0] < self.heap[min_index][0]:
                        min_index = r
        
                if i != min_index:
                    self.heap[i][0], self.heap[min_index][0] = self.heap[min_index][0], self.heap[i][0]
                    self.heap[i][1], self.heap[min_index][1] = self.heap[min_index][1], self.heap[i][1]#  
                else:
                    break

    def solve(self):
        self.read_data()
        self.assign_jobs()
        

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

