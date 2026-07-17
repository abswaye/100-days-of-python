class SoccerTeam:
    def __init__(self, name, country, ranking):
        self.name = name
        self.country = country
        self.ranking = ranking
        self.wins = 0

    def show_info(self):
        print(f"{self.name} represents {self.country}. ranking: {self.ranking}")

    def win_match(self):
        self.wins += 1
        print(f"{self.name} won a match! Total wins: {self.wins}")
argentina = SoccerTeam("Argentina","Argentina", 1)
france = SoccerTeam("France","France", 2)
brazil = SoccerTeam("Brazil","Brazil", 5)

argentina.show_info()
argentina.win_match()

print(argentina.wins)
