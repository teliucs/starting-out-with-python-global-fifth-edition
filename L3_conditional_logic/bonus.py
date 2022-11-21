# Kathryn teaches a science class and her students are required to take three tests. She wants to write a program that her students can use to calculate their average test score. She also wants the program to congratulate the student enthusiastically if the average is greater than 95.

# Algorithm:

# Get the first test score
# Get the second test score
# Get the third test score
# Calculate the average
# Display the average
# If the average is greater than 95: Congratulate the user

first = int(input("Enter your first mark: "))
second = int(input("Enter your second mark: "))
third = int(input("Enter your third mark: "))

avarage = (first + second + third) / 3

print(f"Your avarage is {avarage:.0f}.")

if avarage > 95:
    print("Congratulations for your exellence result.")