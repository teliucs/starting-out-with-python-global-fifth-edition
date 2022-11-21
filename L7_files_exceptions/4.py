# 4. Item Counter
# Assume a file containing a series of names (as strings) is named names.txt and exists on
# the computer’s disk. Write a program that displays the number of names that are stored
# in the file. (Hint: Open the file and read every string stored in it. Use a variable to keep a
# count of the number of items that are read from the file.)

def main():
    print("Hi I can read a life and count how many names are in it.")
    choice = input("Do y want to check how many names are in 'names.txt'? (Y/n)\n")
    if choice == 'y':
        print(counter())
    else:
        print("See you.")

def counter():
    opener = open('4_names.txt', 'r')
    counter = 0
    for i in opener:
        counter += 1
    return counter

if __name__ == '__main__':
    main()