import sys
import os
import time

# Constants for game settings
SCREEN_WIDTH = 100

# Classes and game setup
class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'  # Setting the starting location
        self.inventory = []
        self.game_over = False

myPlayer = Player()

# Title Screen functions
def title_screen_selections():
    option = input("> ").lower()
    while option not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ").lower()
    if option == "play":
        setup_game()
    elif option == "help":
        help_menu()
    elif option == "quit":
        sys.exit()

def title_screen():
    os.system('cls')
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
    title_screen_selections()

# Game Map settings
zone_map = {
    'a1': {
        'ZONENAME': 'Town Market',
        'DESCRIPTION': 'You see stalls selling various goods.',
        'EXAMINE': 'The market bustles with activity.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b1',
        'LEFT': '',
        'RIGHT': 'a2'
    },
    'a2': {
        'ZONENAME': 'Town Entrance',
        'DESCRIPTION': 'The main entrance of the town with guards watching.',
        'EXAMINE': 'The guards seem alert and watchful.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3'
    },
    'a3': {
        'ZONENAME': 'Town Square',
        'DESCRIPTION': 'A vibrant and bustling square filled with people.',
        'EXAMINE': 'There is a beautiful fountain in the center of the square.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4'
    },
    'a4': {
        'ZONENAME': 'Town Hall',
        'DESCRIPTION': 'The official building where the town\'s matters are managed.',
        'EXAMINE': 'You notice the grand architecture of the town hall.',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': ''
    },
    'b1': {
        'ZONENAME': 'Town Gate',
        'DESCRIPTION': 'The gate that leads out of the town to the northern woods.',
        'EXAMINE': 'The gate is heavily fortified.',
        'SOLVED': False,
        'UP': 'a1',
        'DOWN': 'c1',
        'LEFT': '',
        'RIGHT': 'b2'
    },
    'b2': {
        'ZONENAME': 'Main Street',
        'DESCRIPTION': 'The main street that runs through the center of the town.',
        'EXAMINE': 'Shops line the street on both sides.',
        'SOLVED': False,
        'UP': 'a2',
        'DOWN': 'c2',
        'LEFT': 'b1',
        'RIGHT': 'b3'
    },
    'b3': {
        'ZONENAME': 'Library',
        'DESCRIPTION': 'A quiet place filled with books and knowledge.',
        'EXAMINE': 'You can spend hours exploring the wealth of books.',
        'SOLVED': False,
        'UP': 'a3',
        'DOWN': 'c3',
        'LEFT': 'b2',
        'RIGHT': 'b4'
    },
    'b4': {
        'ZONENAME': 'Museum',
        'DESCRIPTION': 'A museum showcasing the history of the town and its surroundings.',
        'EXAMINE': 'The artifacts from different eras tell stories of the past.',
        'SOLVED': False,
        'UP': 'a4',
        'DOWN': 'c4',
        'LEFT': 'b3',
        'RIGHT': ''
    },
    'c1': {
        'ZONENAME': 'Northern Woods',
        'DESCRIPTION': 'Dense woods that are said to be home to mystical creatures.',
        'EXAMINE': 'The woods are dense and dark, with a mysterious aura.',
        'SOLVED': False,
        'UP': 'b1',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': 'c2'
    },
    'c2': {
        'ZONENAME': 'Forest Path',
        'DESCRIPTION': 'A narrow path that winds through the woods.',
        'EXAMINE': 'The path is barely visible under the overgrown foliage.',
        'SOLVED': False,
        'UP': 'b2',
        'DOWN': '',
        'LEFT': 'c1',
        'RIGHT': 'c3'
    },
    'c3': {
        'ZONENAME': 'Hermit\'s Hut',
        'DESCRIPTION': 'A small hut where a wise old hermit lives.',
        'EXAMINE': 'The hut is simple but cozy.',
        'SOLVED': False,
        'UP': 'b3',
        'DOWN': '',
        'LEFT': 'c2',
        'RIGHT': 'c4'
    },
    'c4': {
        'ZONENAME': 'Cliff Edge',
        'DESCRIPTION': 'The edge of a cliff that overlooks the valley below.',
        'EXAMINE': 'The view from here is breathtaking.',
        'SOLVED': False,
        'UP': 'b4',
        'DOWN': '',
        'LEFT': 'c3',
        'RIGHT': ''
    }
}


# Main Game Loop
def main_game_loop():
    while not myPlayer.game_over:
        prompt()

# Game Functionalities
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + zone_map[myPlayer.location]['ZONENAME'] + ' #')
    print('# ' + zone_map[myPlayer.location]['DESCRIPTION'] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n=============================")
    print("What would you like to do?")
    action = input("> ").lower()
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action not in acceptable_actions:
        print("Unknown action, try again.")
        action = input("> ").lower()
    if action == 'quit':
        sys.exit()
    elif action in ['move', 'go', 'travel', 'walk']:
        player_move()
    elif action in ['examine', 'inspect', 'interact', 'look']:
        player_examine()

def player_move():
    print("Where would you like to move?")
    move = input("> ").lower()
    if move in ['up', 'north', 'down', 'south', 'left', 'west', 'right', 'east']:
        destination = zone_map[myPlayer.location][move.upper()]
        if destination == '':
            print("You can't go that way.")
        else:
            movement_handler(destination)
    else:
        print("Invalid direction. Use up, down, left, or right.")

def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine():
    if zone_map[myPlayer.location]['SOLVED']:
        print("You have already exhausted all options here.")
    else:
        print(zone_map[myPlayer.location]['EXAMINE'])

def setup_game():
    # Initialization and role selection
    os.system('cls')
    question1 = "Hello, what is your name traveler?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "What role do you want to play? (Warrior, Mage, Priest)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ").lower()
    while player_job not in ['warrior', 'mage', 'priest']:
        print("Please choose a valid role.")
        player_job = input("> ").lower()
    myPlayer.job = player_job

    if player_job == 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif player_job == 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif player_job == 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60

    # Start the game after setup
    main_game_loop()

# Starting the game
title_screen()
