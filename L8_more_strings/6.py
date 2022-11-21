# 6. Average Number of Words
# If you have downloaded the source code from the Computer Science Portal you will find 
# a file named text.txt in the Chapter 08 folder. The text that is in the file is stored as one 
# sentence per line. Write a program that reads the file’s contents and calculates the average 
# number of words per sentence.


def main():
    text_file, num_list = read_file()
    print(text_file)
    print(f"The avarage number of words per sentence is: {compute_avarage(text_file, num_list):,.1f}.")


def read_file():
    with open('Esercizi/L8_more_strings/6_text.txt', 'r') as f:
        list = f.readlines()
        for i, _ in enumerate(f):
            pass
        for i in range(len(list)):
            list[i] = list[i].rstrip('\n')
    return list, i+1


def compute_avarage(list, num):
    total_words = num
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == ' ':
                total_words += 1
    return total_words / num


if __name__ == '__main__':
    main()