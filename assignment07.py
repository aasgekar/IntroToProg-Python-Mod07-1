# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: In a pickle!
#              Working with the pickle Python module
#              as well as Try and Except
#              This script will allow the user to set a wish list
#              for a Fantasy Baseball Team.
# ChangeLog:
# JPlemons, 5.28.2020, Created started script
# JPlemons, 5.29.2020, Wrote the main body
# JPlemons, 5.30.2020, Divided script into functions and separation of concerns
# ---------------------------------------------------------------------------- #

import pickle

# Data ------------------------------------------------#
# Declare the variables
strFileName = "FantasyTeam.dat"
lstTeam = []
rngPositions = range(1, 10)  # Baseball positions are identified numerically 1-9


# Processing--------------------------------------------#
class NoPosition(Exception):
    """ Custom error for no position """
    def __str__(self):
        return "Not a playable position"


def save_roster_to_file(file_name, list_of_players):
    """ create or add to file
    :param file_name: FantasyTeam.dat
    :param list_of_players: add to the list
    """
    file = open(file_name, "ab")
    pickle.dump(list_of_players, file)
    file.close()


def read_roster_from_file(file_name):
    """ read the file
    :param file_name: FantasyTeam.dat
    :return: list_of_players
    """
    file = open(file_name, "rb")
    list_of_players = pickle.load(file)
    file.close()
    return list_of_players


def position_player(lstTeam):
    """ Convert the number position into the name of the position
    this is printed in the program only to confirm to the user their choice
    :param lstTeam:
    :return: the name of the position
    """
    if intPosition == 1:
        lstTeam[1] = "Pitcher"
    elif intPosition == 2:
        lstTeam[1] = "Catcher"
    elif intPosition == 3:
        lstTeam[1] = "First base"
    elif intPosition == 4:
        lstTeam[1] = "Second base"
    elif intPosition == 5:
        lstTeam[1] = "Third base"
    elif intPosition == 6:
        lstTeam[1] = "Shortstop"
    elif intPosition == 7:
        lstTeam[1] = "Left field"
    elif intPosition == 8:
        lstTeam[1] = "Center field"
    elif intPosition == 9:
        lstTeam[1] = "Right field"
    return lstTeam


# Presentation-------------------------------------------#

def print_menu():
    print("""
    *****  Menu  *****
      1. Add Player
      2. Exit Program
    ******************""")
    print()


# Main Body of Script_____________________________________#

print("\nFantasy Baseball Pre-Draft Wish List")
print("Enter the Player and Position you hope to draft.")
while True:
    print_menu()  # Show menu items
    choice = input("Please select (1) to add a player or (2) to exit:  ")

    if choice == "1":  # Add the player
        try:
            strPlayer = str(input(" Player Name: ").strip())
            intPosition = int(input(" Player Position (1-9): ").strip())
            if intPosition not in rngPositions:  # Check that choice was 1-9
                raise Exception("Not a position")
        except ValueError as e:  # if input was a string or float
            print("This is not an acceptable position, please use only a whole number.")
            continue
        except Exception as e:  # if input was not 1-9
            print("Please make sure the Position is 1-9")
            continue

        lstTeam = [strPlayer, intPosition]

        save_roster_to_file(strFileName, lstTeam)
        read_roster_from_file(strFileName)

        position_player(lstTeam)
        print(f"{lstTeam[0].title()} -- {lstTeam[1]}")  # Print last entry to display

    elif choice == "2":  # Exit the program
        print("Good luck on the draft.")
        break

    else:
        print("There are only 2 choices.  Let's try that again.")
