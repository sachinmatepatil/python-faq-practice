'''Problem Statement
While developing a calendar app, you notice that some years have an extra day in February. You recall the leap year rule: a year is a leap year if it is divisible by 4, except if it is divisible by 100, unless it is also divisible by 400. To correctly mark these years, you decide to implement this logic and identify leap years.

Topics
Basic Programming
Date Handling
Examples
Input:
year = 2020
Output:
Leap Year
Explanation:
2020 is divisible by 4 but not by 100, so it is a Leap Year.
Input:
year = 1900
Output:
Not a Leap Year
Explanation:
1900 is divisible by 100 but not by 400, so it is Not a Leap Year.
Input:
year = 2000
Output:
Leap Year
Explanation:
2000 is divisible by 400, so it is a Leap Year.'''

year = 2000

def leap_year(year):
    if (year % 4) == 0 and (year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
print(leap_year(year))