# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, skill, location):
        self.name = name
        self.skill = skill
        self.location = location
    
    # def attack(self):
    #     print(f'{self.name} attacks with {self.skill}!')
    
    def locate(self):
        print(f"{self.name} is currently in the: {self.location}")
    
    def move(self,place):
        self.location = place
        print(f"{self.name} has moved to the {self.location}")
    
    def __repr__(self):
        return str(dict([('name', self.name), ('skill', self.skill), ('location', self.location)]))



