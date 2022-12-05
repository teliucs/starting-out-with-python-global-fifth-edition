# 3. Recursive Lines
# Write a recursive function that accepts an integer argument, n. The function should display 
# n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line 
# showing 2 asterisks, up to the nth line which shows n asterisks.


def main():

    ast = "*"
    num = 1
    
    lines = int(input("How many end of asterisks: "))
        
    print_asterisk(ast, num, lines)
    
    
def print_asterisk(ast, num, end):
    if end > num:
        print(ast * num)
        num += 1
        return print_asterisk(ast, num, end)
    elif end == num:
        print(ast * num)


if __name__ == '__main__':
    main()