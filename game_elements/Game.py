import pygame
from common import *
from time import sleep
from game_elements.StateMachine import StateMachine
from game_elements.GameLoop import GameLoop
from game_elements.Player import Player

class Game:
    def __init__(self):
        self.current_state = 0

        self.gameloop = GameLoop()
        gameloop_events = [
            # --- GAMELOOP EVENTS ---
            WAIT_5S,
            ITEM_CHOOSEN,
            ITEM_EVENT_FINISHED,
            ITEM_NOT_CHOOSEN,
            DICE_ROLLED,
            SQUARE_MOVE,
            SQUARE_EVENT_BEGINGS,
            SQUARE_EVENT_FINISHED,
            MOVE_FINISHED,
            TURN_FINISHED,
        ]
        for event in gameloop_events:
            self.gameloop.attach_event(event)
        self.continue_ = True        

    def run(self):
        #print(f"GAME ST = {self.current_state}")
        if self.current_state == PREPARATION:
            self.gameloop.init(
                self.config_players(),
                self.set_board(),
            )
            self.gameloop.start()
            self.gameloop.show_avatars()
            self.gameloop.set_avatars()
            GAME_CONFIG_DONE.happen()

        elif self.current_state == GAMELOOP:
            self.gameloop.run()
        elif self.current_state == GAME_EVENT:
            # here you have to place a game event
            pass
        elif self.current_state == FINISHED:
                self.continue_ = False
                self.game_finished()

    def transition(self, event):
        if self.current_state == PREPARATION:
            if event == GAME_CONFIG_DONE:
                self.current_state = GAMELOOP

        elif self.current_state == GAMELOOP:
            if event == GAME_EVENT_BEGINS:
                self.current_state = GAME_EVENT

        elif self.current_state == GAME_EVENT:
            if event == GAME_EVENT_FINISHED:
                self.current_state = GAMELOOP

        elif self.current_state == FINISHED:
            pass

    def set_board(self):
        print(F"Please Choose a board")
        for board in BOARDS:
            print(F"* -> {board}")
        choosen = False
        while not choosen:
            choosen = True
            board = input("Which one do you like?\n=> ")
            for board_ in BOARDS:
                if board == board_:
                    # board choosen exist
                    choosen = True
                    break
                else:
                    choosen = False
            if not choosen:
                print("Please verify your text")
        return board

    def config_players(self):
        players = []
        players_n = int(input("How many players?\n"))
        for i in range(players_n):
            name = input(F"Name of player {i} => ")
            player = Player(name)
            players.append(player)
        for player in players:
            print(F"Welcome {player.name}")
        return players

    def attach_event(self, event):
        event.attach(self)