'''Write a Python function that takes a list and returns a new list with distinct elements from the first list.

Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

def unique_List(numbers):
    unique_numbers = []
    for x in numbers:
        if x not in unique_numbers:
            unique_numbers.append(x)
    return unique_numbers
print(unique_List([1,2,3,3,3,3,4,5]))
