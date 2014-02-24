import sys
import math
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and
# it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
# the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two
# abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
###############################################################################

def find_all_abundant_numbers(max):
    abundants = []
    for n in range(12, max + 1):
        divisors = []
        sqrt_n = int(math.sqrt(n))
        step = 1
        if n % 2 != 0:
            step = 2

        for i in range(1, sqrt_n + 1, step):
            if n % i == 0:
                divisors.append(i)
                if i*i != n and i != 1:
                    divisors.append(int(n/i))

        if sum(divisors) > n:
            abundants.append(n)

    return abundants

def non_abundant_sums(max):
    abundants = find_all_abundant_numbers(max)
    integers = [True] * max
    half = int(len(abundants)/2)
    for i in range(0, half):
        for j in range(i, len(abundants)):
            if abundants[i] + abundants[j] >= max:
                break

            integers[abundants[i] + abundants[j]] = False

    ret = 0
    for i in range(0, max):
        if integers[i]:
            ret += i

    return ret

# Main:
start = time.clock()

max = 28123
print ("Sum of all the positive integers which cannot be written as the sum of two abundant numbers: {}".format(non_abundant_sums(max)))
print ("Time: {0:.4f} (s)".format(time.clock() - start))





