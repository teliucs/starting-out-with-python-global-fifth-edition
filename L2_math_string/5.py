# 5 When a bank account pays compound interest, it pays interest not only on the principal amount that
# was deposited into the account, but also on the interest that has accumulated over time. Suppose you want
# to deposit some money into a savings account, and let the account earn compound interest for a certain number of years.
# The formula for calculating the balance of the account after a specified number of years is:  A=P(1+r/n)**nt 

# The terms in the formula are:

# A  is the amount of money in the account after the specified number of years.
# P  is the principal amount that was originally deposited into the account.
# r  is the annual interest rate.
# n  is the number of times per year that the interest is compounded.
# t  is the specified number of years.
# Write a program that makes the calculation for you. The program should ask the user to input the values of 
# P ,  r ,  n ,  t . Once the input data has been entered, the program should calculate and display the amount
# of money that will be in the account after the specified number of years.

P = float(input("How many money did you deposit? $"))
rate = float(input("How much is the annual interest rate? %"))
r = rate / 100
n = float(input("How many times per year is the interest compounded? "))
t = float(input("How many years? "))

A = P * ((1+r/n) ** (n*t))

print(f"The amount of money that will be in the account after {t:.0f} years is {A:.2f}$")