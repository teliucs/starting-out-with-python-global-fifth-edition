# 9. Vowels and Consonants
# Write a program with a function that accepts a string as an argument and returns the
# number of vowels that the string contains. The application should have another function
# that accepts a string as an argument and returns the number of consonants that the string
# contains. The application should let the user enter a string, and should display the number
# of vowels and the number of consonants it contains.


def main():
    string = input("Enter here a string:\n")
    print(f"In {string} the number of vowels are {count_vowels(string)} and consonant are {count_consonants(string)}.")


def count_vowels(string):
    vowels = "aAeEiIoOuU"
    count = 0
    
    for i in string:
        if i in vowels:
            count += 1
    return count


def count_consonants(string):
    consonants = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"
    count = 0
    
    for i in string:
        if i in consonants:
            count += 1
    return count


if __name__ == '__main__':
    main()