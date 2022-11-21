# 3 Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the centimeters of rainfall for that month. After all iterations, the program should display the number of months, the total centimeters of rainfall, and the average rainfall per month for the entire period.

years = int(input("How many years? "))
total = 0

for year in range(1, years + 1):
    for month in range(1, 13):
        single = float(input(f"Enter the rainfall for month {month} of year {year}: "))
        total += single

months = year * 12
print(f"{months} months, total: {total:.1f} and avarage {(total / months):.1f}")