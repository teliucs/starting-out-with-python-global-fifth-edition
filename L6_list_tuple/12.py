# 12. Prime Number Generation
# A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and 
# itself. A positive integer greater than 1 is composite if it is not prime. Write a program that
# asks the user to enter an integer greater than 1, then displays all of the prime numbers that 
# are less than or equal to the number entered. The program should work as follows:
    # • Once the user has entered a number, the program should populate a list with all of the 
        # integers from 2 up through the value entered.
    # • The program should then use a loop to step through the list. The loop should pass each 
        # element to a function that displays whether the element is a prime number, or a composite number.
        

def main():
    number, integers_list = scrape_integers()
    prime, divisors = is_prime(number, integers_list)
    if prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT prime, because its divisors are: {divisors}.")


def scrape_integers():
    n = int(input("Enter a number greater than '1': "))
    while n < 2:
        print("Ehi, I said you to enter an integer greater than '1'.")
        n = int(input("Enter a number greater than '1': "))
    
    list = [i for i in range(2, n)]
    return n, list


def is_prime(n, list):
    divisors = []
    prime = True
    
    for i in range(len(list)):
        if n % list[i] == 0:
            divisors.append(list[i])
            prime = False
            
    return prime, divisors
        


if __name__ == '__main__':
    main()