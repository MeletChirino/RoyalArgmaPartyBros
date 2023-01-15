import os
from common import *

# --- DIRECTIONS
L = [-1, 0]
R = [1, 0]
D = [0, 1]
U = [0, -1]
O = [0,0]

# --- FOLDERS ---
FILE_FOLDER = os.path.dirname(__file__)
ROOT_FOLDER = os.path.dirname(FILE_FOLDER)
BOARDS_FOLDER = os.path.join(ROOT_FOLDER, 'game_elements', 'img', 'boards')
CHARACTERS_FOLDER = os.path.join(ROOT_FOLDER, 'game_elements', 'img', 'characters')

MAIN_BOARD = {
    "background": os.path.join(BOARDS_FOLDER, "board1.png"),
    "size": (930, 550),
    "offset": [120, 90],
    "start_pos": [70, 70], # you should add the offset and the initial position
    "dim": [1, 4],
    "square_dir": [
            [1, 1, 1, 1],
            ],
    "square_ev": [
            [1, 1, 1, 1],
            ],
}

MONOPOLY_BOARD = {
    "background": os.path.join(BOARDS_FOLDER, "monopoly.png"),
    "size": (930, 550),
    "offset": [120, 90],
    "start_pos": [70, 70], # you should add the offset and the initial position
    "dim": [1, 4],
    "square_dir": [
            [R, R, R, R, R, D],
            [U, O, O, O, O, D],
            [U, O, O, O, O, D],
            [U, L, L, L, L, L],
            ],
    "square_ev": [
            [R, R, R, R, R, D],
            [U, O, O, O, O, D],
            [U, O, O, O, O, D],
            [U, L, L, L, L, L],
            ],
}
