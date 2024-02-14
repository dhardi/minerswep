import random
import os

matrix_invisible =[]
guess_played =[]
"""
display of board
"""
row_a = ["x","x","x","x","4","x","x","x"]
row_b = ["x","x","x","x","x","x","x","x"]
row_c = ["x","x","x","x","x","x","x","x"]
row_d = ["x","x","x","7","x","x","x","x"]
row_e = ["x","x","x","x","x","x","x","x"]
row_f = ["x","x","x","x","x","x","x","x"]
row_g = ["x","x","x","x","x","x","x","x"]
row_h = ["x","x","x","x","x","x","x","9"]
print("   1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 ")
print(f"1{row_a}\n2{row_b}\n3{row_c}\n4{row_d}\n5{row_e}\n6{row_f}\n7{row_g}\n8{row_h}\n")



def main_board():
    """
    create a second board it will not be visible to the player
    """
    a=[]   
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    for i in range(9):
        a.append(i)
        b.append(i)
        c.append(i)
        d.append(i)
        e.append(i)
        f.append(i)
        g.append(i)
        h.append(i)
    mix_numbers(a,b,c,d,e,f,g,h)        


def mix_numbers(list_a,list_b,list_c,list_d,list_e,list_f,list_g,list_h):  
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
    #new_board(list_a,list_b,list_c,list_d,list_e,list_f,list_g,list_h)
    matrix_invisible =[list_a,list_b,list_c,list_d,list_e,list_f,list_g,list_h]
    print(matrix_invisible)
    #new_board(matrix_invisible)
    choice_Play(matrix_invisible)
   
#def new_board(new_matrix_invisible):
    """
    show the board invisible it will be delete this function
    """
   # matrix_invisible =[new_list_a,new_list_b,new_list_c,new_list_d,new_list_e,new_list_f,new_list_g,new_list_h]
    
    
    #print(f"{new_list_a}\n{new_list_b}\n{new_list_c}\n{new_list_d}\n{new_list_e}\n{new_list_f}\n{new_list_g}\n{new_list_h}\n")
    
def choice_Play(mtx_data):
    """
    it will get the input and make tuples and put it on a list
    """
    while True:
        try:
            global guess_played  
            num1, num2 = map(int, input("Enter two numbers separated by a space: \n").split())
            input_play = (num1 - 1 , num2 - 1) # necessary for matches with the display row and column 
            guess_played.append(input_play)
            print (mtx_data)
        except:
            """
            this it will check if the guess was played twice 
            """
            choice_Play()
        finally:
            search_board(guess_played,mtx_data)

def search_board(pin_board,mtx_data_ava):
    """
    it will pin on the board the location of guess played and also check if there is a bomb 
    """
    global row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, guess_played
    matrix =[row_a,row_b ,row_c ,row_d ,row_e ,row_f ,row_g ,row_h]    
    row_guess, column_guess  = pin_board[-1] # the negative value is to take the last input from the list 
    
    if mtx_data_ava[row_guess ][column_guess] == 8:
        clearConsole()
        matrix[row_guess ][column_guess] = u"\U0001F4A3"
        print("you lost it")
        print("   1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 ")
        print(f"{matrix[0]}\n {matrix[1]}\n {matrix[2]}\n{matrix[3]}\n{matrix[4]}\n{matrix[5]}\n{matrix[6]}\n{matrix[7]}\n")
    else:
        clearConsole()
        matrix[row_guess ][column_guess] = u"\u2705"
        print("  1  |  2 |  3  |  4 |  5 | 6  | 7 | 8")
        print(f"1{matrix[0]}\n2{matrix[1]}\n3{matrix[2]}\n4{matrix[3]}\n5{matrix[4]}\n6{matrix[5]}\n7{matrix[6]}\n8{matrix[7]}\n")
        
    
    #print(matrix[row_guess ][column_guess])







def main():   
    main_board()
    



def clearConsole():
    """
    clean the screen for the user code from https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)  

main()

