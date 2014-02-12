import sys
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
###############################################################################

start = time.clock()
i1 = 1
i2 = 2
sum = 2

while i2 + i1 < 4000000:
	i1, i2 = i2, i1 + i2

	if i2 % 2 == 0:
		sum += i2

elapsed = time.clock() - start
print ("Sum: {}".format(sum))
print ("Time: {}".format(elapsed))
