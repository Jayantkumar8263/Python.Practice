"""Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)."""

for i in range(1500, 2700):
    if i % 5 == 0:
        print(f" {i} is devisible by 5.")

    elif i % 7 == 0:
        print(f" {i} is devisible by 7.")
    
    else : 
        print(f" {i} is not devisible by 5 or 7.")