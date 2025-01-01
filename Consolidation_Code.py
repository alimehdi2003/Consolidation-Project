#Consolidation Game Project
#Abbas Mehdi INST 126
#11/26/24

import random


# Function to display game menu
def display_menu():
    print("\nTuple Out Game Menu:")
    print("1) Roll the Dice")
    print("2) View Scores")
    print("3) Quit")

# Function to roll dice
def roll_dice():
    dice = random.choices(range(1, 7), k=3)
    print(f"You rolled: {dice}")
    
    # Check for "tuple out" scenario (same number on all three dice)
    if dice.count(dice[0]) == 3:
        print("You tupled out and scored 0 points!\n")
        return 0
    
    # Check for "fixed" dice (two dice are the same)
    fixed_dice = []
    for value in set(dice):  # Iterate over the unique dice values
        if dice.count(value) == 2:  # Check if the current value appears twice
            fixed_dice.append(value)  # Add it to fixed_dice if it does
    
    
    # If there are fixed dice, allow re-rolling of others
    if fixed_dice:
        print("You have fixed dice! You can re-roll the others.\n")
    
    # Total points for this turn
    return sum(dice)

# Function to get valid player input
def get_player_input(player_name):
    valid_input = False
    while not valid_input:
        try:
            # Collect the player's name
            input_value = input(f"{player_name}, do you want to roll the dice or quit? (roll/quit): ").strip().lower()
            if input_value in ['roll', 'quit']:
                valid_input = True
                return input_value
            else:
                print("Invalid input, please type 'roll' or 'quit'.")
        except ValueError:
            print("Invalid input, please try again.")

