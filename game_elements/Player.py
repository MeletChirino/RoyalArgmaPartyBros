from common import *
import pygame
#from time import sleep

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
        self.pos = Position()
        self.next_pos = Position()
        self.px = Position()
        self.next_px = Position()
        self.coins = 20
        self.offset = [0, 0]
        self.av_name = ""
        self.moving = False
        self.speed = [0, 0]

    def set_avatar(self, avatar):
        img_file = AVATARS[avatar]
        self.av_name = avatar
        self.avatar = pygame.image.load(img_file)
        self.pic = pygame.transform.scale(self.avatar, PIC_SIZE)
        self.avatar = pygame.transform.scale(self.avatar, CHARACTER_SIZE)

    def set_offset(self, offset):
        self.offset = offset

    def move(self, final_position):
        self.px.change(final_position)

    def advance(self, direction):
        # aqui debes calcular la velocidad que debes sumarle al personaje en funcion de la casilla
        advance_px = [
            SQUARE_SIZE * direction[0],
            SQUARE_SIZE * direction[1]
            ]
        final_position = p_sum(advance_px, self.px.p())
        self.next_px.change(final_position)
        self.move(final_position)
        self.pos.x += direction[0]
        self.pos.y += direction[1]

    def display_stats(self):
        # this mehtod draws character stats on left side of the canvas
        pass

    def draw(self, screen):
        screen.blit(self.avatar, self.px.p())

    def __str__(self):
        return F"{self.name}"