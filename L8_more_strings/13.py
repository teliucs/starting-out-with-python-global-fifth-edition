# 13. PowerBall Lottery
# To play the PowerBall lottery, you buy a ticket that has five numbers in the range of 1–69, 
# and a “PowerBall” number in the range of 1–26. (You can pick the numbers yourself, or you 
# can let the ticket machine randomly pick them for you.) Then, on a specified date, a winning 
# set of numbers is randomly selected by a machine. If your first five numbers match the first 
# five winning numbers in any order, and your PowerBall number matches the winning PowerBall number, then you win the jackpot, which is a very large amount of money. If your 
# numbers match only some of the winning numbers, you win a lesser amount, depending on 
# how many of the winning numbers you have matched.
# In the student sample programs for this book, you will find a file named pbnumbers.txt, 
# containing the winning PowerBall numbers that were selected between February 3, 2010 
# and May 11, 2016 (the file contains 654 sets of winning numbers). Figure 8-7 shows an 
# example of the first few lines of the file’s contents. Each line in the file contains the set of six 
# numbers that were selected on a given date. The numbers are separated by a space, and the 
# last number in each line is the PowerBall number for that day. For example, the first line in 
# the file shows the numbers for February 3, 2010, which were 17, 22, 36, 37, 52, and the 
# PowerBall number 24.
# Write one or more programs that work with this file to perform the following:
# • Display the 10 most common numbers, ordered by frequency
# • Display the 10 least common numbers, ordered by frequency
# • Display the 10 most overdue numbers (numbers that haven’t been drawn in a long 
# time), ordered from most overdue to least overdue
# • Display the frequency of each number 1–69, and the frequency of each Powerball 


def unified_list(number_list):
    master_list = []
    for draw in number_list:
        draw_list = draw.split()
        master_list += draw_list
    return master_list, draw_list


def times_each_appears(a_list):
    counter = 0
    numbersfound = []
    timesfound = []
    
    # Iterate each number in the list.
    for number in a_list:
        if number not in numbersfound:
            # Setup a counter to check how many times a number is seen.
            counter = 0
        
            # Check how many times the number is in this list.
            for searchnumber in a_list:
            
                # If the number is found, add + 1 to the counter.
                if number == searchnumber:
                    counter += 1
       
        if number not in numbersfound:
            numbersfound.append(number)
            timesfound.append(counter)
    return numbersfound,timesfound

    
def top10common(times,numbers):
    counter = 0
    index = 0
    top10times= []
    top10numbers = []
    for count in range(10):
        # Find the index number of the number that appears the most times.
        index = (times.index(max(times)))
        # Add this number to the list top10numbers
        top10numbers.append(numbers[index])
        # Add the number of times it was found to top10times
        top10times.append(times[index])
        # remove the number from the searchlist
        del numbers[index]
        del times[index]
    print('Most Common Numbers')
    print('-------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(top10numbers)):
        print(top10numbers[index] + '\t--->\t' + str(top10times[index]))
    print()
    

def bottom10common(times,numbers):
    counter = 0
    index = 0
    bottom10times = []
    bottom10numbers = []
    for count in range(10):
        # Find the index of the number that appear the least times.
        index = times.index(min(times))
        # Add this number to the bottom10numbers
        bottom10numbers.append(numbers[index])
        # Add the number of times it was found to the bottom10times list
        bottom10times.append(times[index])
        # remove the number from the lists times and numbers.
        del numbers[index]
        del times[index]
    print('Least Common Numbers')
    print('--------------------')
    print('Numbers\t\tTimes')
    print('-------\t\t-----')
    for index in range(len(bottom10numbers)):
        print(bottom10numbers[index] + '\t--->\t' + str(bottom10times[index]))
    print()
    

def top10overdue(times,numbers,original_list):
    count = 0
    overdue_list = []
    not_seen_list = []
    placeholder = ''
    for number in numbers:
        placeholder = number
        for specific_number in numbers:
            if specific_number == placeholder:
                count = 0
            else:
                count += 1
        overdue_list.append(number)
        not_seen_list.append(count)
    top10overdue =[]
    top10notseenfor =[]
    for count in range(10):
        index = not_seen_list.index(max(not_seen_list))
        top10notseenfor.append(not_seen_list[index])
        top10overdue.append(overdue_list[index])
        del not_seen_list[index]
        del overdue_list[index]
    print("Overdue List")
    print("------------")
    print()
    print('Number\t\tOverdue')
    print('------\t\t-------')
    for index in range(len(top10overdue)):
        print(top10overdue[index] + '\t--->\t' + str(top10notseenfor[index]))
    print()
    

def seperate_frequency(a_list):
    powerballs = []
    powerballs_count = []
    non_powerballs = []
    non_powerballs_count = []
    counter = 0
    number = 0
    for count in range(1,27):
        number = count
        # Split the list into draws
        for draw in a_list:
            draw_list = draw.split()
            if int(draw_list[5]) == number:
                counter += 1
        powerballs.append(number)
        powerballs_count.append(counter)
        counter = 0

    for count in range(1,70):
        number = count
        for draw in a_list:
            draw_list = draw.split()
            for searchnumber in draw_list:
                if int(searchnumber) == number:
                    counter += 1
        non_powerballs.append(number)
        non_powerballs_count.append(counter)
        counter = 0
        
    print('Powerballs Frequency')
    print('--------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(powerballs)):
        print(str(powerballs[index]) + '\t--->\t' + str(powerballs_count[index]))
    print()
    print('Regulars Frequency')
    print('------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(non_powerballs)):
        print(str(non_powerballs[index]) + '\t--->\t' + str(non_powerballs_count[index]))


def main():
    infile = open('pbnumbers.txt', 'r')
    
    contents = infile.readlines()
    
    for index in range(len(contents)):
        contents[index] = contents[index].rstrip('\n')
    master_list,split_list = unified_list(contents)
    numbersfound,timesfound = times_each_appears(master_list)
    
    top10common(timesfound,numbersfound)
    bottom10common(timesfound,numbersfound)
    top10overdue(timesfound,numbersfound,master_list)
    seperate_frequency(contents)
    infile.close()


if __name__ == '__main__':
    main()