import pygame, sys
from game_elements.Player import Player, config_players

if __name__=="__main__":
    print("Welcome to RoyalArgmaPartyBros")
    players = config_players()
    print(F"I hope you enjoy the game")

        # init pygame
    pygame.init()
    size = (800, 500)
    # crear ventana
    screen = pygame.display.set_mode(size)

    # giant loop
    close = False
    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
