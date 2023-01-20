class Tr:
    def __init__(self, event, next_state):
        self.event = event
        self.next_state = next_state

    def match_ev(self, event):
        if event == self.event:
            return True
        else:
            return False

    def next_st(self):
        return self.next_state