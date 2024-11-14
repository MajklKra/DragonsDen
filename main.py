

from tkinter import *
import tkinter.font as tkFont

from Classes.player import Player
from Methods.verification import verification
from Classes.square import Square
from Methods.check import check
from Data.Chessboard import pole2

from Methods.players import players
from Methods.place import place

from Classes.MyApp import MyApp


def main():
    root = Tk()
    app = MyApp(root)

    ###for i in range(len(app.stitky)):
            ###print(app.stitky[i].cget("text"))

    ###for i in range(len(app.stitky)):
            ###print(app.stitky2[i].cget("text"))
        
    root.mainloop()

main()


     