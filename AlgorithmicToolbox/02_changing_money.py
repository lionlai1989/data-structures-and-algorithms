# Uses python3
import sys

def get_change(n):
    no_ten = 0
    no_five = 0
    no_one = 0
    no_ten = n // 10 #(floored) quotient
    no_five = (n % 10) // 5
    no_one = (n % 10) % 5
    #print(no_one, no_five, no_ten)
    return int(no_one + no_five + no_ten)

if __name__ == '__main__':
	input = sys.stdin.readline()
	n = int(input)
	print(get_change(n))
