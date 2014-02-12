import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the sum of the digits in the number 100!
###############################################################################

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





