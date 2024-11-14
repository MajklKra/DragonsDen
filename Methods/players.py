from Classes.player import Player
from Methods.verification import verification
from Classes.square import Square
from Methods.check import check
from Data.Chessboard import pole2


import tkinter as tk
from tkinter import messagebox

pocet = 0  # Globální proměnná pro počet hráčů
pole = []

open_windows = []

okno = 0




def formular_jmena_hracu():
    # Formulář pro zadání jmen hráčů
    root = tk.Tk()
    root.title("Jména")

    open_windows.append(root)

    root.protocol("WM_DELETE_WINDOW", zavri)

    # Rámeček (Frame) s okrajem pro formulář
    #form_frame = tk.Frame(root, bd=1, relief="solid", bg="lightblue",padx=10, pady=10)
    form_frame = tk.Frame(root, relief="solid", bg="lightblue",padx=10, pady=10)
    form_frame.pack(expand=True)

    labels = []
    entries = []

    for i in range(pocet):
        #label = tk.Label(root, text=f"Jméno hráče {i+1}:")
        label = tk.Label(form_frame, text=f"Jméno hráče {i+1}:", bg="lightblue")
        label.pack()
        #entry = tk.Entry(root)
        entry = tk.Entry(form_frame)
        entry.pack()
        labels.append(label)
        entries.append(entry)

    #button = tk.Button(root, text="Uložit jména", command=lambda: ulozit_jmena_hracu(entries, root))
    button = tk.Button(form_frame, text="Uložit jména", command=lambda: ulozit_jmena_hracu(entries, root))
    button.pack(pady=10)

    root.mainloop()


def ulozit_jmena_hracu(entries, root):
    global pole
    pole = []  # Reset pole před uložením nových jmen

    error = 0
    
    for entry in entries:
        jmeno = entry.get()
        if jmeno:
            pole.append(Player(jmeno, 1))
            
        else:
            messagebox.showerror("Chyba", "Všechna jména hráčů musí být vyplněna.")
            error = 1
            root.attributes('-topmost', True)
            return

    if (error !=1):
        messagebox.showinfo("Úspěch", f"Jména hráčů byla uložena.")
        root.quit()
        root.destroy()
        open_windows.remove(root)
    
#print_jmena_hracu()

def formular():

    '''
    # Vytvoření hlavního okna formuláře
    root = tk.Tk()
    root.title("Zadejte počet hráčů")
    root.attributes('-topmost', True)
    
    # Vytvoření štítku a textového pole
    label = tk.Label(root, text="Počet hráčů:")
    label.pack(pady=5)

    entry_pocet_hracu = tk.Entry(root)
    entry_pocet_hracu.pack(pady=5)

    # Tlačítko pro potvrzení hodnoty a zavření okna
    button = tk.Button(root, text="Uložit", command=lambda: ulozit_pocet_hracu(entry_pocet_hracu, root))
    button.pack(pady=10)

    root.mainloop()
    '''
   
    def move_window_down():
        x, y = root.winfo_x() +10 , root.winfo_y() + 10  # Zvětší souřadnici y pro posun dolů
        root.geometry(f"300x300+{x}+{y}")  # Nastaví novou pozici okna
        if y < 100 and x <100:  # Nastaví cílovou pozici
            root.after(50, move_window_down)  # Opakuje pohyb každých 50 ms
    
    # Vytvoření hlavního okna formuláře
    root = tk.Tk()
    root.title("Hráči")
    root.attributes('-topmost', True)

    open_windows.append(root)
    root.protocol("WM_DELETE_WINDOW", zavri)

    #root.geometry("300x300+100+1000")

    # Spustí animovaný pohyb okna
    #move_window_down()

    # Rámeček (Frame) s okrajem pro formulář
    #form_frame = tk.Frame(root, bd=1, relief="solid", bg="#D3D3D3",padx=50, pady=10)
    form_frame = tk.Frame(root, relief="solid", bg="#D3D3D3",padx=50, pady=10)
    form_frame.pack(expand=True)

    # Vytvoření štítku a textového pole uvnitř form_frame
    label = tk.Label(form_frame, text="Počet hráčů: [Max: 7]")
    label.pack(pady=5)

    entry_pocet_hracu = tk.Entry(form_frame)
    entry_pocet_hracu.pack(pady=5)

    # Tlačítko pro potvrzení hodnoty a zavření okna
    button = tk.Button(form_frame, text="Uložit", command=lambda: ulozit_pocet_hracu(entry_pocet_hracu, root))
    button.pack(pady=10)

    root.mainloop()


def ulozit_pocet_hracu(entry, root):
    global pocet
    
    try:
        # Převedení vstupu na číslo a kontrola platného rozsahu
        pocet = int(entry.get())
        if 1 <= pocet <= 7:
            messagebox.showinfo("Úspěch", f"Počet hráčů byl uložen: {pocet}")
            root.quit()  # Ukončí hlavní smyčku okna
            root.destroy()  # Zavře okno formuláře

            open_windows.remove(root)
        else:
            messagebox.showerror("Chyba", "Počet hráčů musí být mezi 1 a 7.")
    except ValueError:
        messagebox.showerror("Chyba", "Zadejte platné číslo.")


def zavri():
    print("Ostatni okna budou uzavřena.")
    # Zavření všech otevřených vyskakovacích oken
       
    for window in open_windows:
        window.destroy()  # Zavře všechna otevřená vyskakovací okna

    open_windows.clear()  # Vyčistí seznam po zavření všech oken

    

def players():
    global pocet

    # Zavolání formuláře pro zadání počtu hráčů
    formular()

    # Po formuláři, zkontrolujeme hodnotu `pocet`
    if pocet > 0:
        print(f"Počet hráčů je: {pocet}")
    else:
        print("Počet hráčů nebyl zadán nebo je mimo povolený rozsah.")
        return  # Ukončí funkci, pokud není `pocet` platný

    #pole = []  # Seznam pro uložení hráčů

    '''
    for i in range(pocet):
        while True:
            try:
                jmeno = input(f"Zadejte jmeno {i+1}. hrace: ")
                if jmeno:
                    # Přidá jméno hráče, pokud není prázdné
                    pole.append(Player(jmeno, 1))
                    break
                else:
                    print("Jméno nemůže být prázdné. Zadejte jméno znovu.")
            except ValueError:
                print("Chyba: Zadejte prosím jméno")
    '''
  
    formular_jmena_hracu()
    
    return pole
