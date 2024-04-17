import sys
import os
import time
import json

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
        self.inventory = []
        self.location = 'b2'  # Setting the starting location
        self.game_over = False

myPlayer = Player()

# Load zone map from JSON file
def load_zones():
    with open('zones.json', 'r') as file:
        return json.load(file)

zone_map = load_zones()

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
    clear_screen()
    print('###################################')
    print("# WELCOME TO KAI'S TEXT ADVENTURE #")
    print('###################################')
    print('            - PLAY -               ')
    print('            - HELP -               ')
    print('            - QUIT -               ')
    title_screen_selections()

def help_menu():
    clear_screen()
    print('###################################')
    print("#     HELPFUL HINTS AND TIPS      #")
    print('###################################')
    print('-Use up, down, left, right to move-')
    print('  -Type your commands to do them-  ')
    print(' -Use "Look" to inspect something- ')
    print(' -Type "inventory" to see your items-')
    print('            - BACK -               ')
    title_screen_selections()

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')  # Clears the screen on Windows
    else:
        os.system('clear')  # Clears the screen on Unix/Linux/Mac


# Main Game Loop
def main_game_loop():
    while not myPlayer.game_over:
        prompt()

# Game Functionalities
def print_location():
    print('# ' + zone_map[myPlayer.location]['ZONENAME'] + ' #')
    print('# ' + zone_map[myPlayer.location]['DESCRIPTION'] + ' #')

def prompt():
    location_info = zone_map[myPlayer.location]
    print("\n=============================")
    print(f"You are at the {location_info['ZONENAME']}.")
    print("What would you like to do?")
    print("Available actions:")
    print(" - Move (type 'move')")
    print(" - Examine (type 'examine')")
    if myPlayer.inventory:
        print(" - Look at inventory (type 'inventory')")
    if 'ITEM' in location_info and location_info['ITEM'] not in myPlayer.inventory:
        print(f" - Pick up {location_info['ITEM']} (type 'pickup')")
    print(" - Quit game (type 'quit')")
    
    action = input("> ").lower()
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'inventory', 'pickup']
    while action not in acceptable_actions:
        print("Unknown action, try again.")
        action = input("> ").lower()
    
    if action == 'quit':
        sys.exit()
    elif action in ['move', 'go', 'travel', 'walk']:
        clear_screen()
        player_move()
    elif action in ['examine', 'inspect', 'interact', 'look']:
        player_examine()
    elif action == 'inventory':
        show_inventory()
    elif action == 'pickup':
        pickup_item()


def pickup_item():
    location_info = zone_map[myPlayer.location]
    if 'ITEM' in location_info and location_info['ITEM'] not in myPlayer.inventory:
        myPlayer.inventory.append(location_info['ITEM'])
        print(f"You have picked up {location_info['ITEM']}.")
    else:
        print("There is nothing here to pick up.")

def player_move():
    location_info = zone_map[myPlayer.location]
    available_directions = {"north": "UP", "south": "DOWN", "east": "RIGHT", "west": "LEFT"}
    valid_moves = []

    print("Where would you like to move?")
    print("Available directions:")

    # Iterate over possible directions and print available ones
    for direction, key in available_directions.items():
        if location_info.get(key):  # Check if the key has a non-empty destination
            valid_moves.append(direction)
            destination_zone = location_info[key]
            print(f" - {direction.capitalize()} (to {zone_map[destination_zone]['ZONENAME']})")

    if not valid_moves:
        print("There are no available moves from here.")
        return

    move = input("> ").lower()
    while move not in valid_moves:
        print("Invalid direction. Choose from the available options:")
        for move in valid_moves:
            destination_zone = location_info[available_directions[move]]
            print(f" - {move.capitalize()} (to {zone_map[destination_zone]['ZONENAME']})")
        move = input("> ").lower()

    destination = location_info[available_directions[move]]
    movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + zone_map[destination]['ZONENAME'] + ".")
    myPlayer.location = destination
    clear_screen()
    print_location()

# Load items from JSON file
def load_items():
    with open('items.json', 'r') as file:
        return json.load(file)

# Define items dictionary
items = load_items()

# Update player_examine function
def player_examine():
    location_info = zone_map[myPlayer.location]
    if location_info['SOLVED']:
        print("You have already exhausted all options here.")
    else:
        print(location_info['EXAMINE'])
        if 'ITEM' in location_info and location_info['ITEM'] not in myPlayer.inventory:
            item_name = location_info['ITEM']
            if item_name in items:
                print(f"You find a {items[item_name]['name']}. Do you want to pick it up? (yes/no)")
                choice = input("> ").lower()
                if choice == 'yes':
                    myPlayer.inventory.append(item_name)
                    print(f"You picked up the {items[item_name]['name']}.")
            else:
                print(f"Error: Item '{item_name}' not found in items dictionary.")
        else:
            print("There is nothing here to pick up.")

# Function to show inventory
def show_inventory():
    print("You are carrying:")
    for item_name in myPlayer.inventory:
        if item_name in items:
            print(f"- {items[item_name]['name']}: {items[item_name]['description']}")


def setup_game():
    clear_screen()
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

    print("########################")
    print("#     LET IT BEGIN     #")
    print("########################")
    clear_screen()
    main_game_loop()

title_screen()
