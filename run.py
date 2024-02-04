import random 
import pyfiglet


T = "Miner Swep"
game_title = pyfiglet.figlet_format(T)
"""
Creates The Title of the game with ASCII Art
"""


def game_menu():
    """
    Menu of the Game 
    """
    print (game_title)
    print("Press S to Start\n")
    print("Press H to How to Play\n")
    selected = input("Enter with S or H\n")
    Game_option_validated(selected)

def Game_option_validated(data_str):
    """
    Validated an input press by the user
    """
    while True:
        print ("Command Invalid please Try again\n")
        if data_str == "s":
            print("Game Screen")
            break
        elif data_str == "h":
            print("Tutorial Screen")
            break
    

def main ():
    game_menu()
    
main()