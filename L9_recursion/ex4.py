# 4 Write a recursive function that accepts an integer argument,  'n' .
# The function should display 'n' lines of asterisks on the screen,
# with the first line showing 1 asterisk, the second line showing 2 asterisks,
# up to the nth line which shows  'n' asterisks.


def main():
    integer = int(input("Type here an integer: "))
    print_asterisks(integer)


def print_asterisks(num):
    ASTERISKS = '*'
    if num > 0:
        print_asterisks(num - 1)
        print(ASTERISKS * num)


if __name__ == '__main__':
    main()