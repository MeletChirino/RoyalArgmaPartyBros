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

class Player:
    def __init__(self, name_):
        self.name = name_
        self.current_pos = Position()
        self.next_pos = Position()
        self.px = Position()
        self.coins = 20
        #self.avatar = []

    def set_avatar(self, avatar):
        img_file = AVATARS[avatar]
        self.avatar = pygame.image.load(img_file)
        self.pic = pygame.transform.scale(self.avatar, PIC_SIZE)
        self.avatar = pygame.transform.scale(self.avatar, CHARACTER_SIZE)

    def move(self, final_position):
        pass

    def display_stats(self):
        pass

    def draw(self, screen):
        screen.blit(self.avatar, self.current_pos.p())