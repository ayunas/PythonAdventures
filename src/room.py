# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,place,nextrooms,message):
        self.place = place
        self.message = message
        # self.north,self.south,self.east,self.west = nextroom
        self.nextrooms = nextrooms
    
    def getNextRooms(self):
        # nextrooms = {**self.nextrooms}
        return self.nextrooms

    def __repr__(self):
        return "\n" + str(dict([("place: ", self.place), ("message", self.message), ('nextrooms', self.nextrooms) ] )) + "\n"

    n_to = 'tread northward'
    s_to = 'go southward'
    w_to = 'set westward'
    e_to = 'rise eastward'

# outside = Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons")

# print(outside.n_to)
