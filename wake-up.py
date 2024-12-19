import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You turn off your alarm.")
    print_pause("You hit 'Snooze' on your alarm.")
    print_pause("You let the alarm play.")
    choice()

def choice():
    print_pause("Do you want to wake up?")
    print("1. Yes")
    print("2. No")
    
    choice = input("Please enter 1 or 2: ")
    
    if choice == "1":
        yes()
    elif choice == "2":
        no()
    else:
        print_pause("Invalid choice. Please select 1 or 2.")
        choice()

def yes():
    print_pause("You wake up. It's cold and the sky is dark.")
    print_pause("Suddenly, you hear a clanging from the kitchen.")
    print_pause("You have two options:")
    print("1. Investigate the sound")
    print("2. Go back to sleep")
    
    choice = input("Please enter 1 or 2: ")

    if choice == "1":
        investigate_sound()
    elif choice == "2":
        go_to_sleep()
    else:
        print_pause("Invalid choice. Please select 1 or 2.")
        enter_cave()

def no():
    print_pause("You decide to go back to sleep.")
    print_pause("As you drift off to sleep, you hear a loud bang, and then, nothing.")
    print_pause("The end.")

def investigate_sound():
    print_pause("You gather your courage and move closer to the sound.")
    print_pause("The room is completely dark.)
    print_pause("You step on a lego")
    print("1. You screan out in pain - who gives? You are hurting!")
    print("2. You bite hard on your lip, muffling any potential noise.")
    
    choice = input("Please enter 1 or 2: ")
    
    if choice == "1":
        print_pause("You scream out in pain.")
        print_pause("Feeling confused, you feel something hit the back of your head.")
        print_pause("The end.")
    elif choice == "2":
        print_pause("You bite hard on your lip, determined to be stealhy.")
        print_pause("You see a figure in the shadows.")
        print_pause("The end.")
    else:
        print_pause("Invalid choice. Please select 1 or 2.")
        investigate_sound()

# Start the game
intro()
