import random

guess_played =[]

row_a = ["x","x","x","x","x","x","x","x"]
row_b = ["x","x","x","x","x","x","x","x"]
row_c = ["x","x","x","x","x","x","x","x"]
row_d = ["x","x","x","x","x","x","x","x"]
row_e = ["x","x","x","x","x","x","x","x"]
row_f = ["x","x","x","x","x","x","x","x"]
row_g = ["x","x","x","x","x","x","x","x"]
row_h = ["x","x","x","x","x","x","x","x"]
print("   1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 ")
print(f"1{row_a}\n2{row_b}\n3{row_c}\n4{row_d}\n5{row_e}\n6{row_f}\n7{row_g}\n8{row_h}\n")



def main_board():
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
    random.shuffle(list_a)
    random.shuffle(list_b)
    random.shuffle(list_c)
    random.shuffle(list_d)
    random.shuffle(list_e)
    random.shuffle(list_f)
    random.shuffle(list_g)
    random.shuffle(list_h)   
    new_board(list_a,list_b,list_c,list_d,list_e,list_f,list_g,list_h)
    
   
   
def new_board(new_list_a,new_list_b,new_list_c,new_list_d,new_list_e,new_list_f,new_list_g,new_list_h,):
    print(f"{new_list_a}\n{new_list_b}\n{new_list_c}\n{new_list_d}\n{new_list_e}\n{new_list_f}\n{new_list_g}\n{new_list_h}\n")
    
def choice_Play():
    while True:
        try:
            global guess_played
            num1, num2 = map(int, input("Enter two numbers separated by a space: \n").split())
            input_play = (num1, num2)
            guess_played.append(input_play)
            print (guess_played)
        except:
            choice_Play()
        finally:
            search_board(guess_played)

def search_board(pin_board):
    

def main():   
    main_board()
    choice_Play()



def clearConsole():
    """
    clean the screen for the user code from https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)  

main()

