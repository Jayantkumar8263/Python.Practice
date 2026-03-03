""" Write a Python program to calculate a dog's age in dog years.

Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years."""

age = int(input("Enter your dog's age in human years: "))
if age < 2:
    print(age * 10.5)
else:
    print(2*10.5 + (age-2)*4)