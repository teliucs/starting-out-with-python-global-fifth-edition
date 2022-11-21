# 5. Alphabetic Telephone Number Translator
# Many companies use telephone numbers like 555-GET-FOOD so the number is easier for 
# their customers to remember. On a standard telephone, the alphabetic letters are mapped to 
# numbers in the following fashion:
# A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and O = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# W, X, Y, and Z = 9
# Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The application should display the telephone number with any 
# alphabetic characters that appeared in the original translated to their numeric equivalent. For example,
# if the user enters 555-GET-FOOD, the application should display 
    # 555-438-3663.
    

def main():
    number = get_number().upper()
    convert(number)


def get_number():
    num = input("Enter the number which you would like to convert.\n(format XXX-XXX-XXXX)\n")
    return num


def convert(phone):
    alpha  = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", \
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", \
               "W", "X", "Y", "Z"]
    number = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
    
    for index in range(len(phone)):
        if phone[index].isalpha():
            print(number[alpha.index(phone[index])], end="")
        else:
            print (phone[index], end = "")
        

if __name__ == '__main__':
    main()