import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
###############################################################################


def champernownes_constant():
    i = 1
    num = ""
    while len(num) < 1000000:
        num += str(i)
        i += 1

    d = 1
    ret = 1

    for i in range(7):
        #print('{}: d = {}'.format(num[d-1], d))
        ret *= int(num[d-1])
        d *= 10

    return ret


def main():
    print("Value for of expression: {}".format(champernownes_constant()))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()