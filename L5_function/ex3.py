# Dr. Kimura teaches an introductory statistics class and has asked you to write a program that he can use in class to simulate the rolling of dice. The program should randomly generate two numbers in the range of 1 through 6 and display them. In your interview with Dr. Kimura, you learn that he would like to use the program to simulate several rolls of the dice, one after the other.

# Algorithm:

    # While the user wants to roll the dice:
        # Display a random number in the range of 1 through 6
        # Display another random number in the range of 1 through 6
        # Ask the user if he or she wants to roll the dice again
import random

num1 = 0
num2 = 0
       
def main():
    start()
    roll_dice(num1, num2)
    choice = input("If you would like to roll again type 'y': ")
    while choice == 'y':
        roll_dice(num1, num2)
        choice = input("Would you like to roll again? y\\N: ")

def start():
    print("Ehi everybody, lets roll some dices...")

def roll_dice(num1, num2):
    print('Rolling the dice . . .') 
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print(f"You rolled: {num1}, {num2}")

main()