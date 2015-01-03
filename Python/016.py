import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the greatest product of five consecutive digits in the 1000-digit number.
###############################################################################

def power_digit_sum(base, exp):
	digits = str(base ** exp)
	return sum(map(int, digits))


def main():
    base = 2
    exp = 1000
    sum = power_digit_sum(base, exp)
    print("Sum of the digits of the number 2^1000: {}".format(sum))
    

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))


