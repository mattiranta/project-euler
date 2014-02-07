# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
import sys

def sieve_of_erastothenes(max):
	sqrt_max = math.ceil(math.sqrt(max))
	ps = []
	sieve = [True] * (max + 1)

	for p in range(2, max + 1):
		if sieve[p]:
			ps.append(p)
			for i in range(p * p, max + 1, p):
				sieve[i] = False

	return ps

def sum_of_primes_below(n, primes):
	sum = 0
	for i in primes:
		if i > n:
			print("n: {},  i: {}".format(n, i))
			return sum

		sum += i

	return -1

# Main:
import time
start = time.clock()

# A good guess of how far we have to go, to include nth prime
max = 2000010
n   = 2000000

primes = sieve_of_erastothenes(max)
print("Primes calculated: {}, last prime: {}".format(len(primes), primes[-1]))

sum = sum_of_primes_below(n, primes)

if sum > -1:
	print ("Sum of primes below {}: {}".format(n, sum))
else:
	print(
		"Not enough primes were calculated (last prime in sequence was {}th = {})"
		.format(len(primes), primes[-1]))

print ("Time: {0:.4f} (s)".format(time.clock() - start))





