import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
#begin by sorting it into alphabetical order. 
#Then working out the alphabetical value for each name, 
#multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, 
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
#So, COLIN would obtain a score of 938 x 53 = 49714.

#What is the total of all the name scores in the file?
###############################################################################


def read_input(path):
    return [name.replace('"', '') for name in open(path).read().split(',')]
    
def sum_ascii_chars(str):
    return sum((ord(c) - 64 for c in str))

def calc_name_scores(names):
    return [sum_ascii_chars(name) * (pos + 1) for pos, name in enumerate(sorted(names))]


def main():
    total = sum(calc_name_scores(read_input("../../data/022_names.txt")))
    print("Total of all name scores: {}".format(total))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()

