# 4 Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one cent the first day, two cents the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the period. The output should be displayed in a euro amount, not the number of cents.

salary = 0.01
total = 0.01

days = int(input("After how many days do you want to see your salary? "))
print(f"How many money will you have after {days} days:")

print("Days\t|   Money")
print("---------------------")
print(f"Day 1\t|   0.01€")


for i in range(2, days + 1):
    salary = salary * 2
    total += salary
    print(f"Day {i}\t|   {salary:.2f}€")
    
print("---------------------")
print(f"Your total pay is {total:.2f}€.")
