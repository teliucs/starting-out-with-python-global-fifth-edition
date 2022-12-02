# 3 Design a recursive function that accepts an integer argument 'n'
# and prints every second number from 'n' down to a minimum of  0 .
# Assume that 'n'  is always a positive integer.


def main():
    integer = int(input("Type here an integer: "))
    print_previous(integer)


def print_previous(num):
    if num > 0:
        print(num)
        print_previous(num - 2)
        

if __name__ == '__main__':
    main()