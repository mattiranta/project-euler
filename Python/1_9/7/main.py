import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001 prime number?
###############################################################################


def sieve_of_erastothenes(max):
	ps = []
	sieve = [True] * (max + 1)

	for p in range(2, max + 1):
		if sieve[p]:
			ps.append(p)
			for i in range(p * p, max + 1, p):
				sieve[i] = False

	return ps

# Main:
start = time.clock()

# A good guess of how far we have to go, to include nth prime
max = 105000
n = 10001

primes = sieve_of_erastothenes(max)

if len(primes) >= n:
	print ("{} prime: {}".format(n, primes[n-1]))
else:
	print(
		"Not enough primes were calculated (last prime in sequence was {}th = {})"
		.format(len(primes), primes[-1]))

print ("Time: {}".format(time.clock() - start))





