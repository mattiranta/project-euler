import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
###############################################################################


def read_input(path):
    f = open(path)
    return [int(num) for num in f.readlines() ]

def first_ten_digits_of_sum(numbers):
    return str(sum(numbers))[:10]


def main():
    digits = first_ten_digits_of_sum(read_input("../../data/013_input.txt"))
    print("First ten digits of the sum: {}".format(digits))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()


