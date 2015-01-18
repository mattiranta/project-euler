import sys
import os
import timeit
import itertools
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import sieve_of_erastothenes
from euler_lib import permutations

###############################################################################
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?
###############################################################################


def concat_prime_perms():

    all_primes = sieve_of_erastothenes(9999)
    primes = set([i for i in all_primes if i > 999])

    for i in range(3333, 1000, -1):
        for j in range(1000, 9999):
            hits = list()
            for k in range(0, 3):
                curr = j + k*i
                if curr > 9999:
                    break

                if curr in primes:
                    hits.append(curr)

            if len(hits) >= 3 and hits[0] != 1487:
               if permutations(hits):
                   return "".join('{0}'.format(n) for n in hits)

    return "- not found -"


def main():
    print("Concatenated prime permutations: {}".format(concat_prime_perms()))
    
    
def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()