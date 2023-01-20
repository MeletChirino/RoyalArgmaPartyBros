import pygame
from common import *
from time import sleep
from game_elements.GameLoop import GameLoop
from game_elements.Player import Player
from game_elements.Transition import Tr



class Game:
    def __init__(self, **kwargs):
        self.current_state = 0

        self.gameloop = GameLoop()
        self.trans_info = {
            # transitions info
            PREPARATION: [
                Tr(GAME_CONFIG_DONE, GAMELOOP),
                ],
            GAMELOOP: [
                Tr(GAME_EVENT_BEGINS, GAME_EVENT),
                ],
            GAME_EVENT: [
                Tr(GAME_EVENT_FINISHED, GAMELOOP),
                ],
            # Next one is empty for the moment
            FINISHED: [],
        }
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
        self.name = ""
        self.save_kwargs(self.name, 'name', kwargs)
        self.verbose = ""
        self.save_kwargs(self.verbose, 'verbose', kwargs)
        self.description = ""
        self.save_kwargs(self.description, 'description', kwargs)
    
    def save_kwargs(self, val, key, kwargs):
        if key in kwargs.keys():
            val = kwargs[key]
            print(f"{key}: {val} saved.")

    def run(self):
        print(f"GAME ST = {self.current_state}")
        if self.current_state == PREPARATION:
            self.gameloop.set_board("monopoly")
            players = [
                Player("melet", "vash"),
                Player("Camila", "zelda"),
                Player("Mariel", "kirby"),
                Player("Thiz", "tingle")
            ]
            for player in players:
                self.gameloop.add_player(player)
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
        transitions = self.trans_info[self.current_state]
        for transition in transitions:
            if transition.match_ev(event):
                self.current_state = transition.next_st()

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