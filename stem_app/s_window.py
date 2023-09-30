"""import tkinter as tk
import random
import json
import tkinter.messagebox as messagebox
from tkinter import scrolledtext

class MemoryGame:
    def __init__(self, root, card_info):
        self.root = root
        self.root.title("Memòria científica")
        
        self.card_info = card_info
        self.cards = list(card_info.keys())  # Utilitzem les claus del JSON com a noms de les cartes
        self.cards.extend(self.cards)
        random.shuffle(self.cards)
        
        self.flipped = [False] * 16
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None
        
        self.buttons = []
        self.disabled_pairs = 0  # Inicialitza el comptador de parelles deshabilitades
        
        self.card_back_image = tk.PhotoImage(file="card_back.png")
        self.card_images = {}  # Fem servir un diccionari en lloc d'una llista
        
        for i in range(4):
            row = []
            for j in range(4):
                idx = i * 4 + j
                button = tk.Button(self.root, image=self.card_back_image, command=lambda idx=idx: self.flip_card(idx))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        self.load_card_images()
    
    def load_card_images(self):
        for idx, card in enumerate(self.cards):
            self.card_images[card] = tk.PhotoImage(file=self.card_info[card]["imagen"])
    
    def flip_card(self, idx):
        if self.flipped[idx] or self.num_flipped == 2:
            return
        
        self.flipped[idx] = True
        self.num_flipped += 1
        
        self.buttons[idx // 4][idx % 4].config(image=self.card_images[self.cards[idx]])
        
        if self.num_flipped == 2:
            self.prev_idx2 = idx
            self.root.after(1000, self.check_match)
        else:
            self.prev_idx = idx
    
    def check_match(self):
        if self.cards[self.prev_idx] == self.cards[self.prev_idx2]:
            self.buttons[self.prev_idx // 4][self.prev_idx % 4].config(state=tk.DISABLED)
            self.buttons[self.prev_idx2 // 4][self.prev_idx2 % 4].config(state=tk.DISABLED)
            self.disabled_pairs += 1  # Incrementa el comptador de parelles deshabilitades
            self.show_card_info(self.cards[self.prev_idx])
        else:
            self.buttons[self.prev_idx // 4][self.prev_idx % 4].config(image=self.card_back_image)
            self.buttons[self.prev_idx2 // 4][self.prev_idx2 % 4].config(image=self.card_back_image)
        
        self.flipped[self.prev_idx] = False
        self.flipped[self.prev_idx2] = False
        
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None

        # Verifica si totes les parelles han estat deshabilitades i tanca la finestra principal si és el cas
        if self.disabled_pairs == len(self.cards) // 2:
            self.root.after(3000, lambda: self.root.destroy())


    def show_card_info(self, card_name):
        card_info = self.card_info.get(card_name, {"titulo": "Sense títol", "descripció": "Sense descripció"})
        title = card_info["titulo"]
        description = card_info["descripcion"]
        
        # Retard de 1 segon abans de mostrar la finestra amb la descripció
        self.root.after(500, lambda: self.show_description_window(title, description))

    def show_description_window(self, title, description):
        popup_window = tk.Toplevel()
        popup_window.title(title)
    
        # Mida predefinida de la finestra (ajusta els valors segons les teves preferències)
        popup_window.geometry("400x300")  # Amplada x Alçada
        
        # Text widget amb desplaçament
        text_widget = scrolledtext.ScrolledText(popup_window, wrap=tk.WORD, width=40, height=10)  # Ajusta l'amplada i l'alçada segons les teves preferències
        text_widget.insert(tk.END, description)
        text_widget.pack(fill=tk.BOTH, expand=True)
    
        tk.Button(popup_window, text="OK", command=popup_window.destroy).pack()

        
def open_s_window():
    s_window = tk.Toplevel()
    s_window.title("Joc de Memòria - Finestra S")

    # Intentar carregar la informació de les cartes des de l'arxiu JSON
    try:
        with open("card_info.json", "r") as json_file:
            card_info = json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "L'arxiu JSON no s'ha trobat.")
        s_window.destroy()
        return
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error en carregar l'arxiu JSON.")
        s_window.destroy()
        return

    game = MemoryGame(s_window, card_info)

    s_window.mainloop()

    """
import tkinter as tk
import random
import json
import tkinter.messagebox as messagebox
from tkinter import scrolledtext

class MemoryGame:
    def __init__(self, root, card_info):
        self.root = root
        self.root.title("Memòria científica")
        
        self.card_info = card_info
        self.cards = list(card_info.keys())  # Utilitzem les claus del JSON com a noms de les cartes
        self.cards.extend(self.cards)
        random.shuffle(self.cards)
        
        self.flipped = [False] * 16
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None
        
        self.buttons = []
        self.disabled_pairs = 0  # Inicialitza el comptador de parelles deshabilitades
        self.attempts = 0  # Inicialitza el comptador d'intents
        
        self.card_back_image = tk.PhotoImage(file="card_back.png")
        self.card_images = {}  # Fem servir un diccionari en lloc d'una llista
        
        for i in range(4):
            row = []
            for j in range(4):
                idx = i * 4 + j
                button = tk.Button(self.root, image=self.card_back_image, command=lambda idx=idx: self.flip_card(idx))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        self.load_card_images()
    
    def load_card_images(self):
        for idx, card in enumerate(self.cards):
            self.card_images[card] = tk.PhotoImage(file=self.card_info[card]["imagen"])
    
    def flip_card(self, idx):
        if self.flipped[idx] or self.num_flipped == 2:
            return
        
        self.flipped[idx] = True
        self.num_flipped += 1
        
        self.buttons[idx // 4][idx % 4].config(image=self.card_images[self.cards[idx]])
        
        if self.num_flipped == 2:
            self.prev_idx2 = idx
            self.root.after(1000, self.check_match)
        else:
            self.prev_idx = idx
    
    def check_match(self):
        self.attempts += 1  # Incrementa el comptador d'intents
        
        if self.cards[self.prev_idx] == self.cards[self.prev_idx2]:
            self.buttons[self.prev_idx // 4][self.prev_idx % 4].config(state=tk.DISABLED)
            self.buttons[self.prev_idx2 // 4][self.prev_idx2 % 4].config(state=tk.DISABLED)
            self.disabled_pairs += 1  # Incrementa el comptador de parelles deshabilitades
            self.show_card_info(self.cards[self.prev_idx])
        else:
            self.buttons[self.prev_idx // 4][self.prev_idx % 4].config(image=self.card_back_image)
            self.buttons[self.prev_idx2 // 4][self.prev_idx2 % 4].config(image=self.card_back_image)
        
        self.flipped[self.prev_idx] = False
        self.flipped[self.prev_idx2] = False
        
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None

        # Verifica si totes les parelles han estat deshabilitades i tanca la finestra principal si és el cas
        if self.disabled_pairs == len(self.cards) // 2:
            self.root.after(3000, lambda: self.mostra_resultats())

    def show_card_info(self, card_name):
        card_info = self.card_info.get(card_name, {"titulo": "Sense títol", "descripcion": "Sense descripció"})
        title = card_info["titulo"]
        description = card_info["descripcion"]
        
        # Retard de 1 segon abans de mostrar la finestra amb la descripció
        self.root.after(500, lambda: self.mostra_descripcio(title, description))

    def mostra_descripcio(self, title, description):
        popup_window = tk.Toplevel()
        popup_window.title(title)
    
        # Mida predefinida de la finestra (ajusta els valors segons les teves preferències)
        popup_window.geometry("400x300")  # Amplada x Alçada
        
        # Text widget amb desplaçament
        text_widget = scrolledtext.ScrolledText(popup_window, wrap=tk.WORD, width=40, height=10)  # Ajusta l'amplada i l'alçada segons les teves preferències
        text_widget.insert(tk.END, description)
        text_widget.pack(fill=tk.BOTH, expand=True)
    
        tk.Button(popup_window, text="OK", command=popup_window.destroy).pack()

    def mostra_resultats(self):
        result_window = tk.Toplevel()
        result_window.title("Resultats")
        
        # Mostra el nombre d'encerts vs. el total d'intents com a cadena formatada
        resultat = f"Encerts: {self.disabled_pairs}/{self.attempts} intents"
        
        result_label = tk.Label(result_window, text=resultat)
        result_label.pack(padx=10, pady=10)
        
        tk.Button(result_window, text="Tancar", command=result_window.destroy).pack()

        
def open_s_window():
    s_window = tk.Toplevel()
    s_window.title("Joc de Memòria - Finestra S")

    # Intenta carregar la informació de les cartes des de l'arxiu JSON
    try:
        with open("card_info.json", "r") as json_file:
            card_info = json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "L'arxiu JSON no s'ha trobat.")
        s_window.destroy()
        return
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error en carregar l'arxiu JSON.")
        s_window.destroy()
        return

    game = MemoryGame(s_window, card_info)

    s_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Joc de Memòria")
    open_s_window()
    root.mainloop()
