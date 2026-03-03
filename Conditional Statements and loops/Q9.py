"""Write a Python program to get the Fibonacci series between 0 and 50."""

a = 0
b = 1
while a < 50:
    print(a, end=' ')
    a, b = b, a + b