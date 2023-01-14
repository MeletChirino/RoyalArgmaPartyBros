from common import *
import pygame

def config_players():
    players = []
    players_n = int(input("How many players?\n"))
    for i in range(players_n):
        name = input(F"Name of player {i} => ")
        player = Player(name)
        players.append(player)
    for player in players:
        print(F"Welcome {player.name}")
    return players

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
        final_position = p_sum(final_position, self.offset)
        self.next_px.change(final_position)
        finished = False
        while not finished:
            finished = True
            if self.px.x <= self.next_px.x:
                self.px.x += SPEED[0]
                finished = False
            if self.px.y <= self.next_px.y:
                self.px.y += SPEED[1]
                finished = False
            
            self.draw(screen)
            pygame.display.flip()

    def advance(self, n_dice):
        final_position = [SQUARE_SIZE * n_dice, 0]

    def display_stats(self):
        # this mehtod draws character stats on left side of the canvas
        pass

    def draw(self, screen):
        screen.blit(self.avatar, self.px.p())

    def __str__(self):
        return F"{self.name}"