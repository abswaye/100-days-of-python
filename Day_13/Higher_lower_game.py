import random
from game_data import data


score = 0
game_should_continue = True

account_b = random.choice(data)



while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    if a_followers > b_followers:
        correct_answer = "a"
    else:
        correct_answer = "b"

    if guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
