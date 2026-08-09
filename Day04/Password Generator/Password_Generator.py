import random
import Password_strenght

print("Password Generator")
letters = int(input("How many letters would you like your password to have? "))
numbers = int(input("How many numbers would you like your password to have? "))
symbols = int(input("How many symbols would you like your password to have? "))

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = ["0","1","2","3","4","5","6","7","8","9"]
s = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", "/", "~"]

le = random.sample(l, letters)
nu = random.sample(n, numbers)
sy = random.sample(s, symbols)

choice = le + nu + sy
random.shuffle(choice)
password = "".join(choice)

print(f"Your password is: {password}")

strenght = Password_strenght.check_strenght(password)


