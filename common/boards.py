import os

# --- DIRECTIONS
L = [-1, 0]
R = [1, 0]
D = [0, 1]
U = [0, -1]
O = [0,0]

# --- SQUARE EVENTS ---
def move(player):
    print(f"{player} goes drinks")

def coins(player):
    print(f"{player} earns 3 coins")
    player.coins += 3

def coins_x(player):
    print(f"{player} lost 3 coins")
    player.coins -= 3

def passs(player):
    print(f"{player} nothing happens")

M = move
C = coins
X = coins_x
P = passs

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
            [R, R, R, R],
            ],
    "square_ev": [
            [1, 1, 1, 1],
            ],
    "presentation_rect": [200, 90],
    "presentation_rect_w": 800,
    "presentation_rect_h": 300,
    "presentation_font": "monospace",
    "presentation_font_size": 70,
    "presentation_label_coord": [150, 120],
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
            [M, C, X, C, X, X],
            [C, O, O, O, O, P],
            [X, O, O, O, O, P],
            [C, C, M, X, X, M],
            ],
    "presentation_rect": [200, 90],
    "presentation_rect_w": 800,
    "presentation_rect_h": 300,
    "presentation_font": "monospace",
    "presentation_font_size": 70,
    "presentation_label_coord": [150, 120],
}
