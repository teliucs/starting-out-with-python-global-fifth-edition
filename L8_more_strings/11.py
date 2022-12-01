# 11. Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together,
# but the first character of each word is uppercase. Convert the sentence to a string in which
# the words are separated by spaces, and only the first word starts with an uppercase letter. For
# example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
# the roses.”


def main():
    word = input("Type here a sentence words are run together, but the first character of each word is uppercase:\n")
    print("Slicing the word...")
    print(slice_word(word))


def slice_word(string):
    pass


if __name__ == '__main__':
    main()