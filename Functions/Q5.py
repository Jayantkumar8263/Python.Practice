"""Write a Python function to check whether a number falls within a given range."""
def check_range(num, start, end):
    if num in range(start, end):
        print(f"{num} is in the range between {start} and {end}")
    else:
        print(f"{num} is not in the range between {start} and {end}")
check_range(5, 1, 10)