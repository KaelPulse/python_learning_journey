print("Number Sorter")
number1 = float(input("Pick a number :\n"))
number2 = float(input("Pick a different number :\n"))
number3 = float(input("Pick a different number :\n"))
if number1 == number2 and number2 < number3:
    print(f"The highest number is {number3} and the lowest are {number1} and {number2}")
elif number1 == number2 and number2 > number3:
    print(f"The highest number are {number1} and {number2} the lowest is {number3}")
elif number3 == number2 and number2 > number1:
    print(f"The highest number are {number3} and {number2} the lowest is {number1}")
elif number1 > number2 and number2 == number3:
    print(f"The highest number is {number1} and the lowest are {number2} and {number3}")
elif number1 == number3 and number3 < number2:
    print(f"The highest number is {number2} and the lowest are {number1} and {number3}")
elif number1 > number2 and number2 > number3:
    print(f"The highest number is {number1} and the lowest is {number3}")
elif number1 < number2 and number2 > number3 and number1 < number3:
    print(f"The highest number is {number2} and the lowest is {number1}")
elif number1 < number2 and number2 > number3 and number1 > number3:
    print(f"The highest number is {number2} and the lowest is {number3}")
elif number1 > number2 and number2 < number3 and number1 > number3:
    print(f"The highest number is {number1} and the lowest is {number2}")
elif number3 > number2 and number2 > number1:
    print(f"The highest number is {number3} and the lowest is {number1}")
elif number3 == number2 and number2 == number1:
    print("They are all the highest or lowest as they are equal")
else:
    print(f"The highest number is {number3} and the lowest is {number2}")