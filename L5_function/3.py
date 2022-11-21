# 3 There are three seating categories at a stadium. Class A seats cost €20, Class B seats cost €15, and Class C seats cost €10. Write a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.

def income(a, b, c):
    # global total
    # total = a * 20 + b * 15 * c * 10
    return a * 20 + b * 15 * c * 10

def main():
    a = int(input("How many tickets in class A were sold? "))
    b = int(input("How many tickets in class B were sold? "))
    c = int(input("How many tickets in class C were sold? "))
    
    # income(a, b, c)
    # print(f"Income generated from ticket sales: {total:,.2f}€")
    print(f"Income generated from ticket sales: {income(a, b, c):,.2f}€")

main()