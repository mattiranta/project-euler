import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

# Triangle    Tn=n(n+1)/2       1, 3, 6, 10, 15, ...
# Pentagonal  Pn=n(3n?1)/2      1, 5, 12, 22, 35, ...
# Hexagonal   Hn=n(2n?1)        1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.
###############################################################################

def hexagonals():
    n = 1
    while True:
        yield int(n * (2 * n - 1))
        n += 1

    return

def is_pentagonal(n):
    test = (math.sqrt(24*n + 1) + 1)/6
    return test == int(test)

def triangular_pentagonal_hexagonal():
    hex = hexagonals()
    while True:
        next_hex = next(hex)

        if is_pentagonal(next_hex) and next_hex > 40755:
            return next_hex

    return 0


def main():
    print("Next triangle number that is also pentagonal and hexagonal: {}".format(triangular_pentagonal_hexagonal()))


def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()