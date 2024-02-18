import random
import os
import pyfiglet
import sys

T = "Miner Swep"
G = "Game Tutorial"
L = "YOU LOST"
W = "YOU WIN"
lives = 0
game_title = pyfiglet.figlet_format(T)
game_tuto = pyfiglet.figlet_format(G)
message_lost = pyfiglet.figlet_format(L)
message_win = pyfiglet.figlet_format(W)

matrix_invisible = []
"""
display of board
"""
row_a = ["x", "x", "x", "x", "x", "x", "x", "x"]
row_b = ["x", "x", "x", "x", "x", "x", "x", "x"]
row_c = ["x", "x", "x", "x", "x", "x", "x", "x"]
row_d = ["x", "x", "x", "x", "x", "x", "x", "x"]
row_e = ["x", "x", "x", "x", "x", "x", "x", "x"]
row_f = ["x", "x", "x", "x", "x", "x", "x", "x"]
row_g = ["x", "x", "x", "x", "x", "x", "x", "x"]
row_h = ["x", "x", "x", "x", "x", "x", "x", "x"]


def main():

    game_menu()


def game_tutorial():
    """
    This function it will show the Tutorial and explain how the game works
    """
    print(game_tuto)
    print("In this game you will have to guess the safest path to step on.\n")
    print("will be your row and the other will be the column.n")
    print("you will have to select two numbers the first \n")
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


def Game_option_validated(data_str):
    """
    Validated an input press by the user
    """
    if data_str == "s":
        clearConsole()
        main_board()

    elif data_str == "h":
        clearConsole()
        game_tutorial()
    else:
        while True:
            clearConsole()
            print(game_title)
            x_str = input("Enter with S or H\n")
            if x_str == "s":
                clearConsole()
                main_board()
                break
            elif x_str == "h":
                clearConsole()
                main_board()
                break


def game_menu():
    """
    Menu of the Game
    """
    print(game_title)
    print("Press S to Start\n")
    print("Press H to How to Play\n")
    selected = input("Enter with S or H\n")
    Game_option_validated(selected)


def main_board():
    """
    create a second board it will not be visible to the player
    """
    print("   1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 ")
    print(f"1{row_a}\n2{row_b}\n3{row_c}\n4{row_d}\n5{
          row_e}\n6{row_f}\n7{row_g}\n8{row_h}\n")
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    for i in range(9):
        a.append(i)
        b.append(i)
        c.append(i)
        d.append(i)
        e.append(i)
        f.append(i)
        g.append(i)
        h.append(i)
    mix_numbers(a, b, c, d, e, f, g, h)


def mix_numbers(
        list_a,
        list_b,
        list_c,
        list_d,
        list_e,
        list_f,
        list_g,
        list_h):
    """
    it will mix the number and 8 will be our bomb
    """
    global matrix_invisible
    random.shuffle(list_a)
    random.shuffle(list_b)
    random.shuffle(list_c)
    random.shuffle(list_d)
    random.shuffle(list_e)
    random.shuffle(list_f)
    random.shuffle(list_g)
    random.shuffle(list_h)
    matrix_invisible = [
        list_a,
        list_b,
        list_c,
        list_d,
        list_e,
        list_f,
        list_g,
        list_h]
    print(matrix_invisible)
    choice_Play(matrix_invisible)


def choice_Play(mtx_data):
    """
    it will get the input and make tuples and put it on a list
    """

    guess_played = []
    
    while True:
        try:
            num1, num2 = map(
                int, input("Enter two numbers separated by a space: \n").split())
            input_play = (num1 - 1, num2 - 1)
            guess_played.append(input_play)
            search_board(guess_played, mtx_data)
             
            
            continue

            if  num1 > 8 and num2 > 8:
                print("Please enter numbers between 1 and 8.")
                
                continue
           

            if type(num1) == str and type(num2) == str:
                num1, num2 = map(
                    int, input("Please enter integers numbers \n").split())
                continue

            if input_play in guess_played:
                print("You have already guessed this position. Please try again.")
                continue

            
            break
           
        except ValueError:
            # Handle the ValueError if the input cannot be converted to integers
            print("Please enter two integers separated by a space.")

def search_board(pin_board, mtx_data_ava):
    """
    it will pin on the board the location of guess played and also check if there is a bomb
    """
    global row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, guess_played, lives
    matrix = [row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h]
    # the negative value is to take the last input from the list
    row_guess, column_guess = pin_board[-1]

    if mtx_data_ava[row_guess][column_guess] == 8:
        clearConsole()
        matrix[row_guess][column_guess] = u"\U0001F4A3"
        print(message_lost)
        print("   1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 ")
        print(
            f"{
                matrix[0]}\n {
                matrix[1]}\n {
                matrix[2]}\n{
                    matrix[3]}\n{
                        matrix[4]}\n{
                            matrix[5]}\n{
                                matrix[6]}\n{
                                    matrix[7]}\n")
        restart_end_game()
    else:
        clearConsole()
        print(lives)

        matrix[row_guess][column_guess] = u"\u2705"
        print("  1  |  2 |  3  |  4 |  5 | 6  | 7 | 8")
        print(
            f"1{
                matrix[0]}\n2{
                matrix[1]}\n3{
                matrix[2]}\n4{
                    matrix[3]}\n5{
                        matrix[4]}\n6{
                            matrix[5]}\n7{
                                matrix[6]}\n8{
                                    matrix[7]}\n")
        game_over()
        choice_Play(mtx_data_ava)


def game_over():
    """
    every guess counts +1 with 8 turns the game over
    """
    global lives
    lives += 1

    if lives == 9:
        clearConsole()
        print(f"{message_win}\n")
        restart_end_game()


def restart_end_game():
    """
    after the end of the game it will ask
    if the player wanna play again
    """

    while True:
        restart_game = input("Do you wanna play Again press R\n")
        if restart_game == "r":
            reeboot_script()
            break
        else:
            reeboot_script()
            break


def reeboot_script():
    """
    reboot the script from 0
    """
    clearConsole()
    os.execv(sys.executable, ['python'] + sys.argv)


def clearConsole():
    """
    clean the screen for the user code from
    https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


main()
