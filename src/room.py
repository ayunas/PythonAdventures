# Implement a class to hold room information. This should have name and
# description attributes.
class Room: #{
    def __init__(self,place,nextrooms,message, items):
        self.place = place
        self.message = message
        # self.north,self.south,self.east,self.west = nextroom
        self.nextrooms = nextrooms
        self.items = items
    
    def getNextRooms(self):
        # nextrooms = {**self.nextrooms}
        return self.nextrooms
    
    def getRoomItems(self):
        # for item in self.items:
        #     print(item)
        return self.items
    
    # def __checkItems__(i):
    #     print('current items in room: ', self.items)
    #     for i in self.items:
    #         if i == item:
    #             return True
    #         else:
    #             return False

    def removeItem(self,item):
        # print('item in removeItem', item)
        if item in self.items:
            removed = filter(lambda i : i != item, self.items)
            # print('updated items in room', list(removed))
            self.items = list(removed)
            print('items left in room: ',self.items)
            return self.items
    
    def addItem(self, item):
        # print('item in addItem of room', item)
        self.items.append(item)
        print(f'items now in {self.place}: ',self.items)
        return self.items

    def __repr__(self):
        return "\n" + str(dict([("place: ", self.place), ("message", self.message), ('nextrooms', self.nextrooms), ('items', self.items) ] )) + "\n"


    n_to = 'tread northward'
    s_to = 'go southward'
    w_to = 'set westward'
    e_to = 'rise eastward'
    pass  #ending of the class since there are no brackets!!!
#}

