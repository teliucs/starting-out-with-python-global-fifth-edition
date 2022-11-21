# 1 A company has determined that its annual profit is typically 23 percent of total sales.
# Write a program that asks the user to enter the projected amount of total sales,
# then displays the profit that will be made from that amount.

annual_profit = 0.23
projected = int(input("What are yours projected amount of total sales? "))

real_profit = projected * annual_profit

print(f'Your annual profit is {real_profit:,.2f}€')