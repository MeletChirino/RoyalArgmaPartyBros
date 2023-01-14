import pygame
from common import *

import os

BOARD_SIZE = (420, 250)

class Board:
    def __init__(self, board_id):
        self.properties = BOARDS[board_id]

        self.bg = pygame.image.load(
            self.properties['background']
        )
        self.size = self.properties['size']

    def draw(self, screen, offset):
        screen.fill(WHITE)
        offset = (offset[0], 30)
        screen.blit(self.bg, offset)
        
    