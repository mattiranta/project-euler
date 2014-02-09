# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

import sys
import itertools

def nth_permutation(input, n):
	return next(itertools.islice(itertools.permutations(input), n, None), None)
	
# Main:
import time
start = time.clock()
print("Millionth lexicographic permutation: {}".format(''.join((nth_permutation("0123456789", 999999)))))
print ("Time: {}".format(time.clock() - start))




