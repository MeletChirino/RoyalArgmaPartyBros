import pygame
import socket
from time import sleep, time

# game components
from common import *
from game_elements.Board import Board
from game_elements.Transition import Tr
from game_elements.meryl import Meryl
from game_elements.Player import Player


class GameLoop:
    def __init__(self, **kwargs):
        self.current_state = CHARACTER_SELECT # Starting stage
        pygame.init()
        self.name = ""
        self.save_kwargs(self.name, 'name', kwargs)
        self.verbose = ""
        self.save_kwargs(self.verbose, 'verbose', kwargs)
        self.description = ""
        self.save_kwargs(self.description, 'description', kwargs)
        self.init_time = 0
        self.players = []
        self.max_turns = 0
        self.turn = 0
        self.single_offset = [0, 0]

        self.meryl = Meryl(Meryl.SERVER)

        self.trans_info = {
            # transitions info
            BOARD_SELECT: [
                Tr(BOARD_SELECTED, CHARACTER_SELECT),
                ],
            CHARACTER_SELECT: [
                Tr(GAME_BEGINS, START_TURN),
                Tr(PLAYER_REG, CHARACTER_SELECT),
                ],
            PRESENTATION: [
                Tr(WAIT_5S, CHOOSE_ITEM),
                ],
            CHOOSE_ITEM: [
                Tr(ITEM_CHOOSEN, ITEM_EVENT),
                Tr(ITEM_NOT_CHOOSEN, ROLL_DICE),
                ],
            ITEM_EVENT: [
                Tr(ITEM_EVENT_FINISHED, ROLL_DICE),
                ],
            ROLL_DICE: [
                Tr(DICE_ROLLED, MOVEMENT),
                ],
            MOVEMENT: [
                Tr(SQUARE_MOVE, MOVEMENT),
                Tr(SQUARE_EVENT_BEGINGS, SQUARE_EVENT),
                Tr(MOVE_FINISHED, NEXT_PLAYER),
                ],
            SQUARE_EVENT: [
                Tr(SQUARE_EVENT_FINISHED, NEXT_PLAYER),
                ],
            GAME_EVENT: [
                Tr(TURN_FINISHED, PRESENTATION),
            ]
        }

        self.run_info = {
            BOARD_SELECT: self.board_select,
            # Characters select stage before starting the game
            CHARACTER_SELECT: self.character_select,
            # transitory state
            START_TURN: self.start_turn, # 0
            # Presentacion muestra el nombre del jugador (notifica al server)
            PRESENTATION: self.presentation,# 1
            # Aqui es por si el jugador quiere escoger un item que tenga
            CHOOSE_ITEM: self.choose_item,# 2
            # Aqui espera a que el jugador escoja un Item
            ITEM_EVENT: self.item_event, # 3 Todavia no tengo ni la menor idea de que hacer aqui
            # Este es el espacio donde el item hace efecto
            ROLL_DICE: self.roll_dice,# 4
            # Tiras el dado
            MOVEMENT: self.movement,# 5
            # Se mueve
            SQUARE_EVENT: self.square_event,# 6
            # Si en la casilla hay algun evento, pasa aqui
            NEXT_PLAYER: self.next_player,# 7
            # Estado que da paso al sgte jugador, si lo hay
            GAME_EVENT: self.game_event,# 8
            # Aqui pasan los minijuegos
        }

    def set_board(self, board):
        # Setting up board
        self.board = Board(board)
        self.offset = self.board.properties["offset"]
        print(f"self.offset = {self.offset}")
        self.win_size = [
            self.board.size[0] + self.offset[0] * 1.3, # x
            self.board.size[1] + self.offset[1] # y
            ]
        self.screen = pygame.display.set_mode(self.win_size)
        print(F"Max turns = {self.max_turns}")
        self.clock = pygame.time.Clock()

    def add_player(self, player):
        self.max_turns += 1
        player.set_position(self.max_turns)

        global_offset = p_sum(self.offset, self.board.properties["start_pos"])
        player.set_offset(self.single_offset)

        if (self.max_turns % 3 == 0):
            # this starts a new line
            self.single_offset = p_sum(self.single_offset, [0, CHARACTER_OFFSET])
            self.single_offset[0] = 0
        else:
            # draws a character next to each other
            self.single_offset = p_sum(self.single_offset, [CHARACTER_OFFSET, 0])

        global_offset = p_sum(self.single_offset, global_offset)

        player.move(global_offset)
        self.players.append(player)
        print(f"{player} joined the game")

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.continue_ = False
        print(f"GAMELOOP ST = {self.current_state}")

        st_function = self.run_info[self.current_state]
        st_function()

        # --- Draw Board init
    
        # update screen
        pygame.display.update()
        self.clock.tick(1) # Frames Per Second

    # === State 0 ===
    def start_turn(self):
        # Here you should save some kind of timer value so that next states lasts for a few secons
        self.screen.fill(WHITE)
        self.init_time = pygame.time.get_ticks()
        self.current_state = PRESENTATION

    # === State 1 ===
    def presentation(self):
        # Drawing Rectangle
        self.screen.fill(WHITE)
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
        current_time = pygame.time.get_ticks() - self.init_time
        self.clock.tick(1) # Frames Per Second
        if (current_time >= 3000):
            #print("timeout")
            WAIT_5S.happen()

    # === State 2 ===
    def choose_item(self):
        #print("ITEM event happening")
        self.game_draw()
        ITEM_NOT_CHOOSEN.happen()

    # === State 3 ===
    def item_event(self):
        pass

    # === State 4 ===
    def roll_dice(self):
        self.game_draw()
        self.dice_n = roll_dice()
        #print(F"DICE = {self.dice_n}")
        DICE_ROLLED.happen()

    # === State 5 ===
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
        self.game_draw()

    # === State 6 ===
    def square_event(self):
        self.game_draw()
        # Maybe you should draw somthing else here, depending on the event
        player = self.players[self.turn]
        x = player.pos.x
        y = player.pos.y
        ev = self.board.properties["square_ev"][y][x]
        #print(f"{player} event {ev}")
        ev(player)
        SQUARE_EVENT_FINISHED.happen()

    # === State 7 ===
    def next_player(self):
        self.turn += 1
        if self.turn >= self.max_turns:
            self.turn = 0
            self.current_state = GAME_EVENT
        else:
            self.current_state = PRESENTATION

    # === State 8 ===
    def game_event(self):
        # Mini Game event, present the game and wait for results. Then pass the turn to next player
        print("Play jenga")
        self.game_draw()
        # You should draw something different, depending on the event
        TURN_FINISHED.happen()

    # === State 9 === 
    def character_select(self):
        self.show_avatars()
        self.meryl.wait_for_conn()
        action = self.meryl.wait_for_act()
        # here you're giving general info for local players and show new players
        if action['action'] == 1:
            self.add_player(
                Player(action['name'], action['avatar'])
                )
        elif action['action'] == 0:
            GAME_BEGINS.happen()
        if self.max_turns == 9:
            GAME_BEGINS.happen()

    # === Not relevant methods ===
    def attach_event(self, event):
        event.attach(self)

    def draw_stats(self):
        # Reorder players
        self.reorder_players()
        # Draw stats
        n = 0
        for pos in range(self.max_turns + 1):
            for player in self.players:
                if player.game_position == pos:
                    player.display_stats(self.screen, n)
                    n += 1
    
    def draw_players(self):
        # Draw players
        for player in self.players:
            player.draw(self.screen)

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

    def transition(self, event):
        transitions = self.trans_info[self.current_state]
        for transition in transitions:
            if transition.match_ev(event):
                self.current_state = transition.next_st()

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

            for player in self.players:
                if player.av_name == character:
                    img = pygame.image.load(ELEMENTS['prohibited'])
                    img = pygame.transform.scale(img, CHARACTER_SIZE)
                    self.screen.blit(img, pos)

                    myfont = pygame.font.SysFont("monospace", 20)
                    label = myfont.render(player.name, 1, BLACK)
                    self.screen.blit(label, p_sum(pos, [0, -30]))

            # Set cursor for next Character
            if pos[0] >= (self.win_size[0] - CHARACTER_SPACE - 70):
                pos[0] = CHARACTER_SPACE
                pos[1] += CHARACTER_SPACE
            else:
                pos = p_sum(pos, [CHARACTER_SPACE, 0])

            pygame.display.update()

    def save_kwargs(self, val, key, kwargs):
        if key in kwargs.keys():
            val = kwargs[key]
            print(f"{key}: {val} saved.")

    def game_draw(self):
        self.board.draw(self.screen, self.offset)
        self.draw_stats()
        self.draw_players()

    def send_options(self):
        opt = self.trans_info[self.current_state]
        resp = {'resp': opt}
        print(resp)
        self.meryl.send(resp)