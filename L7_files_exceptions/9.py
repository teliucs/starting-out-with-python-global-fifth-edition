# 9. Exception Handing
# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# • It should handle any IOError exceptions that are raised when the file is opened and data
    # is read from it.
# • It should handle any ValueError exceptions that are raised when the items that are read
    # from the file are converted to a number.

def main():
    # avarage = read()
    # print(f"The avarage of your file is {avarage:,.1f}.")
    read()

def read():
    avarage = 0
    count = 0
    total = 0    
    try:
        opener = open('5_&_6.txt', 'r')
    except IOError:
        print('IOError')
    except ValueError:
        print('ValueError')
    else:
        for i in opener:
            total += int(i)
            count += 1
        opener.close()
        print(total)
        print(count)


if __name__ == '__main__':
    main()