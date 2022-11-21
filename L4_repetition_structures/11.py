# Write a program that uses nested loops to draw this pattern:

# *******
# ******
# *****
# ****
# ***
# **

line = int(input("How many lines do you want? "))

for line in range(line, 0, -1):
    for columns in range(line):
        print("*", end='')
    print()