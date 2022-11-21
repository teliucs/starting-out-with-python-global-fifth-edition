# 3 Write a program that asks the user for a month as a number between 1 and 12. The program should display a message indicating whether the month is in the first quarter, the second quarter, the third quarter, or the fourth quarter of the year. Following are the guidelines:

# If the user enters a number between 1 and 3, the month is in the first quarter.
# If the user enters a number between 4 and 6, the month is in the second quarter.
# If the user enters a number between 7 and 9, the month is in the third quarter.
# If the user enters a number between 10 and 12, the month is in the fourth quarter.
# If the number is not between 1 and 12, the program should display an error.

month = int(input("Type here a number of a month: "))

if month > 0 and month < 13:
    if month > 0 and month < 4:
        print("Your choice is in the first quarter.")
    elif month > 3 and month < 7:
        print("Your choice is in the second quarter.")
    elif month > 6 and month < 10:
        print("Your choice is in the third quarter.")
    else: #month > 9 and month < 13:
        print("Your choice is in the fourth quarter.")
else:
    print("You have to choose between 1 and 12")