import sys
import os
import timeit
import datetime
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

###############################################################################
# You are given the following information, but you may prefer to do some research for yourself.

# - 1 Jan 1900 was a Monday.

# - Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.

# - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#   How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
###############################################################################


def is_leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def sundays_as_first_of_month_ver1():
    day_nr = 1
    sundays = 0

    for year in range(1900, 2001):
        for month in range(1, 13):

            days = 31
            if month == 2:
                if is_leap_year(year):
                    days = 29
                else:
                    days = 28
            elif month == 4 or month == 6 or month == 9 or month == 11:
                days = 30

            for day in range(1, days + 1):
                if day == 1 and day_nr % 7 == 0:
                    if year > 1900:
                        #print('{}/{}/{} \twas sunday ({})'.format(day, month, year, day_nr))
                        sundays += 1

                day_nr += 1

    return sundays

def sundays_as_first_of_month_ver2():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                sundays += 1

    return sundays


def main():
    #print("Sundays as first of month: {}".format(sundays_as_first_of_month_ver1()))
    print("Sundays as first of month: {}".format(sundays_as_first_of_month_ver2()))
    

def main_timed():
    print("Time: {0:.25f}".format(timeit.timeit('main()', 'from ' + os.path.splitext(os.path.basename(__file__))[0] + ' import main', number=1)))

if __name__ == "__main__":
    main_timed()


