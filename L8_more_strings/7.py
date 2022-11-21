# 7. Character Analysis
# If you have downloaded the source code you will find a file named text.txt in the Chapter 08
# folder. Write a program that reads the file’s contents and determines the following:
# • The number of uppercase letters in the file
# • The number of lowercase letters in the file
# • The number of digits in the file
# • The number of whitespace characters in the file.


def main():
    text_file = get_data()
    upper, lower, digit, white_space = analize_data(text_file)
    print("Analizing data....")
    print('--------------------')
    print(f"Number of UPPER: {upper}")
    print(f"Number of LOWER: {lower}")
    print(f"Number of DIGITS: {digit}")
    print(f"Number of WHITE SPACES: {white_space}")


def get_data():
    try:
        with open('Esercizi/L8_more_strings/6_text.txt', 'r') as f:
            list = f.readlines()
            for i in range(len(list)):
                list[i] = list[i].rstrip('\n')
        return list
    except IOError:
        print("File does not exist in that directory.")
    

def analize_data(list):
    upper = 0
    lower = 0
    digit = 0
    white_space = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j].isupper():
                upper += 1
            if list[i][j].islower():
                lower += 1
            if list[i][j].isdigit():
                digit += 1
            if list[i][j] == ' ':
                white_space += 1
    return upper, lower, digit, white_space
            


if __name__ == '__main__':
    main()