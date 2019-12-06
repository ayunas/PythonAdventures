# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.bag = []
    
    def pick(self, item):
        self.bag.append(item)
        print(f"{self.name} picked up the {item} from {self.location}.  Items in {self.name}'s bag: {self.bag} ")

    def drop(self, item):
         removed = filter(lambda i : i != item, self.bag)
         print('remaining in bag', removed)
         print(f"{self.name} dropped {item} in {self.location}")
    
    def locate(self):
        print(f"{self.name} is currently in the: {self.location}")
    
    def move(self,place):
        self.location = place
        print(f"{self.name} has moved to the {self.location}")
    
    def __repr__(self):
        return str(dict([('name', self.name), ('skill', self.skill), ('location', self.location)]))



