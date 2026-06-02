import random
print(r""" Welcome to 
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
""")
word_list = ["Fahima", "Adam", "Instagram","Facebook","laptop","bus","Yaseen","Zaydan"]
chosen_word = random.choice(word_list).lower()
#print(chosen_word)
lives = 6
correct_guesses = []
stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]
print("Lives:", lives)

while lives > 0:
    guess = input("Guess a letter:").lower()
    if guess in chosen_word:
        correct_guesses.append(guess)
    else:
        lives -= 1
        print(f"Wrong. Lives left: {lives}")
        print(stages[lives])
    display = ""
    for letter in chosen_word:
        if letter in correct_guesses:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("You win!")
        break
if lives == 0:
    print("You lose!")
