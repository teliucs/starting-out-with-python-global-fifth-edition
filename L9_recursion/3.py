# 3. Recursive Lines
# Write a recursive function that accepts an integer argument, n. The function should display 
# n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line 
# showing 2 asterisks, up to the nth line which shows n asterisks.


def main():

    ast="*"
    num=1
    
    lines = int(input("How many end of asterisks: "))
        
    print_asterisk(ast, num, lines)
    
# define function.
# here is the algorithm:
# if end>num >>>> print "*" nth times. (which is num in our case)
    # for example: for num=1: print "*" 1 times and go to second line (num=2)
    # then for num=2: print "*" 2 times and go to third line etc. etc.
    # and return same function with num increased by 1 for next line (num+1)th line

# if end==num >>>> print "*" (end)th time. (final line) and do not
# return anything.
def print_asterisk(ast, num, end):
    if end > num:
        print(ast * num) # remember you can multiply the string.
        num += 1
        return print_asterisk(ast, num, end)
    elif end == num:
        print(ast * num)


if __name__ == '__main__':
    main()