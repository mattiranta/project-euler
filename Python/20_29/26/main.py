import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
  
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
###############################################################################

start = time.clock()

def longest_recurring_cycle(max_d):
    longest = 0
    for d in range(max_d - 1, 0, -1):
        #print(d)
        if d < longest:
            break

        remainder = 1
        seen = set()
        while remainder not in seen:
            seen.add(remainder)
            remainder = remainder * 10 % d
         
        if len(seen) > longest:
            longest = len(seen)
            longest_d = d

    return longest_d, longest



# Main:
import time
start = time.clock()
max_d = 1000
d, count = longest_recurring_cycle(max_d)
print("Value of d for longest recurring cycle: {} (length: {})".format(d, count))
print ("Time: {}".format(time.clock() - start))
