#Build a mini fast-food order summary. Ask the user for their name, what item they want to order, and print a final order ticket message combining that info into one sentence. Also print how many characters are in the item name they typed.
print("Heya, how are you?")
order = input("How can I help you?\n")
name = input("May I have a name for the order?\n")
print("Your order is:\n"+order+"\n"+"for "+name)
print(len(order))