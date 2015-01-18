import sys
import os
import timeit
import itertools
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.
###############################################################################


def nth_permutation(input, n):
    return next(itertools.islice(itertools.permutations(input), n, None), None)
    
    
def main():
    print("Millionth lexicographic permutation: {}".format(''.join((nth_permutation("0123456789", 999999)))))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()
