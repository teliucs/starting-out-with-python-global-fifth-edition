# 1 Write a program that asks the user to enter an integer. The program should display "Positive" if the number is greater than 0, "Negative" if the number is less than 0, and "Zero" if the number is equal to 0. The program should then display "Even" if the number is even, and "Odd" if the number is odd.

number = int(input("Type here an integer: "))

if number > 0:
    print("Your integer is positive ", end='')
if number == 0:
    print("Your integer is zero ", end='')
if number < 0:
    print("Your integer is negative ", end='')

if number % 2 == 0:
    print("and it is also even.")
else:
    print("and it is also odd.")