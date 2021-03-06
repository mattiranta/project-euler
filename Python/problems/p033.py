import sys
import os
import timeit
import math
import fractions
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
# is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.
###############################################################################


def find_curious_fractions(max):
    prod_num = 1
    prod_den = 1
    for denominator in range(10,max):
        for numerator in range (10, denominator):
            str_num = str(numerator)
            str_den = str(denominator)
            if  (str_num[0] == str_den[0]                          and numerator/denominator == int(str_num[1])/int(str_den[1])) or \
                (str_num[1] == str_den[1] and str_num[1] != '0'    and numerator/denominator == int(str_num[0])/int(str_den[0])) or \
                (str_num[0] == str_den[1] and int(str_den[0]) != 0 and numerator/denominator == int(str_num[1])/int(str_den[0])) or \
                (str_num[1] == str_den[0] and int(str_den[1]) != 0 and numerator/denominator == int(str_num[0])/int(str_den[1])):

                prod_num = prod_num * numerator
                prod_den = prod_den * denominator
    
    return int(prod_den/fractions.gcd(prod_num, prod_den))


def main():
    print("Value of denominator: {}".format(find_curious_fractions(100)))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()