import sys
import os
import time
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import sieve_of_erastothenes

###############################################################################
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?
###############################################################################

# Below 100: 2 + 3 + 5 + 7 + 11 + 13 = 41
# Below 1000: 953 (21 terms)


def most_consecutive_prime_sum(max):
    primes = sieve_of_erastothenes(max)
    prime_count = len(primes)
    p_set = set(primes)
    
    longest_term_count = 0
    ret = 0
    for i in range(prime_count):
        sum = 0
        term_count = 0
        for j in range(i, prime_count):
             sum += primes[j]

             if sum > max:
                 break

             term_count += 1
             if term_count > longest_term_count and sum in p_set:
                 longest_term_count = term_count
                 ret = sum

    return ret


def main():
    print("Most consecutive prime sum: {}".format(most_consecutive_prime_sum(1000000)))
    
    
print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))