import sys
import os
import time
import math
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 -?? 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
###############################################################################


def sum_square_difference(min, max):
	sum_of_squares = 0
	square_of_sum = 0
	for i in range(min, max + 1):
		sum_of_squares += i * i
		square_of_sum += i

	square_of_sum = square_of_sum * square_of_sum

	return square_of_sum - sum_of_squares


def main():
    min = 1
    max = 100
    diff = sum_square_difference(min, max)
    print ("Difference: {}".format(diff))
    

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))





