import sys
import os
import timeit
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?
###############################################################################


def integer_right_triangles(max_p):
    ps = [0] * (max_p + 1)
    for a in range(1, int(max_p/2)):
        for b in range(a, int(max_p/2)):
            
            c = math.sqrt(a*a + b*b)

            p = int(a) + int(b) + int(c)
            if p > max_p:
                break

            if c != int(c):
                continue

            ps[p] += 1


    return ps.index(max(ps)), max(ps)


def main():
    p, max_p = integer_right_triangles(1000)
    print("Number of solutions is maximized for p: {} ({} solutions)".format(p, max_p))
    

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))