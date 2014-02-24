import sys
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
#
###############################################################################

start = time.clock()

def f():
	pass


# Main:
import time
start = time.clock()
print(": {}".format(f()))
print ("Time: {}".format(time.clock() - start))
