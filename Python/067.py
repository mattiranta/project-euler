import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Find the maximum total from top to bottom of the triangle below:
###############################################################################

def read_input(path):
    f = open(path)
    rows = []
    for line in f.readlines():
        if line:
            rows.append([int(number) for number in line.split(" ") if number.strip()])

    return rows

def max_sum(rows):
	for row in range(len(rows) - 1, -1, -1):
		for i, val in enumerate(rows[row][:-1]):
			rows[row - 1][i] += max(rows[row][i], rows[row][i + 1])

	return rows[0][0]

# Main:
def main():
    base = 2
    exp = 1000
    sum = max_sum(read_input('../data/067_triangle.txt'))
    print("max sum: {}".format(sum))

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))



