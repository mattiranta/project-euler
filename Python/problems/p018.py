import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the maximum total from top to bottom of the triangle below:
###############################################################################

input = \
"""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def read_input(input):
    rows = []
    for line in input.split('\n'):
        if line:
            rows.append([int(number) for number in line.split(" ") if number.strip()])

    return rows

def max_sum(rows):
    for row in range(len(rows) - 1, -1, -1):
        for i, val in enumerate(rows[row][:-1]):
            rows[row - 1][i] += max(rows[row][i], rows[row][i + 1])

    return rows[0][0]


def main():
    base = 2
    exp = 1000
    sum = max_sum(read_input(input))
    print("max sum: {}".format(sum))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()

