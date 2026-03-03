"""Write a Python program to find the median of three values.

Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0 """

num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    median = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    median = num2
else:
    median = num3

print("The median is", median)
