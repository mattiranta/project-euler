import sys
import os
import time
import math
from euler_lib import find_nth_prime
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001 prime number?
###############################################################################

# Main:
import time
start = time.clock()
n = 10001
print("{} prime number: {}".format(n, find_nth_prime(n)))
print ("Time: {}".format(time.clock() - start))

