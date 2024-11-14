from os import X_OK, XATTR_REPLACE
from tkinter import *
import tkinter.font as tkFont

from Classes.player import Player
from Methods.verification import verification
from Classes.square import Square
from Methods.check import check
from Data.Chessboard import pole2

from Methods.players import players
from Methods.place import place

from Methods.players import zavri

import sys

class MyApp:


    def otevrit_vyskakovaci_okno(self):
        vyskakovaci_okno = Toplevel(self._root,bd=1, relief="solid", padx=10, pady=10)
        #form_frame = tk.Frame(root, bd=1, relief="solid", padx=10, pady=10)
        vyskakovaci_okno.title("Konec hry")
        vyskakovaci_okno.geometry("300x200")

        # Přidání štítku a zavíracího tlačítka
        label = Label(vyskakovaci_okno, text="Konec hry !!!.")
        label.pack(pady=20)

        #zavrit_btn = Button(vyskakovaci_okno, text="Zavřít", command=vyskakovaci_okno.destroy)

        zavrit_btn = Button(vyskakovaci_okno, text="Zavřít", command=self.ukoncit_program)
        
        zavrit_btn.pack(pady=10)

        # Přidání funkce pro zavření okna při kliknutí na křížek (X)
        vyskakovaci_okno.protocol("WM_DELETE_WINDOW", self.zavrit_vsechna_okna)

        # Přidání vyskakovacího okna do seznamu otevřených oken
        self.open_windows.append(vyskakovaci_okno)

    def zavrit_vsechna_okna(self):
        print("Všechna okna budou uzavřena.")
        # Zavření všech otevřených vyskakovacích oken
        for window in self.open_windows:
            window.destroy()  # Zavře všechna otevřená vyskakovací okna

        print("Pokus zavrit vyskakovaci okna")
        zavri()

        # Zavření hlavního okna (_root)
        self._root.quit()  # Ukončí hlavní aplikaci
        self._root.destroy()  # Zavře hlavní okno
        

    def ukoncit_program(self):
        print("Program je ukončen.")
        #self._root.quit()
        self.zavrit_vsechna_okna()
        
        
    def __init__(self, root):
        self.open_windows = []
        self._root = root
        self._mode = StringVar()
        self._root.title("Dračí doupě ")

        self._root.geometry("700x700")

        self._font = tkFont.Font(size=10, weight="normal")
        
        self.pokus = 0

        self._root.protocol("WM_DELETE_WINDOW", self.zavrit_vsechna_okna)

        self.p = players()

        self.pocet = (len(self.p))

        self.a_l = 0

        self.center_label = Label(root, text="Dračí doupě ", font=self._font)

        labels = []
       
        for i in range(len(self.p)):
              labels.append(self.p[i].name) 
    
        main_label = Label(root, text="Dračí doupě ", font=("Arial", 16, "bold"), fg="Dark Gray")
        #main_label.pack(pady=10)

        main_label.pack(pady=5, side=TOP)
    
        # Rámec s nadpisem
        top_frame = Frame(self._root)
        #top_frame.pack(pady=10)

        #top_frame.pack(pady=10, fill=X, expand=True)
        top_frame.pack(fill=X, padx=10, pady=(5, 0))

        # První Frame vlevo
        
        #frame_left = Frame(top_frame, width=250, height=500, relief="raised", borderwidth=2)
          
        #frame_left.pack(side=LEFT, padx=10, pady=10)  # Umístění vlevo

        frame_left = Frame(top_frame, width=300, height=300, relief="raised", borderwidth=2)
        frame_left.pack_propagate(False)  # Zabrání přizpůsobení obsahu
        frame_left.grid_propagate(False)
        #frame_left.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        #frame_left.pack(side=LEFT, fill=X, expand=True)
        frame_left.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Přidání štítků do prvního Frame
        ##labels = ["Ahoj, jsem uvnitř Frame!", "Michal", "Petr", "Pavel", "Marketa"]

        self.stitky = [] 
        self.stitky2 = [] 

        for i in range(5):
            frame_left.grid_columnconfigure(i, weight=1, uniform="equal")
       
        label = Label(frame_left, text="Hráči", font=("Arial", 12, "bold"))
        #label.grid(row=0, sticky="w")
   
        label.grid(row=0, column=2, ipady=10, sticky="w") 

        for i, text in enumerate(labels):
            label = Label(frame_left, text=text, font=("Arial", 12))
            label.grid(row=i+1, column=1, columnspan=3,padx=10, pady=10, sticky="w")  # Štítky ve sloupci 0     
            self.stitky.append(label)
    
        ##for i in range(len(pole)):
    
        for i in range(len(self.p)):
            label = Label(frame_left, text="1", font=("Arial", 12))
            label.grid(row=i+1, column=4, padx=10, pady=10, sticky="w")  # Hodnoty ve sloupci 1
            self.stitky2.append(label)
  
        # Přidání tlačítka do prvního Frame vlevo
        #button_left = Button(frame_left, text="Klikni mě", font=("Arial", 12), command=self.button_click)
        #button_left.grid(row=len(labels) + 1, column=1, columnspan=3, pady=20)
       
        # Nový Frame mezi levým a pravým rámem
        #frame_center = Frame(top_frame, width=100, height=500, relief="raised", borderwidth=2)
        #frame_center.pack(side=LEFT, padx=10, pady=10)  # Umístění mezi levým a pravým rámem


        frame_center = Frame(top_frame, width=50, height=100, relief="raised", borderwidth=2)
        frame_center.pack_propagate(False)
        #frame_center.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        frame_center.pack(side=LEFT, fill=X, expand=True)

        # Původní center_label a další obsah
        self.center_label1 = Label(frame_center, text="Hod", font=("Arial", 12, "bold"))
        self.center_label1.pack(pady=(0, 10))  # Vertikální mezera pod prvním labelem

        self.center_label = Label(frame_center, text="", font=("Arial", 12))
        self.center_label.pack(pady=10)

        # Druhý Frame napravo
        #frame_right = Frame(top_frame, width=250, height=500, bg="blue", relief="raised", borderwidth=2)

        #frame_right = Frame(top_frame, width=300, height=600, bg="blue", relief="raised", borderwidth=2)
        
        #frame_right.pack(side=LEFT, padx=10, pady=10)  # Umístění napravo

        #frame_right = Frame(top_frame, width=300, height=300, bg="blue", relief="raised", borderwidth=2)
        frame_right = Frame(top_frame, width=300, height=300, relief="raised", borderwidth=2)
        frame_right.pack_propagate(False)
        #frame_right.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        frame_right.pack(side=LEFT, fill=X, expand=True)

        # Umístění frame_center
        frame_center.pack(side=LEFT, fill=X, expand=True)

        # Přidání tlačítka pod frame_center ve root
        self.below_center_button = Button(self._root, text=" Hoď ", font=("Arial", 12), command=self.button_click)
        self.below_center_button.pack(pady=10)
       
        # Můžete přidat widgety i do druhého Frame
        #label_right = Label(frame_right, text="Tento Frame je napravo", font=("Arial", 12), bg="blue", fg="white")
        #label_right.pack(pady=10)

        #label_right = Label(frame_right, text="Obsah pravého rámce", font=("Arial", 12), bg="blue", fg="white")
        #label_right = Label(frame_right, font=("Arial", 12))
        #label_right.pack(pady=10)
    
        # Načtení obrázku
        self.image = PhotoImage(file="")  # Upravte cestu k obrázku
        #self.image_label = Label(frame_right, image=self.image, bg="blue")
        self.image_label = Label(frame_right, image=self.image)
        #self.image_label.pack(pady=10)
        self.image_label.pack()
    
        # Nový Frame pod oběma rámci
        #frame_bottom = Frame(self._root, width=500, height=100, relief="raised", borderwidth=2)
        #frame_bottom.pack(side=BOTTOM, padx=10, pady=10)  # Umístění dolů

        frame_bottom = Frame(self._root, width=500, height=100, relief="raised", borderwidth=2)
        frame_bottom.pack_propagate(False)
        frame_bottom.pack(side=BOTTOM, padx=10, pady=10, fill=BOTH, expand=True)
    
        # Přidání obsahu do nového Frame
        #bottom_label = Label(frame_bottom, text="Tento Frame je dole", font=("Arial", 12))
        #bottom_label.pack(pady=10)
    
        # Textové pole v dolním rámu
        self.thinker_textbox = Text(frame_bottom, height=10, width=50, font=("Arial", 12), wrap="word")
        self.thinker_textbox.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)
    
        # Posuvník pro textové pole
        scrollbar = Scrollbar(frame_bottom, command=self.thinker_textbox.yview)
        self.thinker_textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        #self.stitky2[self.a_l].config(text=self.p[self.a_l - 1].position, fg="red")
        #self.stitky[self.a_l].config(fg="red")
  
    def button_click(self):
        print("Tlačítko bylo kliknuto!")

        if (self.p[self.a_l-1].position == 100):
            self.ukoncit_program()

        self.pokus = self.pokus + 1

        if (self.a_l == self.pocet):
            self.a_l = 0

        if (self.pokus % 2 != 0):

            for prvek in self.stitky:
                prvek.config(fg="black")

            for prvek in self.stitky2:
                prvek.config(fg="black")

            
            self.stitky2[self.a_l].config(fg="red")
            self.stitky[self.a_l].config(fg="red")
            print(f"hodnota a_l je {self.a_l}")
            return

        else:
            if (self.a_l == self.pocet):
                self.a_l = 0
    
            else:
                self.a_l = self.a_l + 1
    
            if (self.a_l % self.pocet == 1):
                self.thinker_textbox.delete("1.0", END)
       
        text = ""

        '''
        if (self.a_l == self.pocet):
            self.a_l = 1
            
        else:
            self.a_l = self.a_l + 1

        if (self.a_l % self.pocet == 1):
            self.thinker_textbox.delete("1.0", END)
        '''

        print()
        print(f"Aktualni label je {self.a_l}")

        self.p, text, pokus = place(self.p,pole2,self.a_l-1,len(self.p))

        self.center_label.config(text=pokus) 

        print()
        print(f"Vypis údajů:")

        
        for prvek in self.stitky:
            prvek.config(fg="black")

        for prvek in self.stitky2:
            prvek.config(fg="black")
    
        if self.p is not None:
            print(self.p[self.a_l-1].name) 
            print(self.p[self.a_l-1].position) # Zde je bezpečné použít len
            self.stitky2[self.a_l-1].config(text=self.p[self.a_l - 1].position, fg="red")
            self.stitky[self.a_l-1].config(fg="red")
            
            self.thinker_textbox.insert(END, text + "\n")

            if (self.p[self.a_l-1].position == 100):
                print("Konec hry")
                self.thinker_textbox.insert(END, "Konec hry")
                self.otevrit_vyskakovaci_okno()

            if (pole2[self.p[self.a_l-1].position-1].description == "Ladder"):
                self.image = PhotoImage(file="images/ladder2.png")
                self.image_label.config(image=self.image)  # Aktualizuje obrázek na labelu
                self.image_label.image = self.image
            
            elif (pole2[self.p[self.a_l-1].position-1].description == "Snake"):
                self.image = PhotoImage(file="images/snake3.png")
                self.image_label.config(image=self.image)  # Aktualizuje obrázek na labelu
                self.image_label.image = self.image
            
            else:
                self.image = PhotoImage(file="images/dice2.png")
                self.image_label.config(image=self.image)  # Aktualizuje obrázek na labelu
                self.image_label.image = self.image


            
        else:
            print("self.p je None, délka nelze zjistit.")

        
       
        

        



