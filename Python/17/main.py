# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

import sys

def count_letters(words):
	letters = 0
	#print(words)
	for word in words:
		#print(word)
		letters += len(word.replace(' ', ''))

	return letters

def numbers_as_words():
	n = [''] * 1000

	n[0] = 'one'
	n[1] = 'two'
	n[2] = 'three'
	n[3] = 'four'
	n[4] = 'five'
	n[5] = 'six'
	n[6] = 'seven'
	n[7] = 'eight'
	n[8] = 'nine'
	n[9] = 'ten'
	n[10] = 'eleven'
	n[11] = 'twelve'
	n[12] = 'thirteen'
	n[13] = 'fourteen'
	n[14] = 'fifteen'
	n[15] = 'sixteen'
	n[16] = 'seventeen'
	n[17] = 'eighteen'
	n[18] = 'nineteen'
	n[19] = 'twenty'
	n[29] = 'thirty'
	n[39] = 'forty'
	n[49] = 'fifty'
	n[59] = 'sixty'
	n[69] = 'seventy'
	n[79] = 'eighty'
	n[89] = 'ninety'
	n[99] = 'hundred'
	n[999] = 'thousand'
	print(n)
	return n
	
# Main:
import time
start = time.clock()
letter_count = count_letters(numbers_as_words())
print("Letters used: {}".format(letter_count))
print ("Time: {}".format(time.clock() - start))





