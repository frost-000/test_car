command = ""
print ("Enter 'help' for more info.")
started = False
while True:
    command = input ("> ").lower()
    if command == "start":
        if started:
            print ("The engine is running.")
        else:
            started = True
            print ("Car started...")
    elif command == "stop":
        if not started:
            print ("The car doesn't do anything no matter how many times you try.")
        else:
            started = False
            print ("Car has stopped.")
    elif command == "go":
        if started:
            print ("Car is moving...")
        else:
            started = False
            print ("You press on the gas pedal but the car doesn't budge.")
    elif command == "help":
        print ("""
        start - to start the car
        go - to accelerate the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print ("Please use the correct command.")
