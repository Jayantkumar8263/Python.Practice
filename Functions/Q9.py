'''Write a Python program to print the even numbers from a given list.

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]'''

def even(number):
    even_numbers = []
    for i in number:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))