# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
import sys

def find_pythagorean_triplet(n):
	print(n)
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
import time
start = time.clock()
n = 1000
(a, b, c) = (0,0,0)
ret = find_pythagorean_triplet(n)
print(ret)
if ret != None:
	(a, b, c) = ret

print ("{} + {} + {} = {}".format(a, b, c, a + b + c))
print ("a * b * c = {}".format(a * b * c))
print ("Time: {}".format(time.clock() - start))





