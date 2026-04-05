"""Write a Python program to extract year, month, date and time using Lambda."""

import datetime
x = lambda y : datetime.datetime.strptime(y, '%Y-%m-%d %H:%M:%S')
print(f" today's year is: {x('2024-06-01 12:30:45').year}")
print(f" the month is: {x('2024-06-01 12:30:45').month}")
print(f" the day is: {x('2024-06-01 12:30:45').day}")
print(f" the hour is: {x('2024-06-01 12:30:45').hour}")
print(f" the minute is: {x('2024-06-01 12:30:45').minute}")
print(f" the second is: {x('2024-06-01 12:30:45').second}")