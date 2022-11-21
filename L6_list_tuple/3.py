# 3. Rainfall Statistics
    # Design a program that lets the user enter the total rainfall for each of 12 months into a
    # list. The program should calculate and display the total rainfall for the year, the average
    # monthly rainfall, the months with the highest and lowest amounts.

def main():
    rainfall = get_rainfall()
    print(f"Total rainfall for the year is {sum(rainfall)}.")
    print(f"The average monthhly is {sum(rainfall)/len(rainfall)}.")
    
    min_index = get_min(rainfall)
    max_index = get_max(rainfall)
    print(f"The month with the lowest rainfall is: '{min_index + 1}' with {rainfall[min_index]}.")
    print(f"The month with the highest rainfall is: '{max_index + 1}' with {rainfall[max_index]}.")

def get_rainfall():
    rainfall = []
    for i in range(12):
        single = int(input(f"Enter the rainfall for month {i+1}: "))
        rainfall.append(single)
    return rainfall

def get_min(list):
    min_item = min(list)
    min_index = list.index(min_item)
    return min_index

def get_max(list):
    max_item = max(list)
    max_index = list.index(max_item)
    return max_index


if __name__ ==  '__main__':
    main()