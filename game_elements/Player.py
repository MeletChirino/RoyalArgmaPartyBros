from common import *
import pygame
from time import sleep

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def p(self):
        return [self.x, self.y]

    def change(self, next_pos):
        self.x = next_pos[0]
        self.y = next_pos[1]
    
    def __str__(self):
        return F"[x = {self.x}, y = {self.y}]"

class Player:
    def __init__(self, name_):
        self.name = name_
        self.current_pos = Position()
        self.next_pos = Position()
        self.px = Position()
        self.next_px = Position()
        self.coins = 20
        self.offset = [0, 0]
        self.av_name = ""

    def set_avatar(self, avatar):
        img_file = AVATARS[avatar]
        self.av_name = avatar
        self.avatar = pygame.image.load(img_file)
        self.pic = pygame.transform.scale(self.avatar, PIC_SIZE)
        self.avatar = pygame.transform.scale(self.avatar, CHARACTER_SIZE)

    def set_offset(self, offset):
        self.offset = offset

    def move(self, screen, final_position):
        #final_position = p_sum(final_position, self.offset)
        self.next_px.change(final_position)
        finished = False
        while not finished:
            finished = True
            if self.px.x < self.next_px.x:
                self.px.x += SPEED[0]
                finished = False
            if self.px.y < self.next_px.y:
                self.px.y += SPEED[1]
                finished = False

            # this slow down animations
            #sleep(0.1)
            screen.blit(self.avatar, self.px.p())
            pygame.display.flip()

    def advance(self, screen, n_dice, direction):
        # aqui debes calcular la velocidad que debes sumarle al personaje en funcion de la casilla
        advance = [SQUARE_SIZE * n_dice, SQUARE_SIZE * n_dice]
        final_position = p_sum(advance, self.px.p())
        self.move(screen, final_position)

    def display_stats(self):
        # this mehtod draws character stats on left side of the canvas
        pass

    def draw(self, screen):
        screen.blit(self.avatar, self.px.p())

    def __str__(self):
        return F"{self.name}"