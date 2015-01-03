import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the sum of the digits in the number 100!
###############################################################################


def sum_of_digits(n):
	return sum(int(c) for c in list(str(n)) )


def main():
    n = 100
    fact = math.factorial(n)
    print("Sum of the digits in the number 100!: {} (number is {})".format(sum_of_digits(fact), fact))
    

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))




