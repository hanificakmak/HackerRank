import calendar

month, day, year = map(int, input().split())    # While taking input it is better to use with strip() function to remove spaces

print(calendar.day_name[calendar.weekday(year, month, day)].upper())    # weekday() function's inner format is defined as weekday(year, month, day)
