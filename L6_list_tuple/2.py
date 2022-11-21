# 2. Lottery Number Generator
    # Design a program that generates a seven-digit lottery number. The program should generate
    # seven random numbers, each in the range of 0 through 9, and assign each number to a
    # list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
    # displays the contents of the list.
 
import random
   
def main():
    numbers_list = generate_numbers()
    display(numbers_list)

def generate_numbers():
    list = []
    for i in range(7):
        list.append(random.randint(0, 9))
    return list

def display(list):
    print("The 7 random numbers are...\n...\n...")
    for i in range(len(list)):
        print(list[i], end='\t')

if __name__ == '__main__':
    main()