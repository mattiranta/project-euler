# What is the first term in the Fibonacci sequence to contain 1000 digits?

import math
import sys

def fib_gen():
	yield 1
	yield 1
	f1, f2 = 1, 1
	while True:
		f1, f2 = f2, f1 + f2
		yield f2

def first_fib_term_with_over_n_digits(n):
	fib = fib_gen()
	i = 0
	while True:
		i += 1
		curr = next(fib)
		if len(str(curr)) >= n:
			return i

# Main:
import time
start = time.clock()

n = 1000
fib1000terms = first_fib_term_with_over_n_digits(n)
print("First term in the Fibonacci sequence to contain 1000 digits: {}".format(fib1000terms))

print ("Time: {}".format(time.clock() - start))





