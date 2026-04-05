"""Write a Python program to execute a string containing Python code."""

code1 = 'print("Hello, World!")'
exec(code1)

code2 = """
def greet(name):
    return f"Hello, {name}!"
print(greet("joy"))
"""
exec(code2)