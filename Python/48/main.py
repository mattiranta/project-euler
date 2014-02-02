# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import math
import sys

def last_digits(n, count):
	return str(n)[-count:]

def sum_self_powers(start, end):
	return sum(num ** num for num in range(start, end + 1))

# Main:
import time
start = time.clock()

digits = last_digits(sum_self_powers(1,1000), 10)
print("Last ten digits of the series 1^1 + 2^2 + ... 1000^1000: {}".format(digits))
print ("Time: {}".format(time.clock() - start))





