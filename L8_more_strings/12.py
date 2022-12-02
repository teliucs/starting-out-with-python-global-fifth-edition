# 12. Pig Latin
# Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In
# one version, to convert a word to Pig Latin, you remove the first letter and place that letter
# at the end of the word. Then, you append the string “ay” to the word. Here is an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

import time

def main():
    word = input("Type here a sentence words are run together, but the first character of each word is uppercase:\n")
    print("Pig Latining the word...")
    time.sleep(2.5)
    print(pig_latin(word))


def pig_latin(s):
    new = ''
    list_word = s.split()
    for i in range(len(list)):
        list[i] = list[:]
    


if __name__ == '__main__':
    main()