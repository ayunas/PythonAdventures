import sys
from room import Room
from player import Player

room = {  #array in format: [north,south,east,west]
    'outside cave':  Room("Outside Cave Entrance",{'n':'foyer','s':None,'e':None,'w':None},
                     "North of you, the cave mount beckons",['sword','dagger']),

    'foyer':    Room("Foyer", {'n':'overlook', 's':'outside cave','e': 'narrow', 'w':None}, """Dim light filters in from the south. Dusty
passages run north and east.""",['scimitar','axe']),

    'overlook': Room("Grand Overlook", {'n': None,'s': 'foyer','e' : None,'w' : None}, """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",['chair','blanket']),

    'narrow':   Room("Narrow Passage", {'n': 'treasure', 's' : None, 'e' : None, 'w' : 'foyer'}, """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",['torch', 'flash-light','lantern']),

    'treasure': Room("Treasure Chamber",{'n' : None,'s' : 'narrow', 'e' : None, 'w' : None}, """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",['treasure chest','lock']),
}


def promptPick(player):
    currentRoom = room[player.location]
    roomItems = currentRoom.items
    if len(roomItems):
        # print(f'items in the {player.location}: ')
        # for item in roomItems:
        #     print(item)
        picked = input("enter the item you wish to pick up: ")
        # print('picked', picked)
        if picked in roomItems:
            # print('picked', picked)
            # print(room[player.location])
            currentRoom.removeItem(picked)
            # updatedRoomItems = currentRoom.removeItem(picked)
            # print('updated room items: ', updatedRoomItems)
            player.pick(picked)
            # print(f'items now in {player.location}: ', roomItems)
        else: 
            print(f'that item is not in {player.location}')
    else:
        print(f'no room items remain in the {player.location}. Lighten your load or proceed with caution')

def promptDrop(player):
    currentRoom = room[player.location]
    roomItems = currentRoom.items
    droppedItem = input(f'{player.name} has {player.bag}.  Enter item to drop: ')
    if droppedItem in player.bag:
        currentRoom.addItem(droppedItem)
        player.drop(droppedItem)
        # print(f'items now in {player.location}: ', roomItems)
    elif not droppedItem:
        print(f'{player.name} chose not to drop anything...')
    else:
        print(f"{droppedItem} not in {player.name}'s bag")

def createPlayer():
    character = input('Choose your character: warrior, knight, sorcerer, angel, genie: ')
    player = Player(character, 'outside cave')
    return player



def main():
    player = createPlayer()

    while True:
        player.locate()
        print(f"items in {player.name}'s bag:", player.bag)
        print(f'items in the {player.location}: ', room[player.location].items)
        promptPick(player)
        promptDrop(player)
        direction = input('press n to go north, s for south, e for east, w for west. press q to quit... ')
        #need error validation on input
        if direction == 'q':
            sys.exit("You have quit the game!")
            break
            
        rooms = room[player.location].getNextRooms()
        if direction and rooms[direction]:
            player.move(rooms[direction])
            print(room[player.location].message)

        elif not direction:
            print(f'{player.name} has decreed to not trodden further.')
        else:
            print(f'Cannot move {direction } from {player.location}')
    
    
    

    





    # 

main()



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

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# from pygame import *
# from pygame.locals import *
# import pygame
# Declare all the rooms