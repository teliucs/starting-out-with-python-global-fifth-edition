# 4 Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:

# The number of shares that Joe purchased was 2,000.
# When Joe purchased the stock, he paid $40.00 per share.
# Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for the stock.
# Two weeks later, Joe sold the stock. Here are the details of the sale:

# The number of shares that Joe sold was 2,000.
# He sold the stock for $42.75 per share.
# He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.
# Write a program that displays the following information:

# The amount of money Joe paid for the stock.
# The amount of commission Joe paid his broker when he bought the stock.
# The amount for which Joe sold the stock.
# The amount of commission Joe paid his broker when he sold the stock.
# The amount of money that Joe had left when he sold the stock and paid his broker (both times).
# If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.

shares_bought = 2000
stock_bought = 40

shares_sold = 2000
stock_sold = 42.75

commission = 0.03

paid = shares_bought * stock_bought
commission_paid = paid * commission

sold = shares_sold * stock_sold
commission_sold = sold * commission

amount_left = sold - paid - commission_paid - commission_sold

print(f"The amount of money Joe paid for the stock is {paid:.1f}$")
print(f"The amount of commission Joe paid his broker when he bought the stock is {commission_paid:.1f}$")
print(f"The amount for which Joe sold the stock si {sold:.1f}$")
print(f"The amount of commission Joe paid his broker when he sold the stock is {commission_sold:.1f}$")
print(f"The amount of money that Joe had left when he sold the stock and paid his broker (both times) is {amount_left:.1f}$")

if amount_left > 0:
    print("Joe made a profit")
else:
    print("Joe lost money")

