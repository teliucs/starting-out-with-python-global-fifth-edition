# 7. Recursive Power Method
# Design a function that uses recursion to raise a number to a power. The function should
# accept two arguments: the number to be raised, and the exponent. Assume the exponent is
# a nonnegative integer.


def main():
    number = int(input("Type here an integer, it can be positive or negative: "))
    exponent = int(input("Type here the exponent: "))
    
    print(f"The number {number} to the power of {exponent} is: {power(number, exponent)}.")
    

def power(n, e):
    if e <= 1:
        return 1
    else:
        return n * power(n, e -1)


if __name__ == '__main__':
    main()