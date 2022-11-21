# 2. Recursive Multiplication
# Design a recursive function that accepts two arguments into the parameters x and y. The 
# function should return the value of x times y. Remember, multiplication can be performed 
# as repeated addition as follows:
    # 7 * 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
# (To keep the function simple, assume x and y will always hold positive nonzero integers.)


def main():
    number_1 = int(input("Type a positive nonzero integer: "))
    number_2 = int(input("Type a positive nonzero integer: "))
    print(f"The moltiplication of {number_2} by {number_1} times is {multiply(number_1, number_2)}.")


def multiply(x, y):
    if x == 1:
        return y
    if x > 1:
        return y + multiply(x - 1, y)


if __name__ == '__main__':
    main()