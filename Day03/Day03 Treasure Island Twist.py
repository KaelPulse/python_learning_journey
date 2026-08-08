print("Welcome to tilt with Kael")
print("Secure the W in League of Legends!")
queue = input("Queue: Accept or Decline \n")
if queue == "Accept" or queue =="accept":
    print("I knew I could count on you!")
    main = input("Are you going to play your mains or not? Y or N: ")
    if main == "Y" or main == "y":
        print("Let's go!! We gonna win this!")
        lane = input("Which lane are you going to?Mid, Top, Bot?\n")
        if lane == "Mid" or lane == "mid":
            print("Perma ARAM but you've made it through and secured the Win!!!")
        elif lane == "Top" or lane == "top":
            print("You've died alone.")
        else:
            print("Bot? We've lost because you are a bot...")
    else:
        print("GGs we've lost.")    
else:
    print("You have failed me!")
