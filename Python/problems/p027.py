import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Euler discovered the remarkable quadratic formula:

# n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the
# consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces
# the maximum number of primes for consecutive values of n, starting with n = 0.
###############################################################################


def is_prime(n):
    if n <= 0:
        return False

    if n == 1 or n == 2:
        return True

    if n % 2 == 0:
        return False

    sqrtn = int(round(math.sqrt(n)))
    for i in range(3, sqrtn):
        if( n % i == 0):
            return False

    return True

def number_of_primes_produced(a,b):
    n = 0
    while is_prime( int(n*n + a*n + b) ):
        n += 1

    return n


def coefficients_of_quadratic_expr(limit):
    max_primes, max_a, max_b = 0,0,0

    for a in range(-limit + 1, limit):
        for b in range(1, limit, 2):
            prime_count = number_of_primes_produced(a,b)
            if prime_count > max_primes:
                max_primes = prime_count
                max_primes, max_a, max_b = prime_count, a, b

        
    return max_a, max_b


def main():
    limit = 1000
    a, b = coefficients_of_quadratic_expr(limit)
    print("Product of the coefficients a and b: {}".format(a * b))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()

