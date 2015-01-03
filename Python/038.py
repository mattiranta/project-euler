import sys
import os
import timeit
import itertools
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?
###############################################################################


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


def find_concatenated_products(min, max):
    i = 0
    conc_products = []
    conc_prod = 1
    break_outer = False
    while True:
        i += 1
        j = 0

        conc = ""
        while True:
            j += 1

            conc += str(i*j)
            if j == 1:
                continue

            conc_prod = int(conc)
            if conc_prod > max:
                if j == 2:
                    break_outer = True

                break

            if conc_prod > min:
                conc_products.append(conc_prod)

        if break_outer:
            break

    return conc_products


def is_pandigital(n):
    str_n = str(n)
    for i in range(1, 10):
        if str(i) not in str_n:
            return False

    return True


def largest_pandigital_concatenated_product():
    conc_products = find_concatenated_products(123456789, 987654321)
    for i in reversed(conc_products):
        if is_pandigital(i):
            return i

    return -1


def main():
    print("Largest pandigital concatenated product: {}".format(largest_pandigital_concatenated_product()))
    

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))