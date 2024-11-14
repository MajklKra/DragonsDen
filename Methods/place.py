from Classes.player import Player
from Methods.verification import verification
from Classes.square import Square
from Methods.check import check
from Data.Chessboard import pole2

###from termcolor import colored, cprint

##import sys
##sys.setrecursionlimit(2000) 

j = 0

#def place(pole, pole2):
def place(pole, pole2, no, pocet):
    konec = 1

    global j 
    
    s = ""
    s3 = ""
    s4 = ""
    

    s1 = ""

    print()
    print("Jsem tam")
    print(f"Počet je {pocet}")
    
    #while  konec != 100: 

    if ((no) % pocet == 0) :
        j = j + 1
        s = s + f"{j}. kolo"+ "\n"
        s = s + "---------" + "\n"
        s = s + "\n"
        print(f"J je {j}")
        print (f"zbytek po dělení {no % pocet}")
    else:
        print(f"J je {j}")
        print (f"zbytek po dělení {no % pocet}")
    
        
    kolo = f"{j}. kolo"
    print()
    print(kolo)
    print("---------")
    print()

    '''
    s = s + f"{j}. kolo"+ "\n"
    s = s + "---------" + "\n"
    s = s + "\n"
    '''
        
        #for i in range(len(pole)): 
        
            #hod = pole[i].roll_dice() 
            #zprava = f"Hrac {pole[i].name} hodil: {hod}" 

    hod = pole[no].roll_dice() 
    zprava = f"Hráč {pole[no].name} hodil: {hod}" 
    print(zprava)
    s = s + zprava + "\n"
    s1 = hod

    #a_position = verification(hod, pole[i].position, pole[i], pole2)   
    #a_position, s3 = verification(hod, pole[i].position, pole[i], pole2) 
    a_position, s3, s4 = verification(hod, pole[no].position, pole[no], pole2) 

    if (s4 != ""):
        s1 = s4
        
    #zprava = f"Aktualni pozice hrace {pole[i].name} je: {a_position}"
    zprava = f"Aktualní pozice hráče {pole[no].name} je: {a_position}"
    #pole[i].position, s3  = a_position
    #pole[i].position  = a_position
    pole[no].position  = a_position
    #s = s + s3 + f"Aktualni pozice hrace {pole[i].name} je: {a_position}"  + "\n"
    s = s + s3 + f"Aktualní pozice hráče {pole[no].name} je: {a_position}"  + "\n"
    konec = a_position
    print(zprava)
    print()

    #check(pole, pole2, pole[i])
    s4 = check(pole, pole2, pole[no])

    s = s + s4
    
    '''    
    if (konec == 100): 
        print()
        #print(f"Hrac {pole[i].name} vyhral!!!")
        print(f"Hrac {pole[no].name} vyhral!!!")
        print()
        #s = s + f"Hrac {pole[i].name} vyhral!!!"
        s = s + f"Hrac {pole[no].name} vyhral!!!"
        break
    '''

    return pole, s, s1    
        #return pole
        