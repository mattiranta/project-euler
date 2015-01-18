import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import find_nth_prime

###############################################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001 prime number?
###############################################################################


def main():
    n = 10001
    print("{} prime number: {}".format(n, find_nth_prime(n)))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()