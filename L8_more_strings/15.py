# 15. Caesar Cipher
# A “Caesar Cipher” is a simple way of encrypting a message by replacing each letter with a 
# letter a certain number of spaces up the alphabet. For example, if shifting the message by 
# 13, an A would become an N, while an S would wrap around to the start of the alphabet 
# to become an F.
# Write a program that asks the user for a message (a string) and a shift amount (an integer).
# The values should be passed to a function that accepts a string and an integer as 
# arguments, and returns a string representing the original string encrypted by shifting the 
# letters by the integer. For example, a string of “BEWARE THE IDES OF MARCH” and 
# an integer of 13 should result in a string of “ORJNER GUR VQRF BS ZNEPU”.


def main():
    sentence = input('Type here a sentence:\n')
    integer = int(input("Integer: "))


def trasform_ceaser(string, n):
    dictionary = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'. 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


if __name__ == '__main__':
    main()