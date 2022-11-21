# 5 A class has two tests worth 25 points each along with a main exam worth 50 points. For a student to pass the class, they must obtain at least 25 points in the main exam and an overall score of at least 50 points. If a student's total score is less than 50 or they obtain less than 25 points in the main exam, they receive a grade of "Fail". Otherwise, their grade is as follows:

# If they get more than 80, they get a "Distinction" grade.
# If they get less than 80 but more than 60, they get a "Credit" grade.
# If they get less than 60, they get a "Pass" grade.
# Write a program that prompts the user to enter their points for both tests and the main exam and converts the values to integers. The program should first check if the points entered for the tests and main exam are valid. If any of the test scores are not between 0 and 25 or the main exam score is not between 0 and 50, the program should display an error message. Otherwise, the program should display the total points and the grade.

test_1 = int(input("Your points in the first test: "))
test_2 = int(input("Your points in the second test: "))
main_test = int(input("Your points in the main test: "))

total_score = test_1 + test_2 + main_test

if test_1 <= 25 and test_2 <= 25 and main_test <= 50:
    if test_1 >= 0 and test_2 >= 0 and main_test >= 0:
        print(f"Your total score is: {total_score}.\nYour grade is: ")
        if total_score < 50 or main_test < 25:
            print("FAIL")
        elif total_score < 60:
            print("PASS")
        elif total_score < 80:
            print("CREDIT")
        else:
            print("DISTINCTION")
else:
    print("Type in real values.")
