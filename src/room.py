# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,place,message):
        self.place = place
        self.message = message
    
    def __repr__(self):
        return str(dict([("place: ", self.place), ("message", self.message)]))

    n_to = 'tread northward'
    s_to = 'go southward'
    w_to = 'set westward'
    e_to = 'rise eastward'

outside = Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons")

# print(outside.n_to)
