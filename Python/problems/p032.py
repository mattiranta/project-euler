import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once; for example, the 5-digit number, 15234,
# is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to
# only include it once in your sum.
###############################################################################


def is_pandigital(a, b, c):
    s = str(a) + str(b) + str(c)

    for i in range(1, 10):
        if str(i) not in s:
            return False

    return True

def pandigital_products():
    products = set()
    #max = int(math.sqrt(987654321))
    max = 2000
    for i in range(1, max):
        for j in range(i, max):
            prod = i * j
            if int(str(i) + str(j) + str(prod)) > 987654321:
                break;

            if is_pandigital(i, j, prod):
                products.add(prod)

    return products


def main():
    print("Sum of pandigital products: {}".format(sum(pandigital_products())))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()