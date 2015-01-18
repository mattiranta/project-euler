import sys
import os
import timeit
import itertools
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
from euler_lib import sieve_of_erastothenes

###############################################################################
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
###############################################################################


def permute_cyclically(string):
    l= []
    l.append(string)
    string1 = ''
    for i in range(0,len(string)-1,1):
        string1 = string[1:len(string)] + string[:1]
        l.append(string1)
        string = string1

    return l

def circular_primes(max):
    primes = sieve_of_erastothenes(max)

    all_numbers = [False] * (max + 1)
    for p in primes:
        all_numbers[p] = True

    circular_primes = []

    for p in primes:
        
        all_primes = True
        
        for perm in permute_cyclically(str(p)):
            n = int(perm)
            if not all_numbers[n]:
                all_primes = False
                break

        if all_primes:
            circular_primes.append(p)

    return circular_primes


def main():
    max = 1000000
    circ = circular_primes(max)
    print("Number of circular primes below {}: {}".format(max, len(circ)))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()