# Write a program that asks the user to enter five test scores. The program should display a
# letter grade for each score and the average test score. Write the following functions in the
# program:
# • calc_average. This function should accept five test scores as arguments and return the
# average of the scores.
# • determine_grade. This function should accept a test score as an argument and return
# a letter grade for the score based on the following grading scale:
# Score Letter Grade
# 90–100 A
# 80–89 B
# 70–79 C
# 60–69 D
# Below 60 F

def calc_avarage(first, second, third, fourth, fifth):
    return ((first + second + third + fourth + fifth) / 5)

def determine_grade(avarage):
    if avarage >= 90:
        return "A"
    if avarage >= 80 and avarage < 90:
        return "B"
    if avarage >= 70 and avarage < 80:
        return "C"
    if avarage >= 60 and avarage < 70:
        return "D"
    if avarage < 60:
        return "F"

def main():
    first = int(input("First mark: "))
    second = int(input("Second mark: "))
    third = int(input("Third mark: "))
    fourth = int(input("Fourth mark: "))
    fifth = int(input("Fifth mark: "))
    
    avarage = calc_avarage(first, second, third, fourth, fifth)
    print(avarage)
    print(f"Your grade is: {determine_grade(avarage)}")
    
main()