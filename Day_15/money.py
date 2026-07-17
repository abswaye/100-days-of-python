from resources import resources

def make_coffee(drink):
    resources["water"] -= drink["ingredients"]["water"]
    resources["milk"] -= drink["ingredients"]["milk"]
    resources["coffee"] -= drink["ingredients"]["coffee"]