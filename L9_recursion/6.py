# 6. Sum of Numbers
# Design a function that accepts an integer argument and returns the sum of all the integers
# from 1 up to the number passed as an argument. For example, if 50 is passed as an argument,
# the function will return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.


def main():
    try:
        integer = int(input("Type here an integer, it can be positive or negative: "))
        print(f"The sum of the previous values of {integer} is: {get_previous_sum(integer)}.")
    except ValueError:
        print("You have to insert an integer.")
    

def get_previous_sum(n):
    if n > 0:
        return n + get_previous_sum(n - 1)
    elif n < 0:
        return n + get_previous_sum(n + 1)      # I added this to be able to handle negative numbers
    else:
        return 0
    


if __name__ == '__main__':
    main()