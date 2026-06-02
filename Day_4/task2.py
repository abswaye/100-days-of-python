import random
user_choice = input("What do you choose? typ 0 for rock 1 for paper and 2 for scissor")
choices = ["0" "1" "2"]
computer_choice = random.choice(choices)
print(f"You chose {user_choice}")
if user_choice == "computer_choice":
    print("Its a draw!")

elif user_choice == "0" and computer_choice == "2":
    print("You Win!")
elif user_choice == "1" and computer_choice == "0":
    print("You won!")
elif user_choice == "2" and computer_choice == "1":
    print("You won!")

