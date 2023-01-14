import os
from .boards import *
from random import randint

# --- SIZES ---
SQUARE_SIZE = 120
CHARACTER_SIZE = [40, 40]
PIC_SIZE = [70, 70]
SPEED = [1, 1]

CHARACTER_SPACE = 120
CHARACTER_OFFSET = 40

# --- AVATAR LIST ---
AVATARS = {
    #"homer": os.path.join(CHARACTERS_FOLDER, "homer.png"),
    "madeline": os.path.join(CHARACTERS_FOLDER, "madeline.png"),
    "banjo": os.path.join(CHARACTERS_FOLDER, "banjo.png"),
    "donkey": os.path.join(CHARACTERS_FOLDER, "donkey.png"),
    "eren": os.path.join(CHARACTERS_FOLDER, "eren.png"),
    "frisk": os.path.join(CHARACTERS_FOLDER, "frisk.png"),
    "spider": os.path.join(CHARACTERS_FOLDER, "spider_man.gif"),
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
}

# --- COLORS ---
BLACK = (  0,   0,   0)
RED =   (255,   0,   0)
WHITE = (255, 255, 255)

def p_sum(pos1, pos2):
    pos3 = [0, 0]
    for i in range(2):
        pos3[i] = pos1[i] + pos2[i]
    return pos3

def roll_dice():
    return randint(1,6)