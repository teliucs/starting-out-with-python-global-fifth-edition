# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
# application that displays the number of millimeters that the ocean will have risen each year
# for the next 25 years.

RISE = 1.6

print("Year\t| Millimiters")
print("---------------------")

for y in range(25):
    mm = 0
    print(f"{y + 1}\t| {mm + RISE}mm")