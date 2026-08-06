#Ask the user for their full name, city, and favorite number (typed as text). 
#Generate and print a "digital ID card" as a block of text (multiple lines using \n in a single print, or multiple print statements — your choice) that includes their name, city, favorite number, and the total length of their full name.
#The final output should look like a neatly formatted card, not just a plain sentence.
print("Heya how are you?")
full_name = input("What is your full name, please?\n")
city = input("What is your residential city?\n")
fav_n = input("What is your favourite number? Please write it in letters\n")
print("\nName= "+full_name+"\nCity= "+city+"\nFavourite Number= "+fav_n+"\n")
print(len(full_name))

