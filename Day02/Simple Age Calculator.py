#Ask the user for their birth year, calculate their current age using basic arithmetic, and print a message using an f-string that includes their name and calculated age.
#07.08.26

print("Simple Age Calculator!")
user_name = input("What is your name?\n")
year_of_birth = input("What year were you born?\n")
current_year = 2026
user_age = current_year - int(year_of_birth)
print(f"{user_name} you are {user_age} years old")
