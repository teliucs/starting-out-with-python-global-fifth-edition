# 2 The area of a rectangle is the rectangle's length times its width. Write a program that asks for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same.

lenght1 = float(input("Lenght of the first rectangle: "))
widht1 = float(input("Widht of the first rectangle: "))
lenght2 = float(input("Lenght of the second rectangle: "))
width2 = float(input("Widht of the second rectangle: "))

area1 = lenght1 * widht1
area2 = lenght2 * width2

if area1 > area2:
    print("The area of the first rectangle is greater")
if area1 < area2:
    print("The area of the second rectangle is greater.")
if area1 == area2:
    print("The areas of the two rectangle are the same.")