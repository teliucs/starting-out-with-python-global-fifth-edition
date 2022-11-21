# 8. Name Search
# If you have downloaded the source code you will find the following files in the Chapter 07 folder:
    # • GirlNames.txt This file contains a list of the 200 most popular names given to girls
        # born in the United States from the year 2000 through 2009.
    # • BoyNames.txt This file contains a list of the 200 most popular names given to boys
        # born in the United States from the year 2000 through 2009.
# Write a program that reads the contents of the two files into two separate lists. The user
# should be able to enter a boy’s name, a girl’s name, or both, and the application will display
# messages indicating whether the names were among the most popular.


def main():
    try:
        boys_list = get_boys()
        girls_list = get_girls()
        search_name(boys_list, girls_list)
    except IOError:
        print("No such file or directory")

        

def get_boys():
    with open('Esercizi/L6_list_tuple/8_BoysNames.txt', 'r') as f:
        for _ in f:
            boys.append(f.readline().rstrip('\n'))
    return boys


def get_girls():
    girls = []
    with open('Esercizi/L6_list_tuple/8_GirlsNames.txt', 'r') as f:
        for _ in f:
            girls.append(f.readline().rstrip('\n'))
    return girls


def search_name(b, g):
    name = input("Enter a name: ")
    if name in b or name in g:
        print(name, "is among the most popular names.")
    else:
        print(name, "is NOT found among the most popular names.")  


if __name__ == '__main__':
    main()