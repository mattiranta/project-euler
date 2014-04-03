import sys
import os
import time
import itertools
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# The number, 1406357289, is a 0 to 9 pandigital number because it is made
# up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
# we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.
###############################################################################

def find_pandigitals(min, max):
    pandigitals = []
    str_n = ""
    for i in range(0, max ):
        str_n += str(i)
        if (i + 1) < min:
            continue

        perms = list(map("".join, itertools.permutations(str_n)))
        for j in perms:
            pandigitals.append(int(j))

    return pandigitals

def find_divisible_pandigitals():
    pandigitals = find_pandigitals(10, 10)
    divisibles = list()

    count = 0
    for n in pandigitals:
        count += 1
        n_str = str(n)
        if int(n_str[7:]) % 17 == 0:
            if int(n_str[6:9]) % 13 == 0:
                if int(n_str[5:8]) % 11 == 0:
                    if int(n_str[4:7]) % 7 == 0:
                        if int(n_str[3:6]) % 5 == 0:
                            if int(n_str[2:5]) % 3 == 0:
                                if int(n_str[1:4]) % 2 == 0:
                                    divisibles.append(n)
        
        n -= 1


    return divisibles


# Main:
start = time.clock()
print("Sum of all divisible 0 to 9 pandigitals: {}".format(sum(find_divisible_pandigitals())))
print ("Time: {}".format(time.clock() - start))
