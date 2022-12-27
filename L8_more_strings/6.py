# 6. Average Number of Words
# If you have downloaded the source code from the Computer Science Portal you will find 
# a file named text.txt in the Chapter 08 folder. The text that is in the file is stored as one 
# sentence per line. Write a program that reads the file’s contents and calculates the average 
# number of words per sentence.


def main():
    print(f"The average number of words per sentence is [{read_file():.0f}].")


def read_file():
    total = 0
    lines = 0
    with open("L8_more_strings\\6_text.txt", 'r') as f:
        for line in f:
            words = line.split()
            total += len(words)
            lines += 1
    return total / lines


if __name__ == '__main__':
    main()