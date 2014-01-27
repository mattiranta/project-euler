# Find the greatest product of five consecutive digits in the 1000-digit number.

import math
import sys

def power_digit_sum(base, exp):
	digits = str(base ** exp)
	return sum(map(int, digits))


# Main:
import time
start = time.clock()

base = 2
exp = 1000
sum = power_digit_sum(base, exp)
print("Sum of the digits of the number 2^1000: {}".format(sum))

print ("Time: {}".format(time.clock() - start))





