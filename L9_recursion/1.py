# 1. Recursive Printing
# Design a recursive function that accepts an integer argument, n, and prints the numbers 1 
# up through n.


def main():
    number = 5
    recursion(number)
    

def recursion(n):
    if n == 1:
        print(1)
    else:
        print(1)
        return recursion(n-1)
    

if __name__ == '__main__':
    main()