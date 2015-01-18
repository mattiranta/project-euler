import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# What is the first term in the Fibonacci sequence to contain 1000 digits?
###############################################################################


def fib_gen():
    yield 1
    yield 1
    f1, f2 = 1, 1
    while True:
        f1, f2 = f2, f1 + f2
        yield f2

def first_fib_term_with_over_n_digits(n):
    fib = fib_gen()
    i = 0
    while True:
        i += 1
        curr = next(fib)
        if len(str(curr)) >= n:
            return i


def main():
    n = 1000
    fib1000terms = first_fib_term_with_over_n_digits(n)
    print("First term in the Fibonacci sequence to contain 1000 digits: {}".format(fib1000terms))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()



