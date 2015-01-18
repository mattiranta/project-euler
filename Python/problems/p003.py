import sys
import os
import time
import math
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import is_prime

###############################################################################
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
###############################################################################

def largest_prime_factor(n):
    sqrt_n = round(math.sqrt(n))

    for i in range(sqrt_n + 1, 1, -1):
        if n % i == 0 and is_prime(i):
            return i

    return -1


def main():
    factor = largest_prime_factor(600851475143)
    print ("Largest prime factor: {}".format(factor))


def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()