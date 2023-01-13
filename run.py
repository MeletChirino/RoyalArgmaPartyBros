import pygame, sys
from game_elements.Player import Player, config_players
from common.colors import Color

COLOR = Color()

if __name__=="__main__":
    print("Welcome to RoyalArgmaPartyBros")
    players = config_players()
    print(F"I hope you enjoy the game")

        # init pygame
    pygame.init()
    size = (420, 250)
    background = pygame.image.load("img/boards/board1.png")
    # crear ventana
    screen = pygame.display.set_mode(size)

    # giant loop
    close = False
    while not close:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                close = True
        screen.fill(COLOR.WHITE)
        screen.blit(background, (0,0))

        # --- Draw Zone Init ---

        # --- Draw Zone End ---

        # update screen
        pygame.display.flip()
