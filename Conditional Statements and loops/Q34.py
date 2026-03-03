"""Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20."""

x = int(input("enter the first number :"))
y = int(input("enter the first number :"))
z = (x + y)
if z >=15 and z <=20:
    print("20")
else:
    print(z)