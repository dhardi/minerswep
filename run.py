import random 
import pyfiglet
import os


T = "Miner Swep"
G = "Game Tutorial"
game_title = pyfiglet.figlet_format(T)
game_tuto =  pyfiglet.figlet_format(G)
"""
Creates The Title of the game with ASCII Art
"""
class Board:

    def __init__(self,size,bombs):
        self.size = size
        self.board = [["." for x in range(size)]for y in  range(size)]
        self.bombs
    

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
        clearConsole()
        game_costruct ()
            
    elif data_str == "h":
        clearConsole()
        game_tutorial()
    else:
        while True:
            clearConsole()
            print (game_title)
            x_str = input("Enter with S or H\n")
            if x_str == "s":
                clearConsole()
                game_costruct ()
                break
            elif x_str == "h":
                clearConsole()
                game_tutorial()
                break
            
def clearConsole():
    """
    clean the screen for the user code from https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)  


def game_costruct ():
    """
    This Def will take an input and save into array also it will check if its a valid number 
    and if not rep number already 
    """
    row_data =[]
    colum_data =[]  
    print ("example 35\n")
    while True:
     try:
        data_input = input("Please select row and Colum\n")
        split_number = [int(digit) for digit in str(data_input)]
        row_data.append(data_input[0])
        colum_data.append(data_input[1])
        check_reps_list(row_data,colum_data)
     except:
        clearConsole()
        game_costruct ()

  

def check_reps_list(row_list,colum_list):
    print("funciona")
    create_board()
    



"""
def create_board():
    for i in range (8):
        for j in range(8):
            print(f"({i},{j})", end="")
        print()   
   
"""    



def game_tutorial():
    """
    This function it will show the Tutorial and explain how the game works
    """
    print(game_tuto)
    print("In this game you will have to guess the safest path to step on.\n")
    print("you will have to select two numbers the first will be your row and the other will be the column.\n")
    print("you have 8 attempts if you step on a mine you lose.\n")
    back_menu = input("Press M to Main Menu\n")
    if back_menu == "m":
        clearConsole()
        game_menu()
    else:
        while True:
            clearConsole()
            game_tutorial()
            if back_menu == "m":
                clearConsole()
                game_menu()
                break

def main ():
    clearConsole()
    game_menu()
    
    
main()