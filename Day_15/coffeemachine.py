from resources import MENU, resources
from money import make_coffee
choice = input("What would you like? espresso/latte/cappuccino: ")

    
    

if choice == "report":

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

elif choice == "latte":

    drink = MENU["latte"]

    if (
        drink['ingredients']['water'] <= resources["water"]
        and drink["ingredients"]["milk"] <= resources["milk"]
        and drink["ingredients"]["coffee"] <= resources["coffee"]
    ):
        print("There is enough water.")
        make_coffee(drink)
    else:
        print("Sorry, there is not enough water.")

