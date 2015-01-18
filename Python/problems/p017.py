import sys
import os
import time
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.
###############################################################################


def get_as_text(i, n):
    ret = ''

    if i < 20:
        ret = n[i]
    elif i < 100 and i % 10 == 0:
        ret = n[(i//10) * 10]
    elif i < 100:
        ret = n[(i//10) * 10] + '-' + n[i % 10]
    elif i == 1000:
        ret = n[i // 1000] + ' ' + n[1000]
    elif i % 100 == 0:
        ret = n[i // 100] + ' ' + n[100]
    else:
        ret = n[i // 100] + ' ' + n[100] + ' and ' + get_as_text(i % 100, n)

    return ret

def letter_count():
    n = [''] * 1001
    n[1] = 'one'
    n[2] = 'two'
    n[3] = 'three'
    n[4] = 'four'
    n[5] = 'five'
    n[6] = 'six'
    n[7] = 'seven'
    n[8] = 'eight'
    n[9] = 'nine'
    n[10] = 'ten'
    n[11] = 'eleven'
    n[12] = 'twelve'
    n[13] = 'thirteen'
    n[14] = 'fourteen'
    n[15] = 'fifteen'
    n[16] = 'sixteen'
    n[17] = 'seventeen'
    n[18] = 'eighteen'
    n[19] = 'nineteen'
    n[20] = 'twenty'
    n[30] = 'thirty'
    n[40] = 'forty'
    n[50] = 'fifty'
    n[60] = 'sixty'
    n[70] = 'seventy'
    n[80] = 'eighty'
    n[90] = 'ninety'
    n[100] = 'hundred'
    n[1000] = 'thousand'
    return sum(len(get_as_text(i, n).replace(' ', '').replace('-', '')) for i in range(1, 1001))
    

def main():
    print("Letters used: {}".format(letter_count()))


def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()




