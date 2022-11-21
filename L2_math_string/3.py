# 3 Write a program that asks the user to enter the radius of a circle. The program should calculate
# and display the area and circumference of the circle using  πr2  for the area and  2πr  for the circumference.

# NOTE: You can write import math as the first program instruction and then math.pi to obtain the value of  π .

import math

radius = float(input("Put here the radius: "))

circumference = 2 * radius * math.pi

area = math.pi * (radius ** 2)

print(circumference)
print(area)