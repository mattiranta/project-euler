import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# What is the value of the first triangle number to have over five hundred divisors?
###############################################################################


def triangulars():
	sum, i = 1, 1
	
	while True:
		yield sum
		i = i + 1
		sum = sum + i


def count_divisors(n):
	if n == 1: return 1

	count, i = 0, 1
	sqrt_n = int(math.sqrt(n))

	while i <= sqrt_n:
		if n % i == 0:
			count += 2

		i += 1

	if n == sqrt_n ** 2:
		count -= 1
		
	return count

def find_triangular_number_with_divisors(div_limit):
	t_gen = triangulars()
	while True:
		num = next(t_gen)

		# Optimization, to test only even numbers
		if num % 2 != 0: continue

		divisors = count_divisors(num)
		if divisors > div_limit:
			return (num, divisors)
			break

	return (0,0)


def main():
	limit = 500
	(first, divisors) = find_triangular_number_with_divisors(limit)
	print("First triangular number with more than {} divisors: {} ({} divisors)".format(limit, first, divisors))
	

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))
