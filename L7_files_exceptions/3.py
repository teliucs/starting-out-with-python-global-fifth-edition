# 3. Line Numbers
# Write a program that asks the user for the name of a file. The program should display the
# contents of the file with each line preceded with a line number followed by a colon. The
# line numbering should start at 1.

def main():
    show_line()

def show_line():
    filename = input('Enter a filename: ')
    infile = open(filename, 'r')
    
    counter = 1
    line = infile.readline()
    while line != '':
        print(str(counter) + ": ", end='')
        line = line.rstrip('\n')
        print(line)
        counter += 1
        line = infile.readline()

    infile.close()
 

if __name__ == '__main__':
    main()