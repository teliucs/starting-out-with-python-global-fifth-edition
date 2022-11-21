# 1 Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

CALORIES_PER_MINUTE = 4.2

print("---- Calories burnt ----")
print("Minutes\tCalories")

for i in range(10, 31, 5):
    calories = CALORIES_PER_MINUTE * i
    print(f"{i}\t{calories:.0f}")