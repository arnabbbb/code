# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:40:41 2021

@author: arnab19
"""

"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if year % 4 == 0 and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        return 30
        

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year <= datetime.MAXYEAR and year >= datetime.MINYEAR and month > 0 and month < 13 and day <= days_in_month(year, month) and day >= 1:
        return True
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2) and (datetime.date(year2, month2, day2) -  datetime.date(year1, month1, day1)).days >= 0:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        return (date2 - date1).days
    else:
        return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day) and datetime.date(year, month, day) <= datetime.date.today():
        return  (datetime.date.today() - datetime.date(year, month, day) ).days
    return 0
print(age_in_days(1,1,1))
print(days_between(1,1,1,2,2,2))
print(is_valid_date(1,1,1))
print(days_in_month(1,1))
