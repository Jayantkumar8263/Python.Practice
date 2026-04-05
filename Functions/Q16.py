"""Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included)."""

def squares():
    list= []
    for i in range(1, 31):
        list.append(i**2)
    print(list)
squares()