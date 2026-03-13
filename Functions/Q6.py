"""Write a Python function that accepts a string and counts the number of upper and lower case letters.

Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""

def count_case(string):
    upper_case = 0
    lower_case = 0
    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    print(f"No. of Upper case characters : {upper_case}")
    print(f"No. of Lower case Characters : {lower_case}")
count_case('The quick Brow Fox')