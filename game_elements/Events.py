class Event:
    def __init__(self, **kwargs):
        self.sm_list = []
        self.name = ""
        self.save_kwargs(self.name, 'name', kwargs)
        self.verbose = ""
        self.save_kwargs(self.verbose, 'verbose', kwargs)
        self.description = ""
        self.save_kwargs(self.description, 'description', kwargs)
    
    def save_kwargs(self, val, key, kwargs):
        if key in kwargs.keys():
            val = kwargs[key]
            print(f"{key}: {val} saved.")

    def attach(self, st_machine):
        self.sm_list.append(st_machine)

    def happen(self):
        for sm in self.sm_list:
            sm.transition(self)