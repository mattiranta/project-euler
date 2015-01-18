import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import factor

###############################################################################
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 x 7
# 15 = 3 x 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.

# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?
###############################################################################


def find_first_consecutive_integers_with_four_distinct_prime_factors():
    
    found = 0
    i = 2 * 3 * 5 * 7
    while True:
        i += 1
        if len(factor(i)) >= 4:
            found += 1
        else:
            found = 0

        if found == 4:
            return i - 3

    return -1


def main():
    print("First number of the first four consecutive integers to have four distinct prime factors: {}"
          .format(find_first_consecutive_integers_with_four_distinct_prime_factors()))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()