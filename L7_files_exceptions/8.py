# 8. Random Number File Reader
# This exercise assumes you have completed Programming Exercise 7, Random Number File
# Writer. Write another program that reads the random numbers from the file, displays the
# numbers, then displays the following data:
# • The total of the numbers
# • The number of random numbers read from the file

def main():
    print("Here are your statistics from '7_generator.txt': ")
    reader()

def reader():
    string = ''
    total = 0
    counter = 0
    
    opener = open('7_generator.txt', 'r')
    for i in opener:
        i = i.rstrip('\n')        
        string += str(i) + ", "
        total += int(i)
        counter += 1
    opener.close()
    print(f" - number in file are: {string}")
    print(f" - total is {total}")
    print(f" - the numbers are: {counter}.")


if __name__ == '__main__':
    main()