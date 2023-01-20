import pygame
from time import sleep, time
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

        # Setting up players
        self.players = players
        self.turn = 0
        self.max_turns = len(players)
        print(F"Max turns = {self.max_turns}")

        self.clock = pygame.time.Clock()
        self.save_kwargs(self.name, 'name', kwargs)
        self.save_kwargs(self.verbose, 'verbose', kwargs)
        self.save_kwargs(self.description, 'description', kwargs)
    
    def save_kwargs(self, val, key, kwargs):
        if key in kwargs.keys():
            val = kwargs[key]
            print(f"{key}: {val} saved.")

    def start(self):
        self.screen = pygame.display.set_mode(self.win_size)

    def run(self):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                self.continue_ = False
        #print(f"GAMELOOP ST = {self.current_state}")

        if self.current_state == PRESENTATION:
            self.presentation()

        elif self.current_state == CHOOSE_ITEM:
            # This gives the player the choice wether 
            # to roll the dice or use an item
            ITEM_NOT_CHOOSEN.happen()
        elif self.current_state == ITEM_EVENT:
            # If player choose an item here happens something
            pass
        elif self.current_state == ROLL_DICE:
            self.dice_n = roll_dice()
            DICE_ROLLED.happen()

        elif self.current_state == MOVEMENT:
            self.movement()
            
        elif self.current_state == SQUARE_EVENT:
            # Here we see the event of the last square of the player
            self.square_event()
        elif self.current_state == NEXT_PLAYER:
            # Here we pass the turn to the next player, if its the last one we pass
            # to a game event
            self.turn += 1
            if self.turn >= self.max_turns:
                self.turn = 0
                self.current_state = GAME_EVENT
            else:
                self.current_state = PRESENTATION
                
        elif self.current_state == GAME_EVENT:
            # Mini Game event, present the game and wait for results. Then pass the turn to next player
            print("Play jenga")
            TURN_FINISHED.happen()
            
        # --- Draw Board init
        self.board.draw(self.screen, self.offset)
        # --- Draw Board end

        # --- Draw players init
        # Reorder players
        self.reorder_players()
        # Draw stats
        n = 0
        for pos in range(self.max_turns + 1):
            for player in self.players:
                if player.game_position == pos:
                    player.display_stats(self.screen, n)
                    n += 1

        # Draw players
        for player in self.players:
            player.draw(self.screen)

        # --- Draw players end

        # update screen
        pygame.display.update()
        self.clock.tick(1) # Frames Per Second

    def reorder_players(self):
        for player in self.players:
            order = 1
            for player_compare in self.players:
                if (player.coins < player_compare.coins):
                    order += 1
            player.change_order(order)

    def get_player_by_pos(self, position):
        for player in self.players:
            if (player.game_position == position):
                return player

    def square_event(self):
        player = self.players[self.turn]
        x = player.pos.x
        y = player.pos.y
        ev = self.board.properties["square_ev"][y][x]
        print(f"{player} event {ev}")
        ev(player)
        SQUARE_EVENT_FINISHED.happen()

    def movement(self):
        if(self.dice_n == 0):
            SQUARE_EVENT_BEGINGS.happen()
            #MOVE_FINISHED.happen()
            return

        player = self.players[self.turn]
        x = player.pos.x
        y = player.pos.y
        dir = self.board.properties["square_dir"][y][x]
        player.advance(dir)
        self.dice_n -= 1

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

        #elif self.current_state == NEXT_PLAYER:

        elif self.current_state == GAME_EVENT:
            if event == TURN_FINISHED:
                self.current_state = PRESENTATION 

    def presentation(self):
        # Drawing Rectangle
        timeout = False
        init_time = pygame.time.get_ticks()
        while(not timeout):
            rect = pygame.Rect(
                self.board.properties["presentation_rect"][0], # x coord
                self.board.properties["presentation_rect"][1], # y coord
                self.board.properties["presentation_rect_w"], # width
                self.board.properties["presentation_rect_h"], # height
            )
            # TODO: Replace this rectangle with a beautiful draw
            pygame.draw.rect(self.screen, GRAY, rect)

            title_font = pygame.font.SysFont(
                self.board.properties["presentation_font"],
                self.board.properties["presentation_font_size"]
                )
            player = self.players[self.turn]
            label = title_font.render(F"{player.name}'s turn", 1, BLACK)
            self.screen.blit(
                label,
                self.board.properties["presentation_label_coord"]
                )
            pygame.display.update([rect])
            current_time = pygame.time.get_ticks() - init_time
            self.clock.tick(1) # Frames Per Second
            if (current_time >= 3000):
                print("timeout")
                WAIT_5S.happen()
                timeout = True

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
                    player.move(global_offset)
                    choosen = True
                    n += 1
                else:
                    print("Character not eligible")
                    choosen = False

    def roll_dice(self):
        # --- Get events init
        print(F"Rolling dice")
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                # for more info https://www.pygame.org/docs/ref/key.html
                if event.key == pygame.K_SPACE:
                    #roll dice
                    self.dice_n = roll_dice()
                    print(F"DICE = {self.dice_n}")
                    DICE_ROLLED.happen()
        # mouse_pos = pygame.mouse.get_pos()
        # --- Get events end

    def attach_event(self, event):
        event.attach(self)