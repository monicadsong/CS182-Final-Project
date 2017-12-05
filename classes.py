import copy

class Dancer:
    def __init__(self, name, availability, role):
        #Initializes the data
        self.name = name
        self.availability = availability
        self.role = role
        #self.times = self.get_dancer_times(performances)
        
    '''
    def get_dancer_times(self, performances):
        times = []
        for p in performances:
            for perf in p.performers:
                if self.name == perf.name:
                    times.append(p.choreographer.name)
        return times
	'''

class Rehearsal:
    def __init__(self, choreographer, performers, domains, slot = None):
        self.choreographer = choreographer
        #set the available times for the choreographer to the 
        self.times = [x for x in choreographer.availability if x in domains]
        self.performers = performers
        self.slot = slot

    def remove_dancer(self, performer):
        self.performers.remove(performer)
