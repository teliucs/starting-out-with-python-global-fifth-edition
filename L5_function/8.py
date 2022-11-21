# A painting company has determined that for every 112 square feet of wall space, one gallon
# of paint and eight hours of labor will be required. The company charges $35.00 per hour
# for labor. Write a program that asks the user to enter the square feet of wall space to be
# painted and the price of the paint per gallon. The program should display the following data:
# • The number of gallons of paint required
# • The hours of labor required
# • The cost of the paint
# • The labor charges
# • The total cost of the paint job

def work(wall, price):
    total_gallons = wall / 112
    total_hours = wall * 8 / 112
    paint_cost = total_gallons * price
    labor_charges = total_hours * 35
    total_cost = total_gallons + total_hours + paint_cost + labor_charges
    
    print(f"The number of gallons of paint required are {total_gallons:,.1f}.")
    print(f"The hours of labor required are {total_hours:,.1f}.")
    print(f"The cost of the paint is ${paint_cost:,.2f}.")
    print(f"The labor charges is ${labor_charges:,.2f}.")
    print(f"The total cost of the paint job is ${total_cost:,.2f}.")

def main():
    square_feet = int(input("Enter the square feet of wall space to be painted: "))
    price_per_gallon = int(input("Enter the price of the paint per gallon: "))
    
    work(square_feet, price_per_gallon)
    
main()