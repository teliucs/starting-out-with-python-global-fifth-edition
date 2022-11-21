# 6 A prime number is a number that is only evenly divisible by itself and 1. For example, the number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6. Write a Boolean function named is_prime which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise. Use the function in a program that prompts the user to enter a number then displays a message indicating whether the number is prime.

# import math

def isPrime(number):
    prime = True
    for i in range(2, number):         # range(2,math.floor(math.sqrt(num)+1))
        if (number % i) == 0:
            prime = False
        break
    return prime

def main():
    print("I can say you if an integer is a prime or not.")
    number = int(input("Enter an integer number greater than 1 (0 to end): "))
    prime = isPrime(number)
    while number != 0:
        if prime:
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")
        number = int(input("Enter an integer number greater than 1 (0 to end): "))
        prime = isPrime(number)

main()