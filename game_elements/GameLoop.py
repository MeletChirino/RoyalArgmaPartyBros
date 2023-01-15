import pygame
from game_elements.Board import Board
from common import *

class GameLoop:
    def __init__(self):
        self.current_state = 0
        pygame.init()

    def init(self, players, board):
        # Setting up board
        self.board = Board(board)
        self.offset = self.board.properties["offset"]
        self.win_size = [
            self.board.size[0] + self.offset[0] * 1.3, # x
            self.board.size[1] + self.offset[1] # y
            ]
        self.screen = pygame.display.set_mode(self.win_size)

        # Setting up players
        self.players = players
        self.turn = 0
        self.max_turns = len(players)
        print(F"Max turns = {self.max_turns}")

        self.clock = pygame.time.Clock()

    def run(self):
        if self.current_state == PRESENTATION:
            # Here you say who's the player and show its items
            pass
        elif self.current_state == CHOOSE_ITEM:
            # This gives the player the choice wether 
            # to roll the dice or use an item
            pass
        elif self.current_state == ITEM_EVENT:
            # If player choose an item here happens something
            pass
        elif self.current_state == ROLL_DICE:
            # here you roll the dice, only roll the dice and store the number
            pass
        elif self.current_state == MOVEMENT:
            # here player moves square by step, changing speed, and getting
            # square events. When dice_n goes to 0 change the state
            pass
        elif self.current_state == SQUARE_EVENT:
            # Here we see the event of the last square of the player
            pass
        elif self.current_state == NEXT_PLAYER:
            # Here we pass the turn to the next player, if its the last one we pass
            # to a game event
            pass
        elif self.current_state == GAME_EVENT:
            # Mini Game event, present the game and wait for results. Then pass the turn to next player
            pass
            
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

    def transition(self, event):
        if self.current_state == PRESENTATION:
            if event == WAIT_5S:
                self.current_state = CHOOSE_ITEM

        elif self.current_state == CHOOSE_ITEM:
            if event == ITEM_CHOOSEN:
                self.current_state = ITEM_EVENT

            if event == ITEM_NOT_CHOOSEN:
                self.current_state = ROLL_DICE

        elif self.current_state == ITEM_EVENT:
            if event == ITEM_EVENT_FINISHED:
                self.current_state = ROLL_DICE

        elif self.current_state == ROLL_DICE:
            if event == DICE_ROLLED:
                self.current_state = MOVEMENT

        elif self.current_state == MOVEMENT:
            if event == SQUARE_MOVE:
                # dice_n -= 1
                self.current_state = MOVEMENT

            if event == SQUARE_EVENT_BEGINGS:
                self.current_state = SQUARE_EVENT

            if event == MOVE_FINISHED:
                self.current_state = NEXT_PLAYER

        elif self.current_state == SQUARE_EVENT:
            if event == SQUARE_EVENT_FINISHED:
                self.current_state = NEXT_PLAYER

        elif self.current_state == NEXT_PLAYER:
            self.turn += 1
            if self.turn >= self.max_turns:
                self.turn = 0
                self.current_state = GAME_EVENT
            else:
                self.current_state = PRESENTATION
        elif self.current_state == GAME_EVENT:
            if event == TURN_FINISHED:
                self.current_state = PRESENTATION 

    def show_avatars(self):
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

    def set_avatars(self):
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

    def gameloop(self):
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

    def attach_event(self, event):
        event.attach(self)