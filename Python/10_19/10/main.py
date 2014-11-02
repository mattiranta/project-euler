import sys
import math
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append('../../')
from euler_lib import sieve_of_erastothenes

###############################################################################
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
###############################################################################

def sum_of_primes_below(n, primes):
	sum = 0
	for i in primes:
		if i > n:
			return sum

		sum += i

	return -1

# Main:
start = time.clock()

# A good guess of how far we have to go, to include nth prime
max = 2000010
n   = 2000000

primes = sieve_of_erastothenes(max)

sum = sum_of_primes_below(n, primes)

if sum > -1:
	print ("Sum of primes below {}: {}".format(n, sum))
else:
	print(
		"Not enough primes were calculated (last prime in sequence was {}th = {})"
		.format(len(primes), primes[-1]))

print ("Time: {0:.4f} (s)".format(time.clock() - start))





