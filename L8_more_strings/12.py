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
    print(pig_latin(word.upper()))


def pig_latin(s):
    list_word = s.split()
    for i, word in enumerate(list_word):
        for _, _ in enumerate(list_word):
            list_word[i] = word[1:] + word[0] + "AY"
    
    return ' '.join(list_word)
    


if __name__ == '__main__':
    main()