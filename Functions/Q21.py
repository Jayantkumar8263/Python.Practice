"""Write a Python program that invokes a function after a specified period of time.

Sample Output:
Square root after specific miliseconds:
4.0
10.0
158.42979517754858"""


import math
import time
def square_root(number, delay):
    time.sleep(delay / 1000)  # Sleep is a built-in function in Python that is used to delay the execution of a program for a specified amount of time. The time is given in seconds.
    return math.sqrt(number)
print("Square root after specific miliseconds:")
print(square_root(16, 1000))  # 1 second delay
print(square_root(100, 2000))  # 2 seconds delay
print(square_root(25000, 3000))  # 3 seconds delay