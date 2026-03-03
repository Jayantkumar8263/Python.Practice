"""Write a Python program to convert temperatures to and from Celsius and Fahrenheit."""

tem = int(input("Enter the number :"))
i = input("enter the mode : ")

if i.upper() == "C": 
    result = int(round((9 * tem) / 5 + 32))

elif i.upper() == "F": 
    result = int(round((tem - 32) * 5 / 9))

else: 
    print(f" {i} is not defined")

print(f' for {tem} the conversion is {result}')