# Write a program that predicts the approximate size of a population of organisms. The
# application should use text boxes to allow the user to enter the starting number of organisms,
# the average daily population increase (as a percentage), and the number of days the
# organisms will be left to multiply. For example, assume the user enters the following values:
# Starting number of organisms: 2
# Average daily increase: 30%
# Number of days to multiply: 10

def population(int, perc, days):
    total = int
    print(f"1\t| {total}")
    for i in range(1, days):
        total += (total * perc)
        print(f"{i + 1}\t| {total:.4f}")

def main():
    start = int(input("Starting number of organisms: "))
    increase = int(input("Average daily increase %: "))
    percentage = increase / 100
    days = int(input("Number of days to multiply: "))
    
    print("Day Approximate\t| Population")
    print("----------------------------")
    population(start, percentage, days)
    
main()