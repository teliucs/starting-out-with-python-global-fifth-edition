# 2. File Head Display
# Write a program that asks the user for the name of a file. The program should display only
# the first five lines of the file’s contents. If the file contains less than five lines, it should
# display the file’s entire contents.

def main():
    lines = couting_lines()
    show_lines(lines)
    
def couting_lines():
    file = open(r'D:\Lorenzo\UniPG\I\Programming\Esercizi\Files\1_numbers.txt', 'r')
    counter = 0
    for i in file:
        counter += 1
    file.close
    return counter

def show_lines(lines):
    five_lines = ''
    file = open(r'D:\Lorenzo\UniPG\I\Programming\Esercizi\Files\1_numbers.txt', 'r')
    if lines >= 5:
        for i in range(5):
            single_line = file.readline()
            five_lines += single_line
    else:
        entire_file = file.read()
        five_lines += entire_file
    file.close
    print(five_lines)

if __name__ == '__main__':
    main()