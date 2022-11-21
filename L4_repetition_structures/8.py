# Write a program that displays a table of the Celsius temperatures 0 through 20 and their
# Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is:
# F = 9/5 C + 32
# where F is the Fahrenheit temperature, and C is the Celsius temperature. Your program
# must use a loop to display the table.

print("Celsius\t| Fahrenheit")
print("--------------------")

for c in range (1, 21, 1):
    print(f"{c}°C\t| {(9 / 5) * c + 32:.1f}°F")