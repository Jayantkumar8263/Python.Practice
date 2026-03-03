"""Write a Python program to check if a triangle is equilateral, isosceles or scalene."""

x = input("enter the first side : ")
y = input("enter the second side : ")
z = input("enter the third side : ")
if x == y == z:
    print("it is an equilateral triangle")
elif x == y or y == z or z == x:
    print("it is an isosceles triangle")
else:
    print("it is a scalene triangle")