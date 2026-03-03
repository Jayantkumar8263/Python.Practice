"""Write a Python program that checks whether a string represents an integer or not."""

s = input("Enter the string :")
try:
    int(s)
    print(f"{s} is an integer")
except ValueError:
    print(f"{s} is not an integer")