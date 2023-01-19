import os
import json
from random import randint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(BASE_DIR, 'config.json')

with open(FILE) as config_file:
    config = json.load(config_file)

if config['platform'] == "DJANGO":
    from apps.RoyalArgmaPartyBros.common.boards import *
    from apps.RoyalArgmaPartyBros.game_elements.Events import Event
else:
    from common.boards import *
    from game_elements.Events import Event


# ---- GAME STATES ----
PREPARATION = 0
GAMELOOP = 1
GAME_EVENT = 2
FINISHED = 3

# --- GAME EVENTS ---
GAME_CONFIG_DONE = Event()
GAME_EVENT_BEGINS = Event()
GAME_EVENT_FINISHED = Event()
GAME_FINISHED = Event()

# --- GAMELOOP STATES ---
PRESENTATION = 0
CHOOSE_ITEM = 1
ITEM_EVENT = 2
ROLL_DICE = 3
MOVEMENT = 4
SQUARE_EVENT = 5
NEXT_PLAYER = 6
GAME_EVENT = 7

# --- GAMELOOP EVENTS ---
WAIT_5S = Event()
ITEM_CHOOSEN = Event()
ITEM_EVENT_FINISHED = Event()
ITEM_NOT_CHOOSEN = Event()
DICE_ROLLED = Event()
SQUARE_MOVE = Event()
SQUARE_EVENT_BEGINGS = Event()
SQUARE_EVENT_FINISHED = Event()
MOVE_FINISHED = Event()
TURN_FINISHED = Event()

# --- SIZES ---
SQUARE_SIZE = 120
CHARACTER_SIZE = [40, 40]
SPEED = [1, 1]

CHARACTER_SPACE = 120
CHARACTER_OFFSET = 40

# --- AVATAR LIST ---
AVATARS = {
    "madeline": os.path.join(CHARACTERS_FOLDER, "madeline.png"),
    "banjo": os.path.join(CHARACTERS_FOLDER, "banjo.png"),
    "donkey": os.path.join(CHARACTERS_FOLDER, "donkey.png"),
    "eren": os.path.join(CHARACTERS_FOLDER, "eren.png"),
    "frisk": os.path.join(CHARACTERS_FOLDER, "frisk.png"),
    "ganondorf": os.path.join(CHARACTERS_FOLDER, "ganondorf.png"),
    "joker": os.path.join(CHARACTERS_FOLDER, "joker.png"),
    "kirby": os.path.join(CHARACTERS_FOLDER, "kirby.png"),
    "lara": os.path.join(CHARACTERS_FOLDER, "lara.png"),
    "link": os.path.join(CHARACTERS_FOLDER, "link.png"),
    "samus": os.path.join(CHARACTERS_FOLDER, "samus.png"),
    "sans": os.path.join(CHARACTERS_FOLDER, "sans.png"),
    "snake": os.path.join(CHARACTERS_FOLDER, "snake.png"),
    "thanos": os.path.join(CHARACTERS_FOLDER, "thanos.png"),
    "tingle": os.path.join(CHARACTERS_FOLDER, "tingle.png"),
    "vash": os.path.join(CHARACTERS_FOLDER, "vash.gif"),
    "zelda": os.path.join(CHARACTERS_FOLDER, "zelda.png"),
    "spider": os.path.join(CHARACTERS_FOLDER, "spider_man.gif"),
}

# --- BOARDS LIST ----
"""
Boards are defined in boards.py within this same folder
"""
BOARDS = {
    "main": MAIN_BOARD,
    "monopoly": MONOPOLY_BOARD,
}

# --- STATS ---

PIC_SIZE = [40, 40]
STAT_Y_OFFSET = 120

STAT_PROPERTIES = {
    # Main square opt
    "rect_size": [170, 100],
    "rect_offset": [10, 10],
    # Avatar properties
    "avatar_offset": 10,
    "avatar_size": [20, 60],
    # Name properties
    "name_offset": [50, 0],
    "name_font_size": 25,
    "name_font": "monospace", # This can could be a board propertie
    # Coins 
    "coins_offset": [60, 20],
    "coins_font_size": 20,
    "coins_font": "monospace", # This can could be a board propertie
    # Items
    "items_offset": [90, 20],
    "items_size": [20, 20],
    "items_separation": 20,
}


# --- COLORS ---
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
WHITE = (255, 255, 255)
GRAY  = (128, 128, 128)

def p_sum(pos1, pos2):
    pos3 = [0, 0]
    for i in range(2):
        pos3[i] = pos1[i] + pos2[i]
    return pos3

def roll_dice():
    return randint(1,6)