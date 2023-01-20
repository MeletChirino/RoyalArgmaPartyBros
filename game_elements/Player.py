from common import *
import pygame
#from time import sleep

# Constants
MAX_ITEMS = 6

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
        self.game_position = 0
        self.items = []
        self.married = False
        self.married_to = ""

    def marry(player2):
        accept = player2.accept()
        if accept:
            self.married = True
            self.married_to = player2
            print(f"Congratulations {self.name} and {player2.name}")
        else:
            print(f"{player2.name} you're mean person. Drink 3 shots!")

    def accept():
        # by default this is accepted, I can make the question later
        return True

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

    def change_order(self, new_order):
        if new_order != self.game_position:
            print(f"{self.name} p.{self.game_position} -> p.{new_order}")
            self.game_position = new_order

    def display_stats(self, screen, i_):
        # Draw the rectangle
        main_offset = [
            STAT_PROPERTIES["rect_offset"][0],
            STAT_PROPERTIES["rect_offset"][1] +
                (i_) * STAT_Y_OFFSET
            ]
        rect = pygame.Rect(
            main_offset[0], # x coord
            main_offset[1], # y coord
            STAT_PROPERTIES["rect_size"][0], # width
            STAT_PROPERTIES["rect_size"][1], # height
            )
        pygame.draw.rect(screen, GRAY, rect)

        # Draw player's avatar
        offset = [
            main_offset[0] + STAT_PROPERTIES["avatar_offset"],
            main_offset[1] + 20
            ]
        screen.blit(self.pic, offset)

        # Draw Player's name
        offset = [
            main_offset[0] + STAT_PROPERTIES["name_offset"][0],
            main_offset[1] + STAT_PROPERTIES["name_offset"][1]
        ]
        title_font = pygame.font.SysFont(
            #self.board.properties["presentation_font"],
            #self.board.properties["presentation_font_size"]
            STAT_PROPERTIES["name_font"],
            STAT_PROPERTIES["name_font_size"],
            )
        label = title_font.render(F"{self.game_position}.{self.name}", 1, BLACK)
        screen.blit(
            label,
            offset
            )

        # Draw coins
        offset = [
            main_offset[0] + STAT_PROPERTIES["coins_offset"][0],
            main_offset[1] + STAT_PROPERTIES["coins_offset"][1]
        ]
        title_font = pygame.font.SysFont(
            #self.board.properties["presentation_font"],
            #self.board.properties["presentation_font_size"]
            STAT_PROPERTIES["coins_font"],
            STAT_PROPERTIES["coins_font_size"],
            )
        label = title_font.render(F"{self.coins}", 1, BLACK)
        screen.blit(
            label,
            offset
            )

        # Draw items
        i = 0
        offset = [
            main_offset[0] + STAT_PROPERTIES["items_offset"][0],
            main_offset[1] + STAT_PROPERTIES["items_offset"][1]
            ]
        for item in self.items:
            if ((i % 3) == 0):
                offset[1] += i * STAT_PROPERTIES["items_separation"]
                offset[0] = main_offset[0] + STAT_PROPERTIES["avatar_offset"][0]
            else:
                offset[0] += i * STAT_PROPERTIES["items_separation"]

            item_logo = pygame.transform.scale(
                item.logo,
                PIC_SIZE
                )
            screen.blit(item_logo, offset)
        pygame.display.update([rect])

    def draw(self, screen):
        screen.blit(self.avatar, self.px.p())

    def add_coins(self, coins):
        self.coins += coins

    def substract_coins(self, coins):
        self.coins -= coins

    def add_item(self, item):
        if len(self.items) < MAX_ITEMS:
            self.items.append[item]
        else:
            print(f"Max Items!")

    def use_item(self, item):
        if (item in self.items):
            self.items.remove(item)
        else:
            raise Exception(f"You don't have {item.name}")

    def __str__(self):
        return F"{self.name} C={self.coins} p.{self.game_position}"