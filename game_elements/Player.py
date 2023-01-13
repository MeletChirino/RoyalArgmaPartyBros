def config_players():
    players = []
    players_n = int(input("How many players?\n"))
    for i in range(players_n):
        name = input(F"Name of player {i} => ")
        players.append(Player(name))
    for player in players:
        print(F"Welcome {player.name}")
    return players

class Player:
    def __init__(self, name_):
        self.name = name_