"""Write a Python program to convert a month name to a number of days."""

x = input("enter the month name : ")
if x in ('january', 'march', 'may', 'july', 'august', 'october', 'december'):
    print(f"{x} has 31 days")
elif x in ('april', 'june', 'september', 'november'):
    print(f"{x} has 30 days")
elif x == 'february':
    print(f"{x} has 28 or 29 days")
else:
    print("Invalid month name")