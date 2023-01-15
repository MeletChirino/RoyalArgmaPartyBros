class Event:
    def __init__(self):
        self.sm_list = []
    
    def attach(self, st_machine):
        self.sm_list.append(st_machine)

    def happen(self):
        for sm in self.sm_list:
            sm.transition(self)