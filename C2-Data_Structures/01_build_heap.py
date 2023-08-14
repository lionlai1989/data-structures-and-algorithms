#!/usr/bin/env python3

class HeapBuilder:
	def __init__(self):
		self._swaps = []
		self._data = []

	def ReadData(self):
		self.n = int(input())
		self._data = [int(s) for s in input().split()]
		#self.n = 10
		#self._data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
		#self.n = 5
		#self._data = [5, 4, 3, 2, 1]
		assert self.n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
			print(swap[0], swap[1])

	def left_child(self, i):
		return 2*i+1

	def right_child(self, i):
		return 2*i+2 

	def sift_down(self, i):
		min_index = i
		l = self.left_child(i)
		if l <= self.n-1 and self._data[l] < self._data[min_index]:
			min_index = l
		r = self.right_child(i)
		if r <= self.n-1 and self._data[r] < self._data[min_index]:
			min_index = r
		if i != min_index:
			self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
			self._swaps.append((i, min_index))
			self.sift_down(min_index)

	def build_Heap(self):
		#print(self._data)
		for i in reversed(range(0, int((self.n-1)/2)+1)):
			#print(i)
			self.sift_down(i)

	def GenerateSwaps(self):

		'''
		# The following naive implementation just sorts 
		# the given sequence using selection sort algorithm
		# and saves the resulting sequence of swaps.
		# This turns the given array into a heap, 
		# but in the worst case gives a quadratic number of swaps.
		#
		# TODO: replace by a more efficient implementation
		for i in range(len(self._data)):
			for j in range(i + 1, len(self._data)):
				if self._data[i] > self._data[j]:
					self._swaps.append((i, j))
				self._data[i], self._data[j] = self._data[j], self._data[i]
		'''

	def Solve(self):
		self.ReadData()
		#self.GenerateSwaps()
		self.build_Heap()
		self.WriteResponse()
if __name__ == '__main__':
	heap_builder = HeapBuilder()
	heap_builder.Solve()