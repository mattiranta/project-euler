# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?

import time
import sys

def read_input(path):
	f = open(path)
	lines = f.readlines()
	numbers = []
	for line in lines:
		numbers.append([int(col) for col in line.split(' ')])
	return numbers

def greatest_product_of_four_adjacent_numbers(grid):
	greatest_product = 0
	MAX = len(grid)
	# rows:
	for line in grid:
		for i in range(0, MAX - 3):
			greatest_product = max(
				greatest_product, 
				line[i] * line[i + 1] * line[i + 2] * line[i + 3])

	# columns:
	for col in range(0, MAX):
		for line in range(0, MAX - 3):
			greatest_product = max(
				greatest_product, 
				grid[line][col] * grid[line + 1][col] * grid[line + 2][col] * grid[line + 3][col])
	

	# diagonals:
	for i in range(0, 2):

		#    upper
		for col in range(0, MAX):
			for line in range(0, MAX - 3):
				if line + col + 3 >= MAX:
					break

				greatest_product = max(
					greatest_product, 
					grid[line][line + col] * grid[line + 1][line + col + 1] * grid[line + 2][line + col + 2] * grid[line + 3][line + col + 3])

		#    lower
		col = 0
		for line in range(1, MAX - 3):
			greatest_product = max(
				greatest_product, 
				grid[line][col] * grid[line + 1][col + 1] * grid[line + 2][col + 2] * grid[line + 3][col + 3])


		# Turn the whole grid 180 degrees (right becomes left), and do the diagonals again
		for i, line in enumerate(grid):
			grid[i] = line[::-1]


	return greatest_product

# Main:
start = time.clock()

prod = greatest_product_of_four_adjacent_numbers(read_input("input.txt"))
print("Greatest product of four adjacent: {}".format(prod))
print ("Time: {}".format(time.clock() - start))





