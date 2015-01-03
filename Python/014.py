import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the maximum total from top to bottom of the triangle below:
###############################################################################


def longest_collatz_seq(lower_limit, upper_limit):
	longest_seq = (0, 0)
	cache = {}
	for i in range(lower_limit, upper_limit + 1):
		curr = i
		depth = 0
		while curr != 1:
			if curr in cache:
				depth += cache[curr]
				break
			elif curr % 2 == 0:
				curr = curr / 2
			else:
				curr = (3 * curr) + 1
			
			depth += 1

		if depth > longest_seq[1]:
			longest_seq = (i, depth)

		cache[i] = depth

	return longest_seq


def main():
	lower_limit = 1
	upper_limit = 1000000
	(start_elem, elems) = longest_collatz_seq(lower_limit, upper_limit)
	print("Longest chain has {} elems and starts from {}".format(elems, start_elem))
	

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))



