# 2 Prompt the user to enter a string code. Print all substrings of length three in code.


def main():
    sentence = input("Type here your sentence:\n")
    print(divide_string(sentence, 3))
    

def divide_string(string, length):
  n = len(string)
  for i in range(n):
    substring = string[i: i + length]
    if len(substring) == length:
      print(substring)


if __name__ == '__main__':
    main()