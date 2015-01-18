import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
###############################################################################
def sum_of_digits_nth_power(num, n):
    return sum([int(i)**n for i in str(num)])

def digit_fifth_powers():
    ret = []
    curr = 2
    limit = 0
    while limit < (len(str(limit)) * (9 ** 5)):
        limit += 1

    while curr < limit:
        if curr == sum_of_digits_nth_power(curr, 5):
            ret.append(curr)

        curr += 1
        
    return ret


def main():
    print("Sum of numbers that can be written as the sum of fifth powers of their digits: {}".format(sum(digit_fifth_powers())))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()

