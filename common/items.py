DIAMOND_RING = {
    "name": "Diamond Ring",
    "description": "You have found a diamond ring, propose marriage to any player. Married couples shares prices and pushments",
    "effect": marry,
}

def marry(player1, player2):
    player1.marry(player2)