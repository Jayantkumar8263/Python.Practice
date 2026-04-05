"""Write a Python program to access a function inside a function."""

def outer_function():
    print("This is the outer function.")
    def inner_function():
        print ("this is my inner function thst i created inside the outer function")
    inner_function()
outer_function()
