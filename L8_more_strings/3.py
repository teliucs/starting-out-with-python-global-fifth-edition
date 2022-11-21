# 3. Date Printer
# Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. 
# It should print the date in the format March 12, 2018.

def main():
    date = get_date()
    
    literal_date = convert(date)
    
    print("The date is below.")
    print(literal_date)
    
def get_date():
    date=input("Enter the date as mm/dd/yyyy: ")
    return date


def convert(date):
    date_list = date.split("/")
    
    months = ["January", "February", "March", "April", "May", \
            "June", "July", "August", "September", "October", \
            "November", "December"]
    
    new_date = str(months[int(date_list[0])-1]) + " " + str(date_list[1]) + "," + " " + str(date_list[2])

    return new_date


if __name__ == '__main__':
    main()