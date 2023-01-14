import os
from .boards import *

# --- SIZES ---
SQUARE_SIZE = 70
CHARACTER_SIZE = [40, 40]
SPEED = [10, 10]

# --- AVATAR LIST ---
AVATARS = {
    "homer": os.path.join(CHARACTERS_FOLDER, "homer.png"),
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
