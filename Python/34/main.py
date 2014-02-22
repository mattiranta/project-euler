import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
###############################################################################
def sum_of_digit_factorials(num):
	return sum([sum_of_digit_factorials.facts[int(i)] for i in str(num)])

sum_of_digit_factorials.facts = [math.factorial(i) for i in range(0,10)]

def digit_factorials():
	
	ret = []
	curr = 3
	limit = 1
	while limit < sum_of_digit_factorials(int(len(str(limit))*str(9))):
		limit += 100

	# To make it run really fast, guess a much lower upper limit:
	#limit = 100000

	while curr < limit:
		if curr == sum_of_digit_factorials(curr):
			ret.append(curr)

		curr += 1
		
	return ret

# Main:
import time
start = time.clock()
print("Sum of all numbers which are equal to the sum of the factorial of their digits: {}".format(sum(digit_factorials())))
print ("Time: {}".format(time.clock() - start))





