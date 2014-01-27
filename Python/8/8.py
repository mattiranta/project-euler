# Find the greatest product of five consecutive digits in the 1000-digit number.

import math
import sys

def read_digits(path):
	f = open(path, "r")
	digits = f.read()
	digits = digits.translate(None," \r\n")
	return map(int, digits)


def find_greatest_product(numbers):
	max_product = 0
	for i in range(4, len(numbers)):
		product = numbers[i - 4] * numbers[i - 3] * numbers[i - 2] * numbers[i - 1] * numbers[i]
		max_product = max(max_product, product)

	return max_product


# Main:
import time
start = time.clock()

input_file = "input.txt"

greatest_product = find_greatest_product(read_digits(input_file))
print("Greatest product of five consecutive digits: {}".format(greatest_product))

print ("Time: {}".format(time.clock() - start))





