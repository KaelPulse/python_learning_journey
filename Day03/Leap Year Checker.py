print("Leap Year Checker")
year = int(input("What year would you like me to check? XXXX: \n"))
if year%100==0 and year%4==0 and year%400==0:
    print("Leap year")
elif year%4==0 and year%100==0:
    print("Not a leap year")
elif year%4!=0:
    print("Not a leap year")
elif year%4==0 and year%100==0 and year%400!=0:
    print("Not a leap year")
elif year%4==0 and year%100!=0:
    print("Leap Year")
else:
    print("Enter an actual year.")

