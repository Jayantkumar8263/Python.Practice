"""Write a Python program that reads two integers representing a month and day and prints the season for that month and day."""

month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
if month in (12, 1) and day in range(1, 32):
    print("Winter")
elif month in (3, 4, 5) and day in range(1, 32):
    print("Spring")
elif month in (6, 7, 8) and day in range(1, 32):
    print("Summer")
elif month in (9, 10, 11) and day in range(1, 32):
    print("Autumn")
elif month == 2 and day in range(1, 30):
    print("Winter")
else:
    print("Invalid month or day")