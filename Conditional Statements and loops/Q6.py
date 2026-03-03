"""Write a Python program to count the number of even and odd numbers in a series of numbers"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in numbers:
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")