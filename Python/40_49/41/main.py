import sys
import os
import time
import itertools
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
###############################################################################

start = time.clock()

def is_prime(n):
    if(n == 2):
        return True
    if(n % 2 == 0):
        return False

    sqrtn = int(round(math.sqrt(n)))
    for i in range(3, sqrtn):
        if( n % i == 0):
            return False

    return True


def find_pandigitals(min, max):
    pandigitals = []
    str_n = ""
    for i in range(1, max + 1):
        str_n += str(i)
        if i < min:
            continue

        perms = list(map("".join, itertools.permutations(str_n)))
        for j in perms:
            pandigitals.append(int(j))

    return pandigitals


def largest_pandigital_prime():
    # According to divisibility rule for number 3,
    # 8- or 9-digit pandigitals cannot be solutions, because
    # 1+2+3+4+5+6+7+8 = 36 mod 3 = 0 and 1+2+3+4+5+6+7+8+9 = 45 mod 3 = 0.
    # That means, they cannot be primes. 
    # Therefore, 7-digit number is the largest possible solution.
    pandigitals = find_pandigitals(7, 7)
    for p in reversed(pandigitals):
        if is_prime(p):
            return p

    return -1


# Main:
import time
start = time.clock()
print("Largest n-digit pandigital prime: {}".format(largest_pandigital_prime()))
print ("Time: {}".format(time.clock() - start))
