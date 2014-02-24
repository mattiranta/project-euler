import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# Starting in the top left corner of a 2×2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?
###############################################################################

# Answer: 40!/20!/20! = 137846528820

print( 'Number of routes: {}'.format(int(math.factorial(40) / math.factorial(20) / math.factorial(20))))
