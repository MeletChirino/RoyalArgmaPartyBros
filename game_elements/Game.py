import pygame
from common import *
from time import sleep

class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        pygame.init()
        self.offset = board.properties["offset"]
        self.win_size = [board.size[0] + self.offset[0]*1.3, board.size[1] + self.offset[1]]
        self.screen = pygame.display.set_mode(self.win_size)
        self.clock = pygame.time.Clock()
        self.turn = 0
        self.max_turns = len(players)
        print(F"Max turns = {self.max_turns}")
    
    def set_avatars(self):
        self.screen.fill(WHITE)
        title_font = pygame.font.SysFont("monospace", 40)
        label = title_font.render("Choose your character", 1, BLACK)
        self.screen.blit(label, [200, 0])
        pos = [CHARACTER_SPACE, CHARACTER_SPACE]
        for character in AVATARS:
            img = pygame.image.load(AVATARS[character])
            img = pygame.transform.scale(img, CHARACTER_SIZE)
            self.screen.blit(img, pos)
            myfont = pygame.font.SysFont("monospace", 20)
            label = myfont.render(character, 1, BLACK)
            self.screen.blit(label, p_sum(pos, [0, 60]))

            # Set cursor for next Character
            if pos[0] >= (self.win_size[0] - CHARACTER_SPACE - 70):
                pos[0] = CHARACTER_SPACE
                pos[1] += CHARACTER_SPACE
            else:
                pos = p_sum(pos, [CHARACTER_SPACE, 0])
            pygame.display.flip()
        

        single_offset = [0, 0]
        n = 1
        for player in self.players:
            global_offset = p_sum(self.offset, self.board.properties["start_pos"])
            print(F"{player}")
            choosen = False
            while not choosen:
                choosen = True
                avatar = input(F"{player} please choose a character\n >>> ")
                # verify if charater is already choosen
                for player_ in self.players:
                    if avatar == player_.av_name:
                        print(F"{avatar} is already choosen by {player_}")
                        choosen = False
                        break # break for loop
            
                if avatar in AVATARS and choosen:
                    player.set_offset(single_offset)
                    if (n % 3 == 0):
                        # this starts a new line
                        single_offset = p_sum(single_offset, [0, CHARACTER_OFFSET])
                        single_offset[0] = 0
                    else:
                        # draws a character next to each other
                        single_offset = p_sum(single_offset, [CHARACTER_OFFSET, 0])
                    player.set_avatar(avatar)
                    global_offset = p_sum(single_offset, global_offset)
                    player.move(self.screen, global_offset)
                    choosen = True
                    n += 1
                else:
                    print("Character not eligible")
                    choosen = False

    def run(self):
        continue_ = True
        # --- Get events init
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_ = False
            if event.type == pygame.KEYDOWN:
                # for more info https://www.pygame.org/docs/ref/key.html
                if event.key == pygame.K_SPACE:
                    #roll dice
                    n_dice = roll_dice()
                    print(F"DICE = {n_dice}")
                    self.players[self.turn].advance(self.screen, n_dice)
                    self.turn += 1
                    if self.turn >= self.max_turns:
                        self.turn = 0
            if event.type == pygame.KEYUP:
                pass
        # mouse_pos = pygame.mouse.get_pos()
        # --- Get events end

        # --- Draw Board init
        self.board.draw(self.screen, self.offset)
        # --- Draw Board end

        # --- Draw players init
        # Draw stats

        # Draw players
        for player in self.players:
            player.draw(self.screen)
        
        # --- Draw players end

        # update screen
        pygame.display.flip()
        self.clock.tick(10) # Frames Per Second
        return continue_


