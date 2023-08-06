import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        
        self.cards = [f"image{i}.png" for i in range(1, 9)]
        self.cards.extend(self.cards)
        random.shuffle(self.cards)
        
        self.flipped = [False] * 16
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None
        
        self.buttons = []
        
        self.card_back_image = tk.PhotoImage(file="card_back.png")
        self.card_images = [tk.PhotoImage(file=card) for card in self.cards]
        
        for i in range(4):
            row = []
            for j in range(4):
                idx = i * 4 + j
                button = tk.Button(self.root, image=self.card_back_image, command=lambda idx=idx: self.flip_card(idx))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
    
    def flip_card(self, idx):
        if self.flipped[idx] or self.num_flipped == 2:
            return
        
        self.flipped[idx] = True
        self.num_flipped += 1
        
        self.buttons[idx // 4][idx % 4].config(image=self.card_images[idx])
        
        if self.num_flipped == 2:
            self.prev_idx2 = idx
            self.root.after(2000, self.check_match)
        else:
            self.prev_idx = idx
    
    def check_match(self):
        if self.cards[self.prev_idx] == self.cards[self.prev_idx2]:
            self.buttons[self.prev_idx // 4][self.prev_idx % 4].config(state=tk.DISABLED)
            self.buttons[self.prev_idx2 // 4][self.prev_idx2 % 4].config(state=tk.DISABLED)
        else:
            self.buttons[self.prev_idx // 4][self.prev_idx % 4].config(image=self.card_back_image)
            self.buttons[self.prev_idx2 // 4][self.prev_idx2 % 4].config(image=self.card_back_image)
        
        self.flipped[self.prev_idx] = False
        self.flipped[self.prev_idx2] = False
        
        self.num_flipped = 0
        self.prev_idx = None
        self.prev_idx2 = None

def open_s_window():
    s_window = tk.Toplevel()
    s_window.title("Memory Game - S Window")
    
    game = MemoryGame(s_window)

    s_window.mainloop()

