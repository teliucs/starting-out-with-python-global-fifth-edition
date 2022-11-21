# 6 In mathematics, the notation  n!  represents the factorial of the nonnegative integer  n . The factorial of  n  is the product of all the nonnegative integers from  1  to  n . For example,  7!=1×2×3×4×5×6×7=5,040 . As a base case, the factorial of  0  is  1 .

# Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial of that number. Display the factorial.

print("I can calculate the factorial of a non negative integer number.")

n = int(input("What is your n? "))
factorial = 1

while n < 0:
  print("Enter a valid number!")
  number = int(input("Enter a non negative integer: "))

if n > 0:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")    

if n == 0:
    print("The factioral of 0 is 1.")