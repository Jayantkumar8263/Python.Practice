"""Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence."""

num = input("enter the numbers : ")

for i in num.split(","):
    if int(i) % 5 == 0:
        print(f"form {num} the numbers that are divisible by 5 are : {i}")
