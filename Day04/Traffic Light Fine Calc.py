print("Fine Calculator")

color = int(input("What was the traffic light color 0-2? 0. Green, 1. Yellow, 2. Red \n"))
speed = int(input("How fast were you going? \n"))
if color == 0:
    print("You were not fined.")
else:
    if color == 1 and speed < 20:
        print("safely slowing down")
    elif color == 1 and speed > 20:
        print("Caution: you may not stop in time.")
    else:
        if color == 2 and speed == 0:
            print("Stopped safely")
        elif color == 2 and 1< speed <10:
            print("rolling stop : £60 fine.")
        elif color == 2 and speed >= 10:
            print("£100 fine, running the red light")
            if speed >= 30:
                print("Reckless driving charge.")
        else:
            print("Select a valid light color.")
        