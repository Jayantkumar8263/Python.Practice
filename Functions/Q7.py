"""Write a Python function that accepts a string and counts the number of upper and lower case letters."""

s = "That Man Is Mad"

def letters(string): 
    upper_case = 0
    lower_case = 0
    
    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    print(f"The number of upper case letters are : {upper_case}")
    print(f"The number of lower case letters are : {lower_case}")
letters(s)