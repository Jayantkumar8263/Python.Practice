'''Write a Python function that checks whether a passed string is a palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print(is_palindrome("madam"))
print(is_palindrome("nurses run"))