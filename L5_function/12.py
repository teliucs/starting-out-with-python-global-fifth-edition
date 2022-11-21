# This exercise assumes that you have already written the is_prime function in Programming
# Exercise 17. Write another program that displays all of the prime numbers from 1 to 100.
# The program should have a loop that calls the is_prime function.

import math
from script1 import is_prime

def main():
    print("Number\t| Prime")
    print("--------------------")
    for n in range(1, 100 + 1):
        print(f"{n}\t| {is_prime(n)}")
        
main()