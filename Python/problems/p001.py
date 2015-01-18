#!/usr/bin/env python3

import sys
import os
import time
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
###############################################################################

def multiples():
    i = 0
    sum = 0
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        i += 1

    return sum


def main():
    print("Sum of multiples: {}".format(multiples()))


def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()