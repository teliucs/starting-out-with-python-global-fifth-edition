# 7 Write a program that uses nested loops to draw this pattern:

##
# #
#  #
#   #
#    #
#     #

height = int(input("What will be the height? "))
print("--------------------------")

for r in range(height):
    print("#", end='')
    for c in range(r):
        print(" ", end='')
    print("#")
    print()
        