''' Text Game
Certainly! How about creating a program to simulate a simple text-based game? We could create a game where the player navigates through different rooms, i
nteracts with objects, and encounters obstacles or enemies. Here's a basic outline of what the program could include:

1. Define a class for the player character with attributes such as name, health, and inventory.
2. Define a class for rooms with attributes such as description, exits, and any objects or enemies present.
3. Implement movement between rooms.
4. Implement interaction with objects in each room.
5. Implement combat with enemies (if present).
6. Allow the player to pick up items and add them to their inventory.
7. Provide a way to win or lose the game based on certain conditions.

'''
import random
import cmd
import textwrap
import sys
import os
import time

screen_width = 100

# Player setup

class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
        
myPlayer = Player()
        
        
        
# Title Screen

def title_screen_selections():
    option = input("> ").lower()
    if option == "play":
        start_game() # placeholder until written
    elif option == "help":
        help_menu()
    elif option == "quit":
        sys.exit()
    while option not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ").lower()
        if option == "play":
            start_game() # placeholder until written
        elif option == "help":
            help_menu()
        elif option == "quit":
            sys.exit()
            
def title_screen():
    os.system('clear')
    print('###################################')
    print("# WELCOME TO KAI'S TEXT ADVENTURE #")
    print('###################################')
    print('            - PLAY -               ')
    print('            - HELP -               ')
    print('            - QUIT -               ')
    title_screen_selections()
    
def help_menu():
    print('###################################')
    print("#     HELPFUL HINTS AND TIPS      #")
    print('###################################')
    print('-Use up, down, left, right to move-')
    print('  -Type your commands to do them-  ')
    print(' -Use "Look" to inspect something- ')
    

''' Game Map

a1,  a2, ...          Player starts at b2
-----------------
|   |   |   |   | a4
-----------------
|   |   |   |   | b4
-----------------
|   |   |   |   | c4
-----------------
|   |   |   |   | d4
-----------------

'''
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINE = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zone_map = {
    'a1': {
        'ZONENAME': 'Town Market',
        'DESCRIPTION': 'description',
        'EXAMINE': 'examine',
        'SOLVED': False,
        'UP': (''),
        'DOWN': ('b1'),
        'LEFT': (''),
        'RIGHT': ('a2')
    },
    'a2': {
        'ZONENAME': 'Town Entrance',
        'DESCRIPTION': 'description',
        'EXAMINE': 'examine',
        'SOLVED': False,
        'UP': (''),
        'DOWN': ('b2'),
        'LEFT': ('a1'),
        'RIGHT': ('a3')
    },
    'a3': {
        'ZONENAME': 'Town Square',
        'DESCRIPTION': 'description',
        'EXAMINE': 'examine',
        'SOLVED': False,
        'UP': (''),
        'DOWN': ('b3'),
        'LEFT': ('a2'),
        'RIGHT': ('a4')
    },
    'a4': {
        'ZONENAME': 'Town Hall',
        'DESCRIPTION': 'description',
        'EXAMINE': 'examine',
        'SOLVED': False,
        'UP': (''),
        'DOWN': ('b4'),
        'LEFT': ('a3'),
        'RIGHT': ('')
    },
    'b1': {
        'ZONENAME': '',
        'DESCRIPTION': 'description',
        'EXAMINE': 'examine',
        'SOLVED': False,
        'UP': ('a1'),
        'DOWN': ('c1'),
        'LEFT': (''),
        'RIGHT': ('b2')
    },
    'b2': {
        'ZONENAME': 'Home',
        'DESCRIPTION': 'This is your home',
        'EXAMINE': 'Your home looks the same as always - Nothing has changed',
        'SOLVED': False,
        'UP': ('a2'),
        'DOWN': ('c2'),
        'LEFT': ('b1'),
        'RIGHT': ('b3')
    },
    'b3': {
        'ZONENAME': '',
        'DESCRIPTION': 'description',
        'EXAMINE': 'examine',
        'SOLVED': False,
        'UP': ('a3'),
        'DOWN': ('c3'),
        'LEFT': ('b2'),
        'RIGHT': ('b4')
    },
    'b4': {
        'ZONENAME': '',
        'DESCRIPTION': 'description',
        'EXAMINE': 'examine',
        'SOLVED': False,
        'UP': ('a4'),
        'DOWN': ('c4'),
        'LEFT': ('b3'),
        'RIGHT': ('')
    },
}

# Game Interactivity
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.loction.upper + ' #')
    print('# ' + zone_map[myPlayer.location][DESCRIPTION] ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    
def prompt():
    print("\n =============================")
    print("What would you like to do?")
    action = input("> ").lower()
    acceptable_ations = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action not in acceptable_ations:
        print("Unknown action, try again.\n")
        action = input("> ").lower()
    if action == 'quit':
        sys.exit()
    elif action in ['move', 'go', 'travel', 'walk']:
        player_move(action)
    elif action in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action)
        
def player_move(myAction):
    ask = "Where would yo ulike to move to\n?"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zone_map[myPlayer.location](UP)
        movement_handler(destination)
    elif dest in ['left', 'west']:
        

def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ",")
    myPlayer.location = destination
    print_location()
    
    
    
# Game funcionality

def start_game():
    pass
