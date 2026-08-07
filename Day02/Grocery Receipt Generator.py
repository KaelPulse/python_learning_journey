#Ask the user for three different item names and their individual prices.
#Calculate the total cost of all three items, then calculate what a 5% discount would bring the total down to.
#Print a formatted "receipt" showing each item, the original total, and the discounted total.
#Also print the total number of characters across all three item names combined.

print("Grocery Receipt Generator")
item1 = input("Item Name :\n")
item1_price = float(input("Price:\n £"))
item2 = input("Item Name :\n")
item2_price = float(input("Price:\n £"))
item3 = input("Item Name :\n")
item3_price = float(input("Price:\n £"))
item_cost = round(item1_price+ item2_price + item3_price, 2)
discount = round(item_cost - (item_cost * 5/100) , 2)
print(f"{item1}     £{item1_price}\n{item2}     £{item2_price}\n{item3}     £{item3_price}")
print(f"Total Amount: £{item_cost}")
print("Discount: 5%")
print(f"Total: £{discount}")
print(len(item1+item2+item3))
