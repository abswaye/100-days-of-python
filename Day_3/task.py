print("Welcome to Python Pizza Deliveries!")

bill = 0

size = input("What size pizza do you want S, M or L: ")

small_pizza = 16

medium_pizza = 20

large_pizza = 25

if size == "S":

    bill += small_pizza

elif size == "M": 

    bill += medium_pizza

else:
    bill += large_pizza


peperoni = input("Do you want pepperoni on your cheese pizza? Y or N: ")
if peperoni == "Y":
    if size == "S":
       bill += 2
    else:
        bill += 3

    
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1

    
    print(f"You're final amount is {bill}")

