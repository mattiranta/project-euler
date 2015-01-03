import sys
import math
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
###############################################################################


def is_palindrome(i, base):
	if base == 10:
		return str(i) == str(i)[::-1]
	elif base == 2:
		return str(bin(i))[2::] == str(bin(i))[2::][::-1]

	return True

def sum_of_palindromes(max):
	sum = 0
	for i in range(0, max + 1):
		#print(str(bin(i))[2::])
		if is_palindrome(i, 10) and is_palindrome(i, 2):
			sum += i
	return sum


def main():
	max = 1000000
	print ("Sum of palindromic numbers below {}: {}".format(max, sum_of_palindromes(max)))
	

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))


