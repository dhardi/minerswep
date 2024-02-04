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
        clearConsole()
        game_costruct ()
            
    elif data_str == "h":
        print("Tutorial Screen")
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
                ("Tutorial Screen")
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
  row_data =[]
  colum_data =[]  
  print ("example 3,5\n")
  data_input = input("Please select row and Colum\n")
  """raw_data = data_input.split()"""
  print(data_input)
  create_board()



def create_board():
    
    for i in range(9):
       print("[ ]"+"[ ]"+"[ ]"+"[ ]"+"[ ]"+"[ ]"+"[ ]"+ "[ ]") 
        
           

        







def main ():
    clearConsole()
    game_menu()
    
    
main()