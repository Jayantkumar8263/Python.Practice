"""Write a Python program to detect the number of local variables declared in a function."""

def local_variables():
    a = 10
    b = 20
    c = 30
    print("Number of local variables are :", len(locals()))
local_variables()
