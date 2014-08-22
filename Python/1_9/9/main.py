import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
###############################################################################

def find_pythagorean_triplet(n):
	a = 0
	b = 0
	while True:
		a += 1
		if a > n:
			return None

		b = 0
		while b < a:
			b += 1
			c = math.sqrt (a*a + b*b)

			if c.is_integer() and a + b + round(c) == n:
				return (b,a,round(c))

	return None


# Main:
start = time.clock()
n = 1000
ret = find_pythagorean_triplet(n)
if ret != None:
    (a, b, c) = ret
    print ("a * b * c = {} * {} * {} = {}".format(a, b, c, a * b * c))
else:
    print("Cannot find pythagorean triplet for a + b + c = {}".format(n))

print ("Time: {}".format(time.clock() - start))





