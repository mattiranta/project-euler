import sys
import os
import time
import math
import timeit
import functools
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import lcm

###############################################################################
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
###############################################################################


def smallest_evenly_divisible(min, max):
    n = 20
    while True:
        is_divisible = True
        for i in [11,12,13,14,15,16,17,18,19]:
            if is_divisible and n % i == 0:
                pass
            else:
                is_divisible = False

        if is_divisible:
            return n

        n += 20

    return None


def smallest_evenly_divisible_faster(min, max):
    return functools.reduce(lcm, range(min, max + 1))


def main():
    min = 1
    max = 20
    #n = smallest_evenly_divisible(min, max)
    n = smallest_evenly_divisible_faster(min, max)
    print ("Smallest positive number evenly divisible by all [{}..{}]: {}".format(min, max, n))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()