"""Write a Python program to find if a given string starts with a given character using Lambda.

Sample Output:
True
False"""

y = lambda x : True if x.startswith('a') else False
print(y('apple'))
print(y('banana'))
