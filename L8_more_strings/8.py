# 8. Sentence Capitalizer
# Write a program with a function that accepts a string as an argument and returns a copy
# of the string with the first character of each sentence capitalized. For instance, if the argument
# is “hello. my name is Joe. what is your name?” the function should return the string
# “Hello. My name is Joe. What is your name?” The program should let the user enter
# a string and then pass it to the function. The modified string should be displayed.


def main():
    sentence = input("Type here a string:\n")
    print(capitalized(sentence))


def capitalized(string):
    string = string[0].upper() + string[1:]
    
    for i in range(0, len(string)-1):
        if string[i] == '.':
            string = string[:i+2] + string[i+2].upper() + string[i+3:]
    
    return string


if __name__ == '__main__':
    main()