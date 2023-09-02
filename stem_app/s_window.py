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
        self.cards = list(card_info.keys())  # Utilitzem  las claves del JSON como nombres de cartas
        self.cards.extend(self.cards)
        random.shuffle(self.cards)
        
        self.flipped = [False] * 16
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None
        
        self.buttons = []
        self.disabled_pairs = 0  # Inicializa el contador de parejas deshabilitadas
        
        self.card_back_image = tk.PhotoImage(file="card_back.png")
        self.card_images = {}  # Usamos un diccionario en lugar de una lista
        
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
            self.disabled_pairs += 1  # Incrementa el contador de parejas deshabilitadas
            self.show_card_info(self.cards[self.prev_idx])
        else:
            self.buttons[self.prev_idx // 4][self.prev_idx % 4].config(image=self.card_back_image)
            self.buttons[self.prev_idx2 // 4][self.prev_idx2 % 4].config(image=self.card_back_image)
        
        self.flipped[self.prev_idx] = False
        self.flipped[self.prev_idx2] = False
        
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None

        # Verifica si todas las parejas han sido deshabilitadas y cierra la ventana principal si es el caso
        if self.disabled_pairs == len(self.cards) // 2:
            self.root.after(3000, lambda: self.root.destroy())


    def show_card_info(self, card_name):
        card_info = self.card_info.get(card_name, {"titulo": "Sin título", "descripcion": "Sin descripción"})
        title = card_info["titulo"]
        description = card_info["descripcion"]
        
        # Retraso de 1 segundo antes de mostrar la ventana con la descripción
        self.root.after(500, lambda: self.show_description_window(title, description))

    def show_description_window(self, title, description):
        popup_window = tk.Toplevel()
        popup_window.title(title)
    
        # Tamaño predefinido de la ventana (ajusta los valores según tus preferencias)
        popup_window.geometry("400x300")  # Ancho x Alto
        
        # Text widget con scroll
        text_widget = scrolledtext.ScrolledText(popup_window, wrap=tk.WORD, width=40, height=10)  # Ajusta el ancho y alto según tus preferencias
        text_widget.insert(tk.END, description)
        text_widget.pack(fill=tk.BOTH, expand=True)
    
        tk.Button(popup_window, text="OK", command=popup_window.destroy).pack()

        
def open_s_window():
    s_window = tk.Toplevel()
    s_window.title("Juego de Memoria - Ventana S")

    # Intentar cargar la información de las cartas desde el archivo JSON
    try:
        with open("card_info.json", "r") as json_file:
            card_info = json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo JSON no se ha encontrado.")
        s_window.destroy()
        return
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error al cargar el archivo JSON.")
        s_window.destroy()
        return

    game = MemoryGame(s_window, card_info)

    s_window.mainloop()

