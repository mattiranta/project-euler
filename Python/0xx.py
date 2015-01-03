import sys
import os
import time
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
#
###############################################################################

def f():
	pass


# Main:
import time
start = time.clock()
print(": {}".format(f()))
print ("Time: {}".format(time.clock() - start))
