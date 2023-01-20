import pygame, sys
from game_elements.Player import Player
from game_elements.Game import Game
from common import *


if __name__=="__main__":
    print("Welcome to RoyalArgmaPartyBros")
    print(F"I hope you enjoy the game")

    gameplay = Game()
    gameplay_events = [
        GAME_CONFIG_DONE,
        GAME_EVENT_BEGINS,
        GAME_EVENT_FINISHED,
        GAME_FINISHED,
    ]
    for event in gameplay_events:
        gameplay.attach_event(event)
    players = [
        Player("melet", "vash"),
        Player("Camila", "zelda"),
        Player("Mariel", "kirby"),
        Player("Thiz", "tingle")
        ]
    gameplay.set_board("monopoly")

    for player in players:
        gameplay.add_player(player)

    # giant loop
    continue_ = True
    while continue_:
        continue_ = gameplay.run()
        continue_ = gameplay.continue_
