# 8. Sentence Capitalizer
# Write a program with a function that accepts a string as an argument and returns a copy 
# of the string with the first character of each sentence capitalized. For instance, if the argument
# is “hello. my name is Joe. what is your name?” the function should return the string 
# “Hello. My name is Joe. What is your name?” The program should let the user enter 
# a string and then pass it to the function. The modified string should be displayed.


def main():
    stringa = get_string()
    print(convert(stringa))


def get_string():
    return input("Type a string here:\n")


def convert(sentence):
    sentence_list = sentence.split(' ')
    new_sentence = ''
    for i in sentence_list:
        n = i[0].upper()
        new = i.replace(i[0], n)
        space = ' '
        new_sentence += new + space
    return new_sentence

if __name__ == '__main__':
    main()