
def verification(hod, pozice, Player, array):

    x = hod
    soucet = 0 

    aktualni_pozice = 1

    s2 = ""

    s3 = ""

    """
    while x == 6:
      soucet = soucet + 6
      x = Player.roll_dice()
    
    aktualni_pozice = pozice + soucet + x
    """

    if (Player.position + hod > 100):
       print('hod neproběhl !!!') 
       aktualni_pozice = pozice

       s2 = s2 + "hod neproběhl !!!"  + "\n"

    else:
      
      while x == 6:
        soucet = soucet + 6    
        x = Player.roll_dice()
        print(f'Hráč {Player.name} hodil/a: {x}')

        s2 = s2 + f'Hráč {Player.name} hodil/a: {x}'  + "\n"
        s3 = x

        if (Player.position + soucet + x > 100):
            x = 0  
            print('hod neproběhl2 !!!') 

            s2 = s2 + 'hod neproběhl2 !!!'  + "\n"
            s3 = ""
    
      aktualni_pozice = pozice + soucet + x
      y = aktualni_pozice

    ##print(f'velikost pole je {len(array)}')


    if (aktualni_pozice < len(array) and array[aktualni_pozice-1].shift != 0):
        aktualni_pozice = aktualni_pozice + array[aktualni_pozice-1].shift
        zprava = f"Hráč {Player.name} byl/a na pozici {y} a posunul se na pozici {aktualni_pozice}" 
        print(zprava)
        ##print()

        s2 = s2 + f"Hráč {Player.name} byl/a na pozici {y} a posunul se na pozici {aktualni_pozice}"  + "\n"
        
 
    '''
    print()
    print('Pole')
    print()

    for i in range(len(array)):
         print(array[i].id)
         print(array[i].description)
    '''
      
    return aktualni_pozice, s2, s3
    #return aktualni_pozice