# 1 Design a function that accepts a list as an argument and returns the
# largest value in the list. The function should use recursion to find the largest item.

def main():
    list = []
    to_add = int(input("Add an integer ('0' to end): "))
    while to_add != 0:
        list.append(to_add)
        to_add = int(input("Add an integer ('0' to end): "))

    print(f"The maximum value in {list} is: {find_largest(list)}.")


def find_largest(list):
    if len(list) <= 1:
        greatest = list[0]
    else: 
        greatest = max(list[0], find_largest(list[1:]))
    return greatest
    

if __name__ == '__main__':
    main()