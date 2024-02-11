import random

row_a = ["x","x","x","x","x","x","x","8"]
row_b = ["x","x","x","x","x","x","x","8"]
row_c = ["x","x","x","x","x","x","x","8"]
row_d = ["x","x","x","x","x","x","x","8"]
row_e = ["x","x","x","x","x","x","x","8"]
row_f = ["x","x","x","x","x","x","x","8"]
row_g = ["x","x","x","x","x","x","x","8"]
row_h = ["x","x","x","x","x","x","x","8"]
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
    print(f"{list_a}\n{list_b}\n{list_c}\n{list_d}\n{list_e}\n{list_f}\n{list_g}\n{list_h}\n")
   
main_board()  



