import sys
import math
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# Starting with the number 1 and moving to the right in a clockwise direction 
# a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
###############################################################################


def sum_of_diagonals_short(width):
    curr = 1
    total = 1
    for i in range(2, 1001, 2):
        for j in range(0, 4):
            curr += i
            total += curr

    return total

def sum_of_diagonals_long(total_width):
    ret = 0
    half = int(total_width/2)
    count = 1
    matrix = [[0 for i in range(total_width)] for j in range(total_width)]

    row = half
    col = half
    offset = 1

    while offset <= half:

        # left --> right
        while col < half + offset + 1:
            matrix[row][col] = count
            count += 1
            col += 1

        count -= 1
        col -= 1

        # up --> down
        while row < half + offset + 1:
            matrix[row][col] = count
            count += 1
            row += 1
    
        count -= 1
        row -= 1        
        
        # right --> left
        while col > half - offset - 1:
            matrix[row][col] = count
            count += 1
            col -= 1
    
        count -= 1
        col += 1

        # down --> up
        while row > half - offset - 1:
            matrix[row][col] = count
            count += 1
            row -= 1
    
        count -= 1
        row += 1   
         
        offset += 1


    # once more left --> right
    while col < half + offset:
        matrix[row][col] = count
        count += 1
        col += 1

    count -= 1
    col -= 1

    for i in range(total_width):
        ret += matrix[i][i]
        if i != half:
            ret += matrix[total_width - 1 - i][i]

    return ret


def main():
    width = 1001
    print ("Sum of the numbers on the diagonals (short): {}".format(sum_of_diagonals_short(width)))
    #print ("Sum of the numbers on the diagonals (long):  {}".format(sum_of_diagonals_long(width)))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()

