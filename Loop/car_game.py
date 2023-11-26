command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car had been already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop": 
        if not started:
            print("The car had been stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")