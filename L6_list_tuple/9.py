# 9. Population Data
# If you have downloaded the source code you will find a file named USPopulation.txt
# in the Chapter 07 folder. The file contains the midyear population of the United States, in
# thousands, during the years 1950 through 1990. The first line in the file contains the population
# for 1950, the second line contains the population for 1951, and so forth.
# Write a program that reads the file’s contents into a list. The program should display the
# following data:
# • The average annual change in population during the time period
# • The year with the greatest increase in population during the time period
# • The year with the smallest increase in population during the time period


def main():
    try:
        us_pop = get_population()
        annual_change(us_pop)
    except IOError:
        print("No such file or directory")


def get_population():
    infile = open("Esercizi/L6_list_tuple/9_USPopulation.txt", "r")
    pop_list = infile.readlines()
    infile.close()
    
    index = 0
    while index < len(pop_list):
        pop_list[index] = int(pop_list[index].rstrip("\n"))
        index += 1
        
    return pop_list


def annual_change(pop_list):
    ann_change = [0] * (len(pop_list)-1)
    
    for index in range(len(ann_change)):
        ann_change[index] = pop_list[index+1] - pop_list[index]
 
    
    total = 0
    for num in ann_change:
        total += num
    average = total / len(ann_change)
    print("The average annual change in population during the time period is", \
          format(average, ",.2f"))
    
    print("The year with the greatest increase is", str(ann_change.index(max(ann_change)) + 1951) +
           " with an increase of", str(max(ann_change)))
    print("The year with the smallest increase is", str(ann_change.index(min(ann_change)) + 1951) +
           " with an increase of", str(min(ann_change)))


if __name__ == '__main__':
    main()