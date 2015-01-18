import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the greatest product of five consecutive digits in the 1000-digit number.
###############################################################################

def power_digit_sum(base, exp):
    digits = str(base ** exp)
    return sum(map(int, digits))


def main():
    base = 2
    exp = 1000
    sum = power_digit_sum(base, exp)
    print("Sum of the digits of the number 2^1000: {}".format(sum))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()

