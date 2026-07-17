import random
from game_data import data

account_a = random.choice(data)
account_b = random.choice(data)


print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
print(f"Against B: {account_b['name']}")

a_followers = account_a["follower_count"]
b_followers = account_b["follower_count"]
if a_followers > b_followers:
    print("A has more followers")
else:
    print("B has more followers")
round_number = 1

while round_number <= 3:
    account_a = random.choice(data)
    account_b = random.choice(data)
    
