# 1 Python allows you to repeat a string by multiplying it by an integer, for example, 'Hi' * 3 will give 'HiHiHi'. Pretend that this feature does not exist, and instead write a function named repeat that accepts a string and an integer as arguments. The function should return a string of the original string repeated the specified number of times, for example, repeat('Hi', 3) should return 'HiHiHi'.

def repeat(str, int):
    newstr = ""
    for i in range(int):
        newstr += str
    print(newstr)

def main():
    string = input("Enter the string: ")
    integer = int(input("How many times do you want to repeat it? "))
    repeat(string, integer)

main()