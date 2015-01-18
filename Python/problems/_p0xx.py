import sys
import os
import time
import math
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
#
###############################################################################

def f():
    return 1

def main():
    print("Result: {}".format(f()))


def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()