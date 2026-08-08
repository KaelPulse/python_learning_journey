print("BMI Calculator")
weight = float(input("Please enter your weight in Kg: "))
height = float(input("Please enter your height in m: "))
bmi = round(weight / (height*height), 2)
age = int(input("How old are you?"))
print(f"Your BMI is: {bmi}")
if bmi < 18.5:
    if age < 18:
        print("As you are still growing, make sure you eat a balanced diet in abundance.")
    else:
        print("We are gonna need to have a strict diet in place to bring your bmi to normal.")
elif 18.5<= bmi <= 24.9:
    if age < 18:
        print("normal bmi, as you are still growing you might want to feel free to eat more.")
    else:
        print("Your bmi is normal for your weight and height.")
elif 25<= bmi <= 29.9:
    if age < 18:
        print("We shall add more vegetables and less carbs in your diet. As this would balance your bmi while you grow up")
    else:
        print("Your bmi points toward the overweight class, we shall restrict your diet, first step is reduce the amount of fast food / greasy food intake.")
elif bmi >= 30:
    if age <18:
        print("Unfortunately your bmi is not looking great. We'll have to cut your food intake on a daily basis following a strict diet.")
    else:
        print("If you are willing to work towards a more normal bmi, please consider being accepted in the recovery section of the hospital where we will help you lower your bmi.")
else:
    print("Enter valid weight and height.")

