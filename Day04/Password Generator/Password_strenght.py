def check_strenght(password):
    lenght =len(password)
    if lenght <= 6:
        return("Weak password")
    elif 7 <= lenght <=10:
        return("Medium Password")
    else:
        return("Strong Password")
