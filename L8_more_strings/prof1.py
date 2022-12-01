# 1 Prompt the user to enter a string sentence and a character letter. Create a list entries of boolean values with the same length as the string entered by the user and such that the  i -th value of entries is True if and only if the  i -th character of sentence is equal to letter.


def main():
    sentence = input("Type here your sentence:\n")
    letter = input("Which letter do you want to check?\n")
    print(check_sentence(sentence, letter))


def check_sentence(string, letter):
  n = len(string)
  entries = [False] * n
  for i in range(n):
    entries[i] = string[i] == letter
  return entries
        


if __name__ == '__main__':
    main()