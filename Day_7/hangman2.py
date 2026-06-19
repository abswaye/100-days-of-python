import random 
word_list = ["dadir", "adam","yaseen","zaydan","fahima"]
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
place_holder = ""
word_length = len(chosen_word)
for position in range(word_length):
    place_holder += "_"
print(place_holder)

#Now use a while loop to keep asking the user to guess again.
correct_letters = []
game_over = False
while not game_over:
    guess = input("Guess a letter").lower()

    display = ""

# Change the "for" loop so that you keep the previous correct letters in display.

for letters in chosen_word:
    if letters == guess:
        display += letters
        correct_letters.append(guess)
    elif letters in correct_letters:
        display += "_"
    else:
        display += "_"
print(display)
# To do #2 - If guess is not a letter in the chose_word then reduce lives by 1
#If livse goes down to 0 then the game should stop and it should print "you lose"
if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        game_over = True
        print("You lose!")
if "_" not in display:
    game_over = True
    print("Your Win!")