import random 
import pyfiglet
import os


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
    if data_str == "s":
        print("Game Screen")
            
    elif data_str == "h":
        print("Tutorial Screen")
    else:
        while True:
            clearConsole()
            print (game_title)
            x_str = input("Enter with S or H\n")
            if x_str == "s":
                print("Game Screen")
                break
            elif x_str == "h":
                ("Tutorial Screen")
                break
            
def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)  

def main ():
    clearConsole()
    game_menu()
    
main()