import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append('../../')
from euler_lib import is_prime

###############################################################################
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
###############################################################################

def largest_prime_factor(n):
	sqrt_n = round(math.sqrt(n))
	factor = 0

	for i in range(2, sqrt_n):
		if n % i == 0 and is_prime(i):
			factor = i

	return factor


# Main:
start = time.clock()
factor = largest_prime_factor(600851475143)
print ("Largest prime factor: {}".format(factor))
print ("Time: {}".format(time.clock() - start))





