#randomization
#What do you choose? type 0 for rock, 1 for paper or 2 for scissors.
import random
user_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors?")
choices = ["0", "1", "2"]
computer_choice = random.choice(choices)
print(f"You chose {user_choice}")

if user_choice == "computer_choice":
    print("Its a draw!")
    
elif user_choice == "0" and computer_choice == "2":
    print("You win!")
elif user_choice == "2" and computer_choice == "1":
    print("You win!")
elif user_choice == "2" and computer_choice == "1":
    print("You win")

else:
    print("You Lose!")
