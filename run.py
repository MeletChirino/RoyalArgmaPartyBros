import pygame, sys
from game_elements.Player import Player, config_players
from game_elements.Game import Game
from game_elements.Board import Board
from game_elements.Player import Player


if __name__=="__main__":
    print("Welcome to RoyalArgmaPartyBros")
    players = config_players()
    print(F"I hope you enjoy the game")

    gameplay = Game(Board("main"), players)

    gameplay.set_avatars()

    # giant loop
    continue_ = True
    while continue_:
        continue_ = gameplay.run()
