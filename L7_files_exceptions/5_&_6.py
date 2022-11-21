# 5. Sum of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s
# disk. Write a program that reads all of the numbers stored in the file, calculates
# their total and their avarage.

def main():
    total = sum()
    av = avarage(total)
    
    print(f" The sum of your file is: {total:,}.")
    print(f" The avarage of your file is: {av:,.1f}.")

def sum():
    opener = open('5_&_6.txt', 'r')
    sum = 0
    for i in opener:
        sum += int(i)
    return sum
    
def avarage(sum):
    opener = open('5_&_6.txt', 'r')
    counter = 0
    for i in opener:
        counter += 1
    avarage = sum / counter
    return avarage

if __name__ == '__main__':
    main()