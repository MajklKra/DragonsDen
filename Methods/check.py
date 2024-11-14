
from Methods.verification import verification


def check(players, chessboard, Player):
     
    result = True

    s = ""
    
    while result == True:
        
        for i in range(len(players)):  
            if (players[i].position == Player.position and players[i].name != Player.name and Player.position > 1):
                 print(f"Hráč {players[i].name} je na stejné pozici jako hráč {Player.name}") 
                 s = s + f"Hráč {players[i].name} je na stejné pozici jako hráč {Player.name}" + "\n"
                 result = True
                 x = players[i].position
                 players[i].position = players[i].position -1 
                 print(f"Hráč {players[i].name} změnil/a pozici z {x} na {players[i].position}")
                 s = s + f"Hráč {players[i].name} změnil/a pozici z {x} na {players[i].position}" + "\n"
                 print() 
                                               
                 x = verification(0,players[i].position, players[i], chessboard)  
                 
                 #players[i].position = x

                 players[i].position = x[0]

                 print(f'Rekurze číslo. {i}')
                 print(f"pozice hráče {players[i].position}")
                 check(players, chessboard, players[i])

            else:

                if (players[i].position -1 < 1):
                   print(f"pozice hráče {players[i].position}") 
                   players[i].position = 1
                   result = False 
                   break 
         
                result = False
    return s
    