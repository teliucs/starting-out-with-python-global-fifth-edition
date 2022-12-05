# 5. Recursive List Sum
# Design a function that accepts a list of numbers as an argument. The function should recursively
# calculate the sum of all the numbers in the list and return that value.


def main():
    list = []
    to_add = int(input("Add an integer ('0' to end): "))
    while to_add != 0:
        list.append(to_add)
        to_add = int(input("Add an integer ('0' to end): "))

    print(f"The sum for {list} is: {compute_sum(list)}.")


def compute_sum(list):
    if len(list) <= 1:
        return list[0]
    else:
        return list[0] + compute_sum(list[1:])


if __name__ == '__main__':
    main()