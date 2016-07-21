#!/usr/bin/env python3
import sys


def get_optimal_value(capacity, weights, values):
	value = 0.
	
	value_per_unit = [values/weights for values,weights in zip(values, weights)]
	vpu_weights_dict = dict(zip(value_per_unit, weights)) # from smallest to biggest number
	#print(vpu_weights_dict)
	for i in sorted(vpu_weights_dict.keys(), reverse=True):
		#print(capacity, i, vpu_weights_dict[i])
		if capacity > 0:
			if capacity >= vpu_weights_dict[i]:
				capacity = capacity - vpu_weights_dict[i]
				value = value + i*vpu_weights_dict[i]
			else:
				#capacity = capacity - (capacity / vpu_weights_dict[i]) * i*vpu_weights_dict[i]
				value = value + (capacity / vpu_weights_dict[i]) * i*vpu_weights_dict[i]
				capacity = 0
		#vpu_weights_dict[i]
			#print(vpu_weights_dict[i])
	#print(vpu_weights_dict)
	#for i, j in vpu_weights_dict[::-1].items():
	#	print(poop)
#	value_per_unit.sort()
	
	
	return value


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	#sys.stdin.read() will read from standard input till EOF.
	#(which is usually Ctrl+D)
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	#capacity = 3000
	#values = list([60, 100, 120])
	#weights = list([2000, 5000, 900])
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))
