import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("Im thinking of a number from 1 and 100.")
difficulty = (input("Choose a difficulty. Type 'easy' or 'hard' : "))
answer = 100


if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    guess = int(input("Make a guess"))
    if guess > answer:
        print("Too High!")
        attempts -= 1
    elif guess < answer:
        print("Too Low")
        attempts -= 1
    else:
        print("You got it!")
        break
    if attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        print("Guess Again!")


