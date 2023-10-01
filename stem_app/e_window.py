
"""
import tkinter as tk

def open_e_window():
    e_window = tk.Toplevel()
    e_window.title("E Window")
    
    label = tk.Label(e_window, text="Aquesta és la finestra E.")
    label.pack()
"""
"""
import tkinter as tk

class CuriosityGame:
    def __init__(self, root):
        self.root = root
        self.root.title("SABIES QUE...")
        
        self.curiosities = [
            "Sophie Germain (1776) es va haver de disfressar sota el nom de LeBlanc perquè en aquella època les dones no eren acceptades en el món de les matemàtiques i quan va morir, tristament, en el seu certificat de defunció la va identificar simplement com a rendista, sense esmentar els seus èxits en matemàtiques i ciència.",
            "Avui en dia, tothom sap que Newton va descobrir la gravetat, que Darwin va descobrir l'evolució, i que Einstein va descobrir la relativitat. Però quan es tracta de la composició del nostre univers, els llibres de text diuen simplement que l'àtom més abundant de l'univers és l'hidrogen. I ningú no es pregunta com sabem qui ho va descriure així.  La realitat és que Cecilia Payne és la responsable d'aquest descobriment.",
            "Margaret Hamilton va ser una figura clau pel desenvolupament del programari de navegació per a la missió Apol·lo de la NASA que va portar a l'arribada de l'home a la Lluna. El conjunt del codi era més alt que ella! "
        ]
        
        self.current_curiosity = 0
        
        self.curiosity_label = tk.Label(self.root, text="", wraplength=400)
        self.curiosity_label.pack(pady=10)
        
        self.prev_button = tk.Button(self.root, text="Anterior", command=self.prev_curiosity)
        self.prev_button.pack(side=tk.LEFT, padx=10)
        
        self.next_button = tk.Button(self.root, text="Següent", command=self.next_curiosity)
        self.next_button.pack(side=tk.RIGHT, padx=10)

              
        self.display_curiosity()
    
    def display_curiosity(self):
        self.curiosity_label.config(text=self.curiosities[self.current_curiosity])

    
    def next_curiosity(self):
        if self.current_curiosity < len(self.curiosities) - 1:
            self.current_curiosity += 1
            self.display_curiosity()
    
    def prev_curiosity(self):
        if self.current_curiosity > 0:
            self.current_curiosity -= 1
            self.display_curiosity()

           

def open_e_window():
    e_window = tk.Toplevel()
    e_window.title("E Window")
    
    game = CuriosityGame(e_window)

    e_window.mainloop()

"""

import tkinter as tk
import json

class CuriosityGame:
    def __init__(self, root, curiosities_data):
        self.root = root
        self.root.title("Curiositats")
        
        self.curiosities_data = curiosities_data
        self.current_curiosity = 0
        
        self.text_label = tk.Label(self.root, text="", wraplength=400)
        self.text_label.pack(pady=10)
        
        self.image_label = tk.Label(self.root)
        self.image_label.pack()
        
        self.next_button = tk.Button(self.root, text="Següent", command=self.next_curiosity)
        self.next_button.pack(pady=10)
        
        self.display_curiosity()
    
    def display_curiosity(self):
        if 0 <= self.current_curiosity < len(self.curiosities_data):
            curiosity = self.curiosities_data[self.current_curiosity]
            self.text_label.config(text=curiosity["text"])
            
            # Carga y muestra la imagen
            image_path = curiosity["foto"]
            image = tk.PhotoImage(file=image_path)
            self.image_label.config(image=image)
            self.image_label.image = image  # Mantén una referencia para evitar que la imagen se elimine
        else:
            # Cuando se llega al final de las curiosidades
            self.text_label.config(text="No hi ha més curiositats.")
            self.image_label.config(image=None)
            self.next_button.config(state="disabled")
    
    def next_curiosity(self):
        self.current_curiosity += 1
        self.display_curiosity()

def open_e_window():
    e_window = tk.Toplevel()
    e_window.title("Finestra E")
    
    with open("e-info.json", "r", encoding="utf-8") as json_file:
        curiosities_data = json.load(json_file)["curiositats"]
    
    game = CuriosityGame(e_window, curiosities_data)

    e_window.mainloop()

