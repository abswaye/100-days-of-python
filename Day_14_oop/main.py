class Team:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, name):
        self.name = name

class dangerous_players:
    def __init__(self, name):
        self.name = name
    

belgium = Team("Belgium")

cdk = Player("Charles De Ketelaere")

print(belgium.name)
print(cdk.name)

