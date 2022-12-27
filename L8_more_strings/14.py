# 14. Gas Prices
# In the student sample program files for this chapter, you will find a text file named
# GasPrices.txt. The file contains the weekly average prices for a gallon of gas in the
# United States, beginning on April 5th, 1993, and ending on August 26th, 2013. Figure 8-8
# shows an example of the first few lines of the file’s contents:

# Each line in the file contains the average price for a gallon of gas on a specific date. Each line
# is formatted in the following way:
    # MM-DD-YYYY:Price
# MM is the two-digit month, DD is the two-digit day, and YYYY is the four-digit year. Price is
# the average price per gallon of gas on the specified date.
# For this assignment, you are to write one or more programs that read the contents of the file
# and perform the following calculations:
# Average Price Per Year: Calculate the average price of gas per year, for each year in the file.
                        # (The file’s data starts in April of 1993, and it ends in August 2013. Use the data that is present for the years 1993 and 2013.)
# Average Price Per Month: Calculate the average price for each month in the file.
                        # Highest and Lowest Prices Per Year: For each year in the file, determine the date and amount for the lowest price, and the highest price.
# List of Prices, Lowest to Highest: Generate a text file that lists the dates and prices, sorted
                                    # from the lowest price to the highest.
# List of Prices, Highest to lowest: Generate a text file that lists the dates and prices, sorted
                                    # from the highest price to the lowest.
                                    
# You can write one program to perform all of these calculations, or you can write di#erent
# programs, one for each calculation.

import matplotlib.pyplot as plt

def main():
    date_list, price_lists = read_file()
    average_year_years, average_year_prices = average_price_per_year(date_list, price_lists)
    average_price_per_month(date_list, price_lists)
    show_graph(average_year_years, average_year_prices)


def read_file():
    with open('L8_more_strings\\14_GasPrice.txt', 'r') as f:
        f_list = f.readlines()
        date_list = []
        price_lists = []
        for line in f_list:
            date_list.append(line[0:10])
            price_lists.append(line[11:].rstrip('\n'))
    return date_list, price_lists


def average_price_per_year(dates, prices):
    year = ''
    counter = 0
    accumulator = 0
    average_year_years = []
    average_year_prices = []
    for index in range(len(dates)):
        if year == '':
            year = dates[index][6:10]
            accumulator += float(prices[index])
            counter += 1
        elif dates[index][6:10] == year:
                accumulator += float(prices[index])
                counter += 1
        else:
            average = accumulator / counter
            average_year_years.append(year)
            average_year_prices.append(average)
            year = dates[index][6:10]
            counter = 1
            accumulator = float(prices[index])
    print()
    print('Average Price Per Year')
    print('----------------------')
    print('Year\t\tPrice')
    print('----\t\t-----')
    for i in range(len(average_year_years)):
        print(f"{average_year_years[i]}\t--->\t{average_year_prices[i]:,.3f}")
    return average_year_years, average_year_prices


def average_price_per_month(dates, prices):
    month = ''
    year = ''
    counter = 0
    accumulator = 0
    average_price_months = []
    average_price_prices = []

    for index in range(len(dates)):
        if year == '':
            year = dates[index][6:10]
        elif month == '':
            month = dates[index][0:2]
        elif dates[index][0:2] == month and dates[index][6:10] == year:
            accumulator += float(prices[index])
            counter += 1
        else:
            average = accumulator / counter
            average_price_months.append(year + '-' + month)
            average_price_prices.append(average)
            counter = 1
            accumulator = float(prices[index])
            year = dates[index][6:10]
            month = dates[index][0:2]
    print()
    print('Average Price Per Month')
    print('-----------------------')
    print('Month\t\tPrice')
    print('-----\t\t-----')
    for index in range(len(average_price_months)):
        print(average_price_months[index],'----->\t',format(average_price_prices[index],',.3f'))


def show_graph(years, prices):
    """I have added a graph to show the change of price during the years"""
    plt.plot(years, prices, marker = 'o')
    plt.title('Gas price by Year')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()
    

if __name__ == '__main__':
    main()