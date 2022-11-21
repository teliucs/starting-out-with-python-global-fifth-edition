# 1. File Display
# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s
# disk. Write a program that displays all of the numbers in the file.

def main():
    write_numbers()
    read_numbers()
    
def write_numbers():
    file = open(r'D:\Lorenzo\UniPG\I\Programming\Esercizi\Files\1_numbers.txt', 'w')

    for i in range(10):
        file.write(str(i+1) + '\n')

    file.close

def read_numbers():
    file = open(r'D:\Lorenzo\UniPG\I\Programming\Esercizi\Files\1_numbers.txt', 'r')
    
    numbers = file.read()
    
    file.close

    print(numbers)

if __name__ == "__main__":
    main()