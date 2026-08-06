#Ask the user for two facts about themselves (as two separate inputs) and store each in its own variable. Print both facts combined into a single sentence. 
#Then, reassign one of those variables to a brand new value and print an updated sentence showing the change — without asking for new input, just by changing the variable directly in your code.
print("Tell me two facts about yourself")
fact1 = input("Fact 1: \n")
fact2 = input("Fact 2: \n")
print("So you are "+fact1+" and "+fact2)
fact1 = "Extroverted"
print("So in reality you are "+fact1+" and "+fact2)

