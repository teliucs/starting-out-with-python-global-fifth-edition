# 2 Write a program that asks the user to enter the amount of a purchase and the desired number of
# payment instalments. The program should add 5 percent to the amount to get the total purchase amount,
# and then divide it by the desired number of instalments, then display messages telling the user the total
# amount of the purchase and how much each instalment will cost.

purchase = float(input("What is the amount of your purchase? "))
payment_instalments = float(input("What are your amount of payment instalments? "))

real_purchase = purchase + purchase*0.05
single_instalment = real_purchase / payment_instalments

print("The total amount of the purchase is: " + str(real_purchase) + "€")
print("Each instalment will cost: " + str(single_instalment) + "€")

print(f'The toal amount of the purchase is {real_purchase:.2f}')
print(f'Each instalment will cost {single_instalment:.2f}')