import sys
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append('../../')
from euler_lib import sieve_of_erastothenes

###############################################################################
# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
###############################################################################

def is_truncatable_prime(i, p): 
        str_i = str(i)
        for j in range(len(str(i)), 1, -1):
            substr_i = str_i[0:j - 1]
            if int(substr_i) not in p:
                return False

        for j in range(1, len(str(i))):
            substr_i = str_i[j:]
            if int(substr_i) not in p:
                return False
           
        return True

def truncatable_primes():
    primes = sieve_of_erastothenes(750000)
    primes_set = set(primes)
    truncatable = set()
    for i in primes:
        if i < 10:
            truncatable.add(i)
            continue

        if is_truncatable_prime(i, primes_set):
            truncatable.add(i)

    truncatable.remove(2)
    truncatable.remove(3)
    truncatable.remove(5)
    truncatable.remove(7)
    return truncatable


# Main:
import time
start = time.clock()
print("Sum of eleven truncatable primes: {}".format(sum(truncatable_primes())))
print ("Time: {}".format(time.clock() - start))
