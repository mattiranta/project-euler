import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the greatest product of five consecutive digits in the 1000-digit number.
###############################################################################


def read_digits(path):
	f = open(path, "r")
	digits = f.read()
	digits = digits.replace("\n", "")
	return list(map(int, list(digits)))


def find_greatest_product(numbers):
	max_product = 0
	for i in range(4, len(numbers)):
		product = numbers[i - 4] * numbers[i - 3] * numbers[i - 2] * numbers[i - 1] * numbers[i]
		max_product = max(max_product, product)

	return max_product


def main():
    input_file = "../data/008_input.txt"
    greatest_product = find_greatest_product(read_digits(input_file))
    print("Greatest product of five consecutive digits: {}".format(greatest_product))


print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))



