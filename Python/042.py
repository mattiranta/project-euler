import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; 
# so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical
# position and adding these values we form a word value. For example,
# the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?
###############################################################################


def sum_letters(word):
    return sum([int(ord(letter)) - 64 for letter in word])

def is_triangle_number(n):
    test = math.sqrt(8*n + 1)
    return test == int(test)

def triangle_word_count(path):
    f = open(path)
    words = f.read().split(',')
    count = 0
    for word in words:
        if is_triangle_number(sum_letters(word.strip('"'))):
            count += 1

    return count


# Main:
def main():
    print("Count of triangle words: {}".format(triangle_word_count("../data/042_words.txt")))

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))
