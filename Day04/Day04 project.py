print("Rock, Paper or Scissors")

import random

c = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock = 0
paper = 1 
scissors = 2
if c >=3 or c < 0:
    print("You typed an invalid number.")
else:

    choice = ["Rock","Paper","Scissors"]
    ai = random.randint(0,2)
    print(f"The computer chose: {ai}")
    if c == 0 and ai == 0:
        print("Draw")
    elif c== 0 and ai == 1:
        print("You Lost")
    elif c== 0 and ai == 2:
        print("You Win")
    elif c== 1 and ai == 0:
        print("You Win")
    elif c== 1 and ai == 1:
        print(" Draw")
    elif c== 1 and ai == 2:
        print("You Lost")
    elif c== 2 and ai == 0:
        print("You Lost")
    elif c== 2 and ai == 1:
        print("You Win")
    else:
        print("Draw")
