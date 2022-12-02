# 5 Write a recursive function to decide whether a string is palindrome.


def main():
    stringa = input("Type here a string:\n")
    print(check_palindrome(stringa))
    

def check_palindrome(stringa):
    if len(stringa) > 2:
        return stringa[0] == stringa[len(stringa)-1] and check_palindrome(stringa[1:len(stringa)-1])
    else:
        return stringa[0] == stringa[len(stringa)-1]


if __name__ == '__main__':
    main()