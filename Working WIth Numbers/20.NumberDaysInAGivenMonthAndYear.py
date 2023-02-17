# Number of days in a given month of a given year.

month = int(input())
year = int(input())
no_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if(month == 2 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
    print(no_of_days[month - 1] + 1)
else:
    print(no_of_days[month - 1])