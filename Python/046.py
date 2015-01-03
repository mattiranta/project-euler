import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import sieve_of_erastothenes

###############################################################################
# It was proposed by Christian Goldbach that every odd composite number can
# be written as the sum of a prime and twice a square.

# 9 = 7 + 2x12
# 15 = 7 + 2x22
# 21 = 3 + 2x32
# 25 = 7 + 2x32
# 27 = 19 + 2x22
# 33 = 31 + 2x12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
###############################################################################


def is_twice_a_square(n):
    test = math.sqrt(n/2)
    return int(test) == test

def smallest_comp_not_sum_of_prime_and_double_square():
    limit = 10000
    primes = sieve_of_erastothenes(limit)
    odds = []

    for odd in range(3, limit, 2):
        if odd in primes: 
            continue

        found = False
        for prime in primes:
            if prime >= odd: 
                break

            n = odd - prime
            if is_twice_a_square(n):
                found = True
                break

        if not found:
            return odd

    return -1

def main():
    print("Smallest odd composite that cannot be written as the sum of a prime and twice a square: {}"
          .format(smallest_comp_not_sum_of_prime_and_double_square()))


print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))