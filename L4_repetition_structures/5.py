# 5 Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered, the program should display the maxmimum value in the sequence.

print("This program calculates the maximum value among the ones you give.")
print("Type in a negative integer to stop.")

number = int(input("Enter here the integer number: "))
max = number

while number >= 0:
    number = int(input("Enter here the integer number: "))
    
    if number > max:
        max = number
        
print(f"The maximum value of the sequence is: {max}")
