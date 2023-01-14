import os

# --- FOLDERS ---
FILE_FOLDER = os.path.dirname(__file__)
ROOT_FOLDER = os.path.dirname(FILE_FOLDER)
BOARDS_FOLDER = os.path.join(ROOT_FOLDER, 'game_elements', 'img', 'boards')
CHARACTERS_FOLDER = os.path.join(ROOT_FOLDER, 'game_elements', 'img', 'characters')

MAIN_BOARD = {
    "background": os.path.join(BOARDS_FOLDER, "board1.png"),
    "size": (420, 250),
    "offset": [120, 90],
    "start_pos": [105, 105],
    "dim": [1, 4],
    "square_dir": [
            [1, 1, 1, 1],
            ],
    "square_ev": [
            [1, 1, 1, 1],
            ],
}