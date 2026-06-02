print("Welcome to Treasure Island.")
print("Your mission is to find the treasures.")
choice1 = input("left or right").lower()
if choice1 == "right":
    print("You fell into a hole. Game over!")
elif choice1 == "left":
    choice2 = input("swim or wait?")
    if choice2 == "swim":
        print("Attacked by trout. Game over!")
    elif choice2 == "wait":
        choice3 = input("Which door? red, blue or yellow?")
        if choice3 == "red":
            print("Burned by fire bruh youre cooked!")
        elif choice3 == "blue":
            print("You were eaten by the beasts RIP chump!")
        elif choice3 == "yellow":
            print("ok you wont this time!")
else:
    print("Game over!")
    