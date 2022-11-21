# 7. Random Number File Writer
# Write a program that writes a series of random numbers to a file. Each random number
# should be in the range of 1 through 500. The application should let the user specify how
# many random numbers the file will hold.

import random

def main():
    print("Random numbers genetor from 1 throught 500.")
    writer()
    print("You can find your number in '7_generator.txt' file.")

def writer():
    opener = open('7_generator.txt', 'w')
    how_many = int(input('How many integers do you want to generate?\n'))
    for i in range(how_many):
        number = random.randrange(1, 501)
        opener.write(str(number))
        opener.write('\n')
    opener.close()


if __name__ == '__main__':
    main()