 #Ask the user for the total bill, the number of people splitting it, and a fixed service charge percentage.
 #Calculate how much each person owes (rounded to 2 decimal places), and print a full summary using an f-string that shows the original bill, the service charge amount, and the final per-person cost — all in one clean message.

print("Restaurant Bill Splitter")
total_bill = float(input("What is the total bill? £"))
n_of_people = int(input("How many people are splitting the bill?\n"))
service_charge = int(input("Select a service charge rate: 5, 12, 20\n"))
actual_service_charge = round(total_bill * (service_charge/100), 2)
price_per_person =round((total_bill + actual_service_charge) / n_of_people, 2)
print(f"\nTotal Bill: £{total_bill} \nService Charge: £{actual_service_charge} \nPrice Per Person: £{price_per_person}")
