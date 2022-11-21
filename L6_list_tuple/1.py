# 1. Total Sales
    # Design a program that asks the user to enter a store’s sales for each day of the week. The
    # amounts should be stored in a list. Use a loop to calculate the total sales for the week and
    # display the result.

def main():
    sales = store_sales()
    print("Your entries for this week are $" + str(compute_total_sales(sales)) + '.')

def store_sales():
    store_sales = []
    for i in range(7):
        day = float(input("What is the store’s sales for today? $"))
        store_sales.append(day)
    return store_sales

def compute_total_sales(list):
    total = sum(list)
    return total


if __name__ == '__main__':
    main()