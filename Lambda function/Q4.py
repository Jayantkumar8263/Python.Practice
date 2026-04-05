"""Write a Python program to sort a list of dictionaries using Lambda function."""
d = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
d.sort(key = lambda x: x['age'])
print(f"Sorted list of dictionaries by age: {d}")
