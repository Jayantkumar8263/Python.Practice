"""Write a Python program to sort a list of tuples using Lambda function."""

t = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
t.sort(key=lambda x: x[1])
print(t)