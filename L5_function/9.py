# Write a program that generates 100 random numbers
# and keeps a count of how many of those random numbers are even, and how many of
# them are odd.

import random

def odd_even(number):
    global even
    global odd
    even = 0
    odd = 0
    for i in range(number):
        int = random.randint(1, 100)
        if int % 2 == 0:
            even += 1
        else:
            odd += 1
    
def main():
    number = int(input("How mnay integers do you want to generate? "))
    odd_even(number)
    print(f"Even: {even}")
    print(f"Odd: {odd}")
    
main()