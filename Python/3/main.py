#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

def is_prime(n):
	if(n == 2):
		return True
	if(n % 2 == 0):
		return False

	sqrtn = round(math.sqrt(n))
	for i in range(3, sqrtn):
		if( n % i == 0):
			return False

	return True

def largest_prime_factor(n):
	sqrt_n = round(math.sqrt(n))
	factor = 0

	for i in range(2, sqrt_n):
		if n % i == 0 and is_prime(i):
			factor = i

	return factor

# Main:
import time
start = time.clock()
factor = largest_prime_factor(600851475143)
print ("Largest prime factor: {}".format(factor))
print ("Time: {}".format(time.clock() - start))





