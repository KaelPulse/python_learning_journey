print("Gym Membership Cost Calculator")
age = int(input("How old are you?"))
student = input("Are you a student? Y or N ").lower()
days = int(input("How many days a week are you planning to workout?"))
price = 40
student_discount = 10
age_discount = 5
frequency_discount = 10/100
frequency_price = round(price - (price* 10/100), 2)
if age <= 18 or age >= 65:
    age_price = int(price - age_discount)
    if student == "y":
        new_age_price = int(age_price-student_discount)
        if days >= 5:
            student_days = round(new_age_price - (new_age_price* 10/100), 2)
            print(f"Your monthly membership comes to: \n£{student_days} which includes \nAge Discount: £-5 \nStudent Discount: £-10 \nFrequency Discount: 10% \nInitial Price: £40")
        else:
            print(f"Your monthly membership comes to: \n£{new_age_price} which includes \nAge Discount: £-5 \nStudent Discount: £-10 \nInitial Price: £40")
    elif student != "y" and days >=5:
        non_student_f_price = round(age_price -(age_price*10/100), 2)
        print(f"Your monthly membership comes to: \n£{non_student_f_price} which includes \nAge Discount: £-5 \nFrequency Discount: 10% \nInitial Price: £40")
    elif student != "y" and days <5:
        print(f"Your monthly membership comes to: \n£{age_price} which includes \nAge Discount: £-5 \nInitial Price: £40")
else:
    if 19 < age <= 64:
        price = 40
        if student == "y":
            new_price = int(price - student_discount)
            if days >=5:
                psf = round(new_price-(new_price*frequency_discount), 2)
                print(f"Your monthly membership comes to: \n£{psf} which includes \nStudent Discount: £-10 \nFrequency Discount: 10% \nInitial Price: £40")
            else:
                print(f"Your monthly membership comes to: \n£{new_price} which includes \nStudent Discount: £-10 \nInitial Price: £40")
        elif student != "y" and days >= 5:
            print(f"Your monthly membership comes to: \n£{frequency_price} which includes \nFrequency Discount: 10% \nInitial Price: £40")
        else:
            print(f"Your monthly membership comes to: \n£{price}")
    else:
        print(f"Your monthly membership comes to: \n£{price}")

    

