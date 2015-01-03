import sys
import math
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
###############################################################################

def proper_divisors(n):
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

    return divisors

def sum_of_amicables(max):
    sum_of_amicables = 0
    sums_of_divisors = []
    amicables = []
    for i in range(0, (max + 1)):

        sums_of_divisors.append(sum(proper_divisors(i)))

    for i in range(0, max + 1):
        if sums_of_divisors[i] < max and sums_of_divisors[i] != i and sums_of_divisors[sums_of_divisors[i]] == i:
            amicables.append(i)
            sum_of_amicables += i

    return (sum_of_amicables, amicables)


def main():
    max = 10000
    sum, amicables = sum_of_amicables(max)
    print ("Sum of all the amicable numbers under {}: {}".format(max, sum))
    

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))




