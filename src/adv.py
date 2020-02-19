from room import Room
from player import Player
from item import Item
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = [
    Item('Carrot', 'A fresh carrot.'),
    Item('Coins', 'Several unremarkable coins.'),
    Item('Sword', 'Sharp - keep away from eyes.'),
    Item('Wand', 'Useful for performing magic. Not the LA-based psych rock band.')
]
items_len = len(items)

# print(items[random.randrange(items_len)])
room['foyer'].items.append(items[random.randrange(items_len)])
room['outside'].items.append(items[random.randrange(len(items))])
room['overlook'].items.append(items[random.randrange(len(items))])
room['narrow'].items.append(items[random.randrange(len(items))])
room['treasure'].items.append(items[random.randrange(len(items))])
# room is a dictionary containing instances of class Room
# iterate through list of items and randomly add those items to the room


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# helper function to get index of an item in items


def get_idx(lst, value):
    for i, dic in enumerate(lst):
        # print(f'{i} -- {dic} /// {value}')
        if dic.name == value:
            return i
    return -1


# tuple of directions -- don't change
directions = ('n', 'e', 's', 'w')
# tuple for actions a user can make
actions = ('get', 'drop', 'inspect', 'inventory')

player_name = input("Welcome to Adventure, please enter you'll name. ~~~>")
player_one = Player(player_name, room['outside'])

print(
    f'Welcome, {player_one.name}, you find yourself in {player_one.current_room}.')


while True:
    cmd = input("""Select a direction [n,e,s,w] for your character to travel. Inspect room for items using [inspect] 
        
        ~~~>""")

    print(f'cmd --> {cmd}')
    # print(player_one.print_current_room)

    if cmd == 'inspect':
        print(player_one.current_room.list_items())

    elif cmd == 'i' or cmd == 'inventory':
        player_one.print_inventory()

    elif 'get' in cmd:
        item_str = cmd.split(' ', )[1]
        print(f'{player_one.name} is attempting to get {item_str}')

        item_idx = get_idx(player_one.current_room.items, item_str)

        if item_idx >= 0:
            player_one.inventory.append(
                player_one.current_room.items[item_idx])
            player_one.current_room.items.pop(item_idx)
        else:
            print(f'{item_str} is not in {player_one.current_room}')

    elif 'drop' in cmd:
        pass
        item_str = cmd.split(' ',)[1]
        print(
            f'You are dropping {item_str} inside of {player_one.current_room}')
        item_idx = get_idx(player_one.inventory, item_str)

        if item_idx >= 0:
            player_one.inventory.pop(item_idx)
            player_one.current_room.items.append(
                player_one.inventory[item_idx])

    elif cmd in directions:
        player_one.move(cmd)

    elif cmd == 'q':
        print("""
        
        Quitting Adventure, you'll coward
*****************////**/%&@@&&&&%%######**(**#%##############(//////////////////*////**///////////*/*/********/*******, 
///////////////((/***/&@&&%%%%%%%%%%%##%/*//*/##################(/////////////////************/////*/////*************. 
###############/***#&&&%%%%%%%%%%#######(/((/(#((((((((((#########(/////////////*/*/**********///*/****///************. 
%%%%%%%%%%%%%#***/&@&%%%%%%%%%%########(((((((((((((((((((((######%#//////////******************/*//**//////***/******. 
&&&&&&&&&&&@#***#&&&%%%%%%%%%%%%#####((((((//////(////((((((((#######(//////////********************////////**********. 
&&&&&&&&&&@%*/*/&&&%%%%%%%%%%%%%####(((((///////////////(((((((#######(////////***************************///*********. 
&&&&&&&&&@%*/(*%@&&%%%%%%%%%%%%####((((//////**/////////((((((#########(////////******************///***/////*********. 
&&&&&&&&@%,/%,(&&&&%%%%%%%%%%%######(((/////////**//////////(((((#######////////*************//*/*///*****************. 
&&&&&&@@%*/&/*&@&&&%%%%%%%%%%%#####(((((//////**////**//*////////(((###%(//////////***********//*****/****************. 
&&&&&&@@(,#&*/&@&&%%%%%%%%%%%%####(((/////********/***********/////((###(///////***/********/*********/*****/*********. 
@@&&&@@@#,(&//%&&&&%%%%%%%%%%%%##(((///*******,************//*((##%%%%%##////////******************/*//***************. 
@@@@@@@@&**@%*&&&&&%%%%%%%%%%%##((((((#####((////*******/////((#((/((((##(/////////**/*******/*****/////**************. 
@@@@@@@@@/,#%/@&&&&%%%%%%%%%%######((((((((((((((///**///((##(/(((((######//////////**********************************. 
&&&&&&&&@%**((@&&&&&%%%%%%%%######(((////(((######(//**/(#########%%#%%%##(////////********//*************************. 
&&&&&&&&@@*,#@@&&%%%%%%%%%%#######%##((((#####%####((////(#((/*/%&%#/(###(((///////////***/*//*//*********************. 
@@@@@@@@@@%**%%%&%%%%%%%%%######%%&&%%&&&(,**/##(###(////((#(//(((((((##((#(/////////**///////*///*//*****************. 
@@@@@@@@@@@#*/#%%%&%%%%%%%#######%##(((//(((###((##(((/////(###(((###((((((#(////////////*/////**/********************. 
@@@@@@@@@@@@(/*#%%%%%%%%%%###############((((/(((((((((/////(##((((((((((((((/////////////////**////*/*/**************, 
@@@@@@@@@@@@%##*/(#%%%%%%%#####((((//////////////(((((((//*///(((/////((((((#(////////////////////**///*************/*, 
@@@@@@@@@@@@@%#(**(%%%%%%%%####((//////////*****/((###(//****//(((//////((((((//////////////*//**/////********/***///*, 
@@@@@@@@@@@@@@%###%%%%%%%%%%###((((//////****//(((#((((//*,,**//(((/////(((((#(///////////////////////*******/////////, 
@@@@@@@@@@@@@@@%#(#%%%%%%%%%###(((((////****////#((((((////**//###(((///((((((#(//////////////////////*******////////*, 
@@@@@@@@@@@@@@@@&###%%%%%%%%####(((((///***/////(##((((((##(######(((//(((((((##///////////////////////*****/////////*, 
@@@@@@@@@@@@@@@@@&%%%%%%%%%%#####(((((////////////(((((//////((((#####(((((((###(/////////////////////////**//////////, 
@@@@@@@@@@@@@@@@@@@@&%%%%%%%%####(((((((///////(((((((////(((/(((((####(##((####(/////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%####((((((////((((((((((///(((((####%%%%%###(#####(/////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%######((((((((((##(#######%####(#(###############(//////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%#######(((((#(##%%%%#####((/////(((((######%##%#(///////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@&@&&%%%%%########((((###((((((((((//((((((##(((((##%%%#(////////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@&@&&&&&%%%#########((##(((//////((((((##(((((((######(((((//////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@&&@&&&&&&%%%%%###%##%####((((((((((((((#(#(((((#####(((((((/////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@@&@&&&%%&&&%%%%%%%%##########(((((((((#((((((######((((((((/////////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@@&@&&&%%%%%&&%%%%%%%%%%########(((((((((((#######%%###(((((((((/////////////////////////////////, 
@@@@@@@@@@@@@@@@@@@@@@&&%%&&%%%%%%%%&%%%%%%%%%%%%#########(((((#####%%%%##%########(((((//////////////////////////////, 
        """)
        break

    else:
        print('''

        Please provide a valid cardinal direction [n, e, s, w] or enter q to quit.

        ''')


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
