"""Write a Python program to square and cube every number in a given list of integers using Lambda."""
numbers = [1, 2, 3, 4, 5]
# Square
square = list(map(lambda x: x ** 2, numbers))
print("Square of numbers:", square) 
# Cube
cube = list(map(lambda x: x ** 3, numbers))
print("Cube of numbers:", cube)