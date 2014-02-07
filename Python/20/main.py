# Find the sum of the digits in the number 100!

import math
import sys

def sum_of_digits(n):
	return sum(int(c) for c in list(str(n)) )


# Main:
import time
start = time.clock()

n = 100
fact = math.factorial(n)
sum_of_digits = sum_of_digits(fact)
print("Sum of the digits in the number 100!: {} (number is {})".format(sum_of_digits, fact))

print ("Time: {}".format(time.clock() - start))





