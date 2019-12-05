import sys
from room import Room
from player import Player
# from pygame import *
# from pygame.locals import *
# import pygame
# Declare all the rooms

room = {  #array in format: [north,south,east,west]
    'outside':  Room("Outside Cave Entrance",{'n':'foyer','s':None,'e':None,'w':None},
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", {'n':'overlook', 's':'outside','e': 'narrow', 'w':None}, """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", {'n': None,'s': 'foyer','e' : None,'w' : None}, """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", {'n': 'treasure', 's' : None, 'e' : None, 'w' : 'foyer'}, """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",{'n' : None,'s' : 'narrow', 'e' : None, 'w' : None}, """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

def main():
# Make a new player object that is currently in the 'outside' room.
    
    warrior = Player('warrior','sword','outside')

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    while True:
        warrior.locate()
        direction = input('press n to go north, s for south, e for east, w for west. press q to quit... ')
        #need error validation on input
        if direction == 'q':
            sys.exit("You have quit the game!")
            break
        rooms = room[warrior.location].getNextRooms()
        if rooms[direction]:
            warrior.move(rooms[direction])
            print(room[warrior.location].message)
            # print(room[warrior.location].getNextRooms())  #for debugging the game
        else:
            print(f'Cannot move {direction } from {warrior.location}')

main()

