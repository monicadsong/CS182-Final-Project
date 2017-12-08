class Dancer:
    def __init__(self, name, availability, role):
        #Initializes the data
        self.name = name
        self.availability = availability
        self.role = role
        self.constraint_weights = {}

class Rehearsal:
    def __init__(self, choreographer, performers, domains, slot = None):
        self.choreographer = choreographer
        #set the available times for the choreographer to the 
        self.times = [x for x in choreographer.availability if x in domains]
        self.performers = performers
        self.slot = slot

    def remove_dancer(self, performer):
        self.performers.remove(performer)

    def remove_time(self, time):
        self.times.remove(time)

