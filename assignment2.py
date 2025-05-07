Task 1: Check if a Number is Even or Odd

num = int(input("Enter a number:"))

if num//2 ==0:
	print(f"{num} is an even number")
else:
	print(f"{num} is an odd number")



Task 2: Sum of Integers from 1 to 50 Using a Loop

sum = 0
for i in range(1, 51):  # Loop from 1 to 50 (inclusive)
    sum = sum + i

print(f"The sum of numbers from 1 to 50 is: {sum}")
