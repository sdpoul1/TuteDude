Task 1: Calculate Factorial Using a Function 
def factorial(n):
  if n==0:
    return 1
  return n * factorial(n-1)

num=6
print(f"Factorial of {num} is {factorial(num)}")



Task 2: Using the Math Module for Calculations
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)

Displays the calculated results.

import math
num = int(input("Enter the number : ")
print(f"Square root of {num} is : {math.sqrt(num)}")
print(f"Natural log of {num} is : {math.log(num)}")
sineOfNumber = math.sin(num)
sineInRadians = math.radians(sineOfNumber)
print(f"Sine of the number(in radians) :{sinInRadians}")
  

