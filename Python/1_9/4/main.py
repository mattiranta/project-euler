import sys
import os
import time
import math
from euler_lib import is_palindrome
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
###############################################################################

def factorize(n):
	for i in range(999, 99, -1):
		if n % i == 0:
			return (i, round(n/i))

	return (0,0)

def largest_palindrome():
	largest_possible_product = 999 * 999
	for i in range(largest_possible_product + 1, 1, -1):
		if is_palindrome(i):
			(x,y) = factorize(i)
			if x > 99 and x < 1000 and y > 99 and y < 1000:
				return (i, x, y)


	return None

# Main:
start = time.clock()
(palindrome, x, y) = largest_palindrome()
print ("Largest palindrome: {} = {} x {}".format(palindrome, x, y))
print ("Time: {}".format(time.clock() - start))





