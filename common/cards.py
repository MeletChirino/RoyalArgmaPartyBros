class Card:
    def __init__(self, card_dict):
        self.name = card_dict["name"]
        self.description = card_dict["description"]
        self.effect = card_dict["effect"]

    def exec_effect(self):
        self.effect()
