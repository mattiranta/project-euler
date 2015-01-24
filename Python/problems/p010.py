import sys
import math
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import sieve_of_erastothenes

###############################################################################
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
###############################################################################

def sum_of_primes_below(n, primes):
    sum = 0
    for i in primes:
        if i > n:
            return sum

        sum += i

    return -1


def main():
    n = 2000000
    print ("Sum of primes below {}: {}".format(n, sum(sieve_of_erastothenes(n))))
    
    
def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()




