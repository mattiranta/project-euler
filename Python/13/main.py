# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import time
import sys

def read_input(path):
	f = open(path)
	return [int(num) for num in f.readlines() ]

def first_ten_digits_of_sum(numbers):
	return str(sum(numbers))[:10]

# Main:
start = time.clock()

digits = first_ten_digits_of_sum(read_input("input.txt"))
print("First ten digits of the sum: {}".format(digits))
print ("Time: {}".format(time.clock() - start))





