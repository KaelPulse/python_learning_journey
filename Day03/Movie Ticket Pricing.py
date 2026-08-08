print("Movie Ticket Pricing")
age = int(input("How old are you? "))
day = input("Weekday or Weekend? ").lower()
price = 0
if age < 5:
    print("Free Pass.")
elif 5<= age <=17:
    if day == "weekday":
        price += 6
    else:
        price += 8
elif 18<= age <=64:
    if day == "weekday":
        price +=10
    else:
        price += 13
elif age >= 65:
    price += 7
else:
    print("Input a valid age and specify if its a weekday or weekend.")
print(f"The total for your ticket is {price}. Thank you and enjoy the movie!")
