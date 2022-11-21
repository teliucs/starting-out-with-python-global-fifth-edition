# 2 Write a program that asks the user to enter the number of times they have run around a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps. When the loop finishes, the program should display the time of their fastest lap, the time of their slowest lap, and their average lap time.

laps = int(input("How many laps did you run? "))
time = []
for i in range(laps):
    single = int(input(f"What is the time in seconds of the lap number {i+1}: "))
    time.append(single)

fastest = max(time)
slowest = min(time)
avarage = sum(time) / (len(time))

print(f"Fastest: {fastest}, slowest: {slowest} and tbe avarage is {avarage:.0f}")